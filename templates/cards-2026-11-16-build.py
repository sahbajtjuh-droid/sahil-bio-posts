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

# ---------- hexagon molecule ----------
def hexa(cx,cy,r,state,col=AZ,ink=INK):
    pts=' '.join(f'{cx+r*math.cos(math.radians(60*i-30)):.1f},{cy+r*math.sin(math.radians(60*i-30)):.1f}' for i in range(6))
    if state=='pass':
        inner_pts=' '.join(f'{cx+r*0.55*math.cos(math.radians(60*i-30)):.1f},{cy+r*0.55*math.sin(math.radians(60*i-30)):.1f}' for i in range(6))
        return f'<polygon points="{pts}" fill="{col}"/><polygon points="{inner_pts}" fill="none" stroke="#fff" stroke-width="2"/>'
    return f'<polygon points="{pts}" fill="none" stroke="{ink}" stroke-width="2" opacity="0.45"/><line x1="{cx-r*0.6:.1f}" y1="{cy+r*0.6:.1f}" x2="{cx+r*0.6:.1f}" y2="{cy-r*0.6:.1f}" stroke="{ink}" stroke-width="2" opacity="0.45"/>'
def hexgrid(n,passed,cols,r=22,gap=52):
    rows=math.ceil(n/cols); w=cols*gap+gap/2; h=rows*gap*0.9+gap/2
    out=''
    for i in range(n):
        c,rr=i%cols,i//cols
        x=gap/2+c*gap+(gap/2 if rr%2 else 0); y=gap/2+rr*gap*0.88
        out+=hexa(x,y,r,'pass' if i<passed else 'fail')
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" aria-hidden="true">{out}</svg>'
def gate_icon(col):
    return f'<svg width="74" height="54" viewBox="0 0 74 54" aria-hidden="true"><rect x="4" y="6" width="8" height="46" rx="2" fill="{col}"/><rect x="62" y="6" width="8" height="46" rx="2" fill="{col}"/><rect x="4" y="6" width="66" height="8" rx="2" fill="{col}"/><circle cx="8" cy="4" r="4" fill="{col}"/><circle cx="66" cy="4" r="4" fill="{col}"/></svg>'
def compare(ai_lbl, ai_pct, ind_lo, ind_hi, ind_lbl):
    # horizontal scale 0-100
    W=380
    return f'''<div style="margin-top:22px;display:flex;flex-direction:column;gap:12px">
<div style="display:grid;grid-template-columns:96px 1fr 110px;align-items:center;gap:12px"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.1em;font-weight:600;color:{AZD}">AI</span><span style="position:relative;height:16px;background:rgba(17,28,22,0.08);border-radius:8px"><span style="position:absolute;left:0;top:0;bottom:0;width:{ai_pct}%;background:{AZ};border-radius:8px"></span></span><span style="font-family:'Newsreader',serif;font-size:30px;color:{AZD}">{ai_lbl}</span></div>
<div style="display:grid;grid-template-columns:96px 1fr 110px;align-items:center;gap:12px"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.1em;color:{MUT}">INDUSTRY</span><span style="position:relative;height:16px;background:rgba(17,28,22,0.08);border-radius:8px"><span style="position:absolute;left:{ind_lo}%;width:{ind_hi-ind_lo}%;top:0;bottom:0;border-radius:8px;background:repeating-linear-gradient(-45deg,rgba(17,28,22,0.45) 0 2px,transparent 2px 7px);box-shadow:inset 0 0 0 1.5px rgba(17,28,22,0.5)"></span></span><span style="font-family:'Newsreader',serif;font-size:22px;color:{INK};white-space:nowrap">{ind_lbl}</span></div>
</div>'''
def gatecard(no,phase,q,passed,total,cols,ai_lbl,ai_pct,lo,hi,ind_lbl):
    return f'''<div style="background:#fff;border-radius:8px;padding:28px 30px 30px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">
<div style="display:flex;align-items:center;gap:18px">{gate_icon(AZ if no==1 else INK)}<div><div style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.14em;font-weight:600;color:{AZD if no==1 else INK}">GATE {no} · {phase}</div><div style="font-family:'Newsreader',serif;font-style:italic;font-size:30px;line-height:1.1;margin-top:4px">{q}</div></div></div>
<div style="margin-top:22px"><div style="font-family:'Newsreader',serif;font-size:76px;line-height:1;white-space:nowrap;color:{AZ if no==1 else INK}">{passed} of {total}</div><div style="margin-top:6px;font-size:20px;color:{MUT}">AI-discovered molecules passed</div></div>
<div style="margin-top:16px">{hexgrid(total,passed,cols)}</div>
{compare(ai_lbl,ai_pct,lo,hi,ind_lbl)}
</div>'''
ai=card(PAPER,INK,f'''
<div style="font-family:'Newsreader',serif;font-size:84px;line-height:0.98;letter-spacing:-0.02em">AI clears the first gate.<br><span style="font-style:italic;color:{AZ}">Not the second.</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start">
{gatecard(1,'PHASE 1','Is it safe?',21,24,8,'88%',88,40,65,'40 to 65%')}
{gatecard(2,'PHASE 2','Does it work?',4,10,5,'40%',40,30,40,'30 to 40%')}
</div>
<div style="display:grid;grid-template-columns:1fr 420px;gap:36px;align-items:center">
  <div style="font-size:24px;line-height:1.38;color:#2A3530"><b style="font-weight:600">Why the split.</b> Phase 1 tests the molecule, which AI can design on a computer. Phase 2 tests the biology, which no model can predict yet.</div>
  <div style="background:#fff;border-radius:6px;padding:22px 26px 24px;box-shadow:0 18px 40px rgba(17,28,22,0.14),0 2px 6px rgba(17,28,22,0.08);transform:rotate(-2deg)">
    <div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.16em;color:{MUT}">CONFIRMED · IQVIA, 2026</div>
    <div style="margin-top:10px;font-family:'Newsreader',serif;font-size:27px;line-height:1.16">AI-enabled emerging biotechs: <span style="color:{AZ};font-style:italic">75% pass Phase 1.</span> Phase 2 on par with peers.</div>
  </div>
</div>''',footer('SOURCES: BCG 2024 · IQVIA 2026 · NOT INVESTMENT ADVICE',INK,MUT,'rgba(17,28,22,0.18)'),topbar('AI IN THE CLINIC','FOR INVESTORS · THE SCIENCE SIDE','#1A66CC',INK,'rgba(17,28,22,0.2)'))

# ---------- price tags (take) ----------
def tag(w,h,rot,top_lbl,big,small,fill,ink,sub):
    return f'''<div style="position:relative;width:{w}px;transform:rotate({rot}deg);transform-origin:50% 0">
<svg width="{w}" height="70" viewBox="0 0 {w} 70" aria-hidden="true" style="display:block"><path d="M{w/2},0 C{w/2-20},30 {w/2-4},50 {w/2},70" fill="none" stroke="{INK2}" stroke-width="2"/></svg>
<div style="position:relative;background:{fill};color:{ink};border-radius:10px 10px 10px 10px;padding:{h}px 30px 30px;clip-path:polygon(50% 0,100% 16%,100% 100%,0 100%,0 16%);box-shadow:0 14px 30px rgba(26,22,19,0.18)">
<div style="position:absolute;left:50%;top:22px;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:{WARM};box-shadow:inset 0 0 0 2px {INK2}"></div>
<div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.14em;font-weight:600;opacity:0.85">{top_lbl}</div>
<div style="margin-top:10px;font-family:'Newsreader',serif;font-size:{big[1]}px;line-height:1">{big[0]}</div>
<div style="margin-top:8px;font-size:20px;line-height:1.3;opacity:0.9">{small}</div>
</div></div>'''
def trend():
    # schematic: candidates line doubles, approvals flat
    W,H=420,250
    return f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" aria-hidden="true">
<line x1="30" y1="210" x2="400" y2="210" stroke="{INK2}" stroke-width="1.5" opacity="0.5"/>
<path d="M30,150 C140,140 260,100 400,40" fill="none" stroke="{OR}" stroke-width="5" stroke-linecap="round"/>
<path d="M30,175 L400,175" fill="none" stroke="{INK2}" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 12"/>
<text x="400" y="28" font-family="IBM Plex Mono" font-size="15" font-weight="600" fill="{ORD}" text-anchor="end">CANDIDATES · ROUGHLY 2×</text>
<text x="400" y="200" font-family="IBM Plex Mono" font-size="15" font-weight="600" fill="{INK2}" text-anchor="end">FDA APPROVALS · ~50 A YEAR</text>
<text x="30" y="236" font-family="IBM Plex Mono" font-size="14" fill="{MUT2}">10 YEARS AGO</text>
<text x="400" y="236" font-family="IBM Plex Mono" font-size="14" fill="{MUT2}" text-anchor="end">NOW</text>
</svg>'''
take=card(WARM,INK2,f'''
<div style="font-family:'Newsreader',serif;font-size:72px;line-height:1.02;letter-spacing:-0.02em">Your molecule is getting cheaper to find.<br><span style="font-style:italic;color:{OR}">Proof that it works is not.</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start">
  <div style="display:flex;flex-direction:column;align-items:center;padding-top:6px">{tag(360,58,-5,'PRECLINICAL ASSET',('Tens of millions',44),'Typical upfront in a discovery deal','#fff',INK2,'')}</div>
  <div style="display:flex;flex-direction:column;align-items:center">{tag(420,64,4,'AFTER STRONG PHASE 2 DATA',('Hundreds of millions to billions',52),'What pharma may pay for a similar asset',OR,'#fff','')}</div>
</div>
<div style="display:grid;grid-template-columns:440px 1fr;gap:40px;align-items:center;padding-top:10px;border-top:1px solid rgba(26,22,19,0.18)">
  <div><div style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.14em;color:{MUT2};margin:18px 0 6px">SUPPLY OF DRUG CANDIDATES VS APPROVALS</div>{trend()}</div>
  <div style="background:#fff;border-radius:6px;padding:24px 28px 26px;box-shadow:0 18px 40px rgba(26,22,19,0.15),0 2px 6px rgba(26,22,19,0.08);transform:rotate(-2deg)">
    <div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.16em;color:{MUT2}">FOR YOUR SPINOUT</div>
    <div style="margin-top:10px;font-family:'Newsreader',serif;font-size:31px;line-height:1.14">Plan the path to first human data <span style="font-style:italic;color:{OR}">before you plan the company.</span></div>
  </div>
</div>''',footer('SOURCE: B. LIU, FORMATION BIO, IN A16Z NEWS · TREND SCHEMATIC',INK2,MUT2,'rgba(26,22,19,0.18)'),topbar('THE TAKE','FOR SCIENTISTS · THE BUSINESS SIDE','#C93D1A',INK2,'rgba(26,22,19,0.2)'))

# ---------- China number card ----------
def cap(x,y,on):
    w,h=52,22
    if on: return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{AZ}"/><line x1="{x+w/2}" y1="{y+3}" x2="{x+w/2}" y2="{y+h-3}" stroke="#fff" stroke-width="2"/>'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{INK}" stroke-width="1.8" opacity="0.5"/>'
caps=''
for i in range(79):
    c,r=i%10,i//10
    caps+=cap(4+c*64,4+r*40,i<30)
capsvg=f'<svg width="644" height="324" viewBox="0 0 644 324" aria-hidden="true">{caps}</svg>'
china=card(PAPER,INK,f'''
<div style="font-family:'Newsreader',serif;font-size:84px;line-height:0.98;letter-spacing:-0.02em">79 new medicines in 2025.<br><span style="font-style:italic;color:{AZ}">30 launched only in China.</span></div>
<div style="display:grid;grid-template-columns:644px 1fr;gap:36px;align-items:center">
  <div>{capsvg}<div style="margin-top:12px;font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{MUT}">EACH CAPSULE IS ONE NEW MEDICINE LAUNCHED IN 2025</div></div>
  <div style="display:flex;flex-direction:column;gap:22px">
    <div style="display:flex;align-items:center;gap:14px"><svg width="52" height="22" viewBox="0 0 52 22" aria-hidden="true">{cap(0,0,True)}</svg><span style="font-size:22px;line-height:1.3"><b style="font-weight:600;color:{AZD}">30</b> launched only in China</span></div>
    <div style="display:flex;align-items:center;gap:14px"><svg width="54" height="24" viewBox="0 0 54 24" aria-hidden="true">{cap(1,1,False)}</svg><span style="font-size:22px;line-height:1.3"><b style="font-weight:600">49</b> launched in at least one other country</span></div>
  </div>
</div>
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px">
  <div style="background:#fff;border-radius:8px;padding:22px 24px;box-shadow:0 10px 26px rgba(17,28,22,0.09)"><div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.14em;color:{MUT}">CHINA AND INTERNATIONAL DEALS</div><div style="margin-top:10px;font-family:'Newsreader',serif;font-size:36px;line-height:1.05;color:{AZD}">All-time high</div></div>
  <div style="background:#fff;border-radius:8px;padding:22px 24px;box-shadow:0 10px 26px rgba(17,28,22,0.09);transform:rotate(1.5deg)"><div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.14em;color:{MUT}">WESTERN EUROPE AS TRIAL SITE</div><div style="margin-top:10px;font-family:'Newsreader',serif;font-size:36px;line-height:1.05">17% below 2019</div></div>
  <div style="background:#fff;border-radius:8px;padding:22px 24px;box-shadow:0 10px 26px rgba(17,28,22,0.09)"><div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.14em;color:{MUT}">TRIAL STARTS IN 2025</div><div style="margin-top:10px;font-family:'Newsreader',serif;font-size:30px;line-height:1.1">Up for US sponsors, down for European and Chinese</div></div>
</div>''',footer('SOURCE: IQVIA INSTITUTE, GLOBAL R&D TRENDS 2026',INK,MUT,'rgba(17,28,22,0.18)'),topbar('BY THE NUMBERS','FOR INVESTORS · THE SCIENCE SIDE','#1A66CC',INK,'rgba(17,28,22,0.2)'))

for name,html in [('ai',ai),('take',take),('china',china)]:
    open(f'{name}-render.html','w').write(head+html+'\n</body></html>')
