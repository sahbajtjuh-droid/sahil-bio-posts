import math, random
head=open('/home/claude/posts/s1-render.html').read()
head=head[:head.index('<div id="img-s1"')]
F='/home/claude/render/node_modules/@fontsource'
head=head.replace('*{box-sizing',f"@font-face{{font-family:'Newsreader';font-weight:600;font-style:normal;src:url({F}/newsreader/files/newsreader-latin-600-normal.woff2)}}\n*{{box-sizing")
NOISE='''<div style="position:absolute;inset:0;background-image:url('data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22140%22%20height=%22140%22%3E%3Cfilter%20id=%22n%22%3E%3CfeTurbulence%20type=%22fractalNoise%22%20baseFrequency=%220.85%22%20numOctaves=%222%22%20stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect%20width=%22100%25%22%20height=%22100%25%22%20filter=%22url(%23n)%22/%3E%3C/svg%3E');background-size:180px;opacity:0.10;mix-blend-mode:multiply;pointer-events:none;z-index:5"></div>'''
INK='#111C16'; AZ='#1C74E0'; AZD='#1559B4'; MUT='#68766E'; PAPER='#EEF4F0'
OR='#E0451F'; ORD='#B23A17'; INK2='#1A1613'; WARM='#F4F0E8'; MUT2='#6e685c'
def topbar(label, tag, tagbg, ink, line):
    return f'''<div style="position:relative;display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:'IBM Plex Mono';font-size:24px;font-weight:500;letter-spacing:0.22em;color:{ink}">{label}</span><span style="font-family:'IBM Plex Mono';font-size:18px;letter-spacing:0.14em;font-weight:600;color:#fff;background:{tagbg};padding:8px 14px;border-radius:3px">{tag}</span></div><div style="height:1px;background:{line};margin-top:30px"></div>'''
def footer(left, ink, mut, line):
    return f'''<div style="position:absolute;left:104px;right:104px;bottom:72px;display:flex;justify-content:space-between;gap:24px;padding-top:20px;border-top:1px solid {line};font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{mut}"><span>{left}</span><span style="color:{ink};white-space:nowrap">SAHIL BAJAJ · @SAHIL_BIO</span></div>'''
def card(bg,color,inner,footer_html,top):
    return f'''<div id="card" style="position:relative;width:1200px;height:1500px;background:{bg};color:{color};overflow:hidden;padding:96px 104px 0">{NOISE}
{top}
<div style="display:flex;flex-direction:column;justify-content:space-between;height:1170px;padding-top:44px">
{inner}
</div>
{footer_html}
</div>'''
def H(t,acc,col,size=84):
    return f'''<div style="font-family:'Newsreader',serif;font-size:{size}px;line-height:0.98;letter-spacing:-0.02em">{t}<br><span style="font-style:italic;color:{col}">{acc}</span></div>'''
def mono(t,size=15,col=None,w=500,ls=0.14):
    c=f'color:{col};' if col else ''
    return f'''<span style="font-family:'IBM Plex Mono';font-size:{size}px;letter-spacing:{ls}em;font-weight:{w};{c}">{t}</span>'''
def note(lbl,body,rot,mut,w=None):
    ww=f'width:{w}px;' if w else ''
    return f'''<div style="{ww}background:#fff;border-radius:6px;padding:22px 26px 24px;box-shadow:0 18px 40px rgba(17,28,22,0.14),0 2px 6px rgba(17,28,22,0.08);transform:rotate({rot}deg)"><div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.16em;color:{mut}">{lbl}</div><div style="margin-top:10px;font-family:'Newsreader',serif;font-size:28px;line-height:1.16">{body}</div></div>'''
BTAG=('THE BUSINESS SIDE','FOR SCIENTISTS · THE BUSINESS SIDE','#C93D1A')
STAG=('THE SCIENCE SIDE','FOR INVESTORS · THE SCIENCE SIDE','#1A66CC')
def bcard(label,inner,src):
    return card(WARM,INK2,inner,footer(src,INK2,MUT2,'rgba(26,22,19,0.18)'),topbar(label,BTAG[1],BTAG[2],INK2,'rgba(26,22,19,0.2)'))
def scard(label,inner,src):
    return card(PAPER,INK,inner,footer(src,INK,MUT,'rgba(17,28,22,0.18)'),topbar(label,STAG[1],STAG[2],INK,'rgba(17,28,22,0.2)'))
def page(html):
    return head+html+'\n</body></html>'
