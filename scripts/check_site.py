"""Mandatory pre-push check for index.html. Usage: python3 scripts/check_site.py
Fails (exit 1) on malformed HTML, mismatched carousel img/dot counts, or layout overflow."""
import re, sys
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright

PATH = "index.html"
VOID = {"img","br","meta","link","input","hr"}
src = open(PATH, encoding="utf-8").read()
errs = []

# 1. Tag balance with a real parser (base64 stripped for speed)
class P(HTMLParser):
    def __init__(s): super().__init__(); s.stack=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.stack.append((t,s.getpos()))
    def handle_startendtag(s,t,a): pass
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.stack or s.stack[-1][0]!=t:
            errs.append(f"unbalanced </{t}> at {s.getpos()}, open: {s.stack[-1] if s.stack else None}")
            for i in range(len(s.stack)-1,-1,-1):
                if s.stack[i][0]==t: del s.stack[i:]; break
        else: s.stack.pop()
stripped = re.sub(r'(data:image/\w+;base64,)[A-Za-z0-9+/=]+', r'\1B64', src)
p=P(); p.feed(stripped)
for t,pos in p.stack:
    if t not in ("html","body","head"): errs.append(f"unclosed <{t}> at {pos}")

# 2. Render: per-card img/dot counts, card isolation, overflow, JS errors
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for w in (320, 390, 1440):
        pg = b.new_page(viewport={"width": w, "height": 844}); js=[]
        pg.on("pageerror", lambda e: js.append(str(e)))
        pg.goto("file:///home/claude/tableandco/"+PATH)
        r = pg.evaluate("""()=>[...document.querySelectorAll('.collection-card')].map(c=>({
            imgs:c.querySelectorAll('.carousel-track > img').length,
            dots:c.querySelectorAll('.carousel-dots > .dot').length,
            arrows:c.querySelectorAll('.carousel-arrow').length,
            inner:c.querySelectorAll('.collection-card').length,
            carousels:c.querySelectorAll('.carousel').length})) """)
        for i,c in enumerate(r,1):
            if c["imgs"]!=c["dots"] and c["imgs"]>0: errs.append(f"{w}px card {i}: {c['imgs']} imgs vs {c['dots']} dots")
            if c["arrows"]!=2 or c["carousels"]!=1 or c["inner"]!=0: errs.append(f"{w}px card {i}: bad structure {c}")
        if len(r)!=6: errs.append(f"{w}px: expected 6 cards, found {len(r)}")
        if pg.evaluate("document.documentElement.scrollWidth")>w: errs.append(f"{w}px: horizontal overflow")
        errs += [f"{w}px JS error: {e}" for e in js]
        if w==390: pg.screenshot(path="/tmp/check_390.png", full_page=False)
    b.close()
print("FAIL\n"+"\n".join(errs) if errs else "OK")
sys.exit(1 if errs else 0)
