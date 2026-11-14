import math
head=open('/home/claude/posts/s1-render.html').read()
head=head[:head.index('<div id="img-s1"')]
NOISE='''<div style="position:absolute;inset:0;background-image:url('data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22140%22%20height=%22140%22%3E%3Cfilter%20id=%22n%22%3E%3CfeTurbulence%20type=%22fractalNoise%22%20baseFrequency=%220.85%22%20numOctaves=%222%22%20stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect%20width=%22100%25%22%20height=%22100%25%22%20filter=%22url(%23n)%22/%3E%3C/svg%3E');background-size:180px;opacity:0.10;mix-blend-mode:multiply;pointer-events:none;z-index:5"></div>'''
INK='#111C16'; AZ='#1C74E0'; AZD='#1559B4'; MUT='#68766E'; PAPER='#EEF4F0'
OR='#E0451F'; ORD='#B23A17'; INK2='#1A1613'; WARM='#F4F0E8'; MUT2='#6e685c'

def topbar(label, tag, tagbg, ink, line):
    return f'''<div style="position:relative;display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:'IBM Plex Mono';font-size:24px;font-weight:500;letter-spacing:0.22em;color:{ink}">{label}</span><span style="font-family:'IBM Plex Mono';font-size:18px;letter-spacing:0.14em;font-weight:600;color:#fff;background:{tagbg};padding:8px 14px;border-radius:3px">{tag}</span></div><div style="height:1px;background:{line};margin-top:30px"></div>'''
def footer(left, ink, mut, line):
    return f'''<div style="position:absolute;left:104px;right:104px;bottom:72px;display:flex;justify-content:space-between;padding-top:20px;border-top:1px solid {line};font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{mut}"><span>{left}</span><span style="color:{ink}">SAHIL BAJAJ · @SAHIL_BIO</span></div>'''

# ================= 1. TRIAL ODDS: 100 capsules =================
def capsule(x,y,kind):
    w,h=52,24; r=h/2
    if kind=='p1':   fill,stroke,op,extra='none','#9AA59F',0.9,''
    elif kind=='p2': fill,stroke,op,extra='none',AZ,1,f'<line x1="{x+8}" y1="{y+h-4}" x2="{x+w-8}" y2="{y+4}" stroke="{AZ}" stroke-width="2.2"/>'
    elif kind=='p3': fill,stroke,op,extra='none',INK,1,f'<line x1="{x+8}" y1="{y+h-4}" x2="{x+w-8}" y2="{y+4}" stroke="{INK}" stroke-width="2"/>'
    elif kind=='fi': fill,stroke,op,extra='none',INK,1,f'<line x1="{x+8}" y1="{y+h-4}" x2="{x+w-8}" y2="{y+4}" stroke="{INK}" stroke-width="2"/>'
    else:            fill,stroke,op,extra=AZ,AZ,1,f'<line x1="{x+w/2}" y1="{y+3}" x2="{x+w/2}" y2="{y+h-3}" stroke="#fff" stroke-width="2"/>'
    dash=' stroke-dasharray="3 3"' if kind=='p1' else ''
    return f'<g opacity="{op}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"{dash}/>{extra}</g>'
kinds=['p1']*48+['p2']*37+['p3']*6+['fi']*1+['ap']*8
cells=''
gx,gy,dx,dy=0,0,64,46
pos={}
for i,k in enumerate(kinds):
    c,r=i%10,i//10
    x,y=gx+c*dx,gy+r*dy
    cells+=capsule(x,y,k); pos.setdefault(k,[]).append((x,y))
# brackets on right of grid
def note(y,label,count,color,bold=False):
    fw='600' if bold else '500'
    return f'''<div style="position:absolute;left:0;top:{y}px;display:flex;align-items:baseline;gap:14px"><span style="font-family:'Newsreader',serif;font-size:{56 if bold else 40}px;line-height:1;color:{color}">{count}</span><span style="font-size:{24 if bold else 21}px;line-height:1.25;font-weight:{fw};color:{color};max-width:260px">{label}</span></div>'''
gridsvg=f'<svg width="630" height="452" viewBox="0 -2 630 452" aria-hidden="true">{cells}</svg>'
legend=(note(0,'stop after Phase 1',48,MUT)+note(92,'stop in Phase 2.<br>The biggest loss.',37,AZD,True)+note(216,'stop in Phase 3',6,INK)+note(286,'stopped at filing',1,INK)+note(356,'approved',8,AZ,True))
# mock press release with annotations
pr_lines=''.join(f'<div style="height:10px;border-radius:5px;background:rgba(17,28,22,0.13);width:{w}%;margin-top:12px"></div>' for w in [100,94,98,70])
pins=[("01","Primary endpoint, set before the trial?"),("02","Randomised and blinded?"),("03","Patient outcome, or a biomarker?"),("04","Whole trial, or a subgroup found later?"),("05","Better than today's treatment?")]
pinh=''.join(f'''<div style="display:flex;align-items:center;gap:14px;padding:9px 0;border-top:1px solid rgba(17,28,22,0.15)"><span style="flex:0 0 auto;width:34px;height:34px;border-radius:50%;background:{AZ};color:#fff;font-family:'IBM Plex Mono';font-size:15px;font-weight:600;display:flex;align-items:center;justify-content:center">{n}</span><span style="font-size:22px;line-height:1.25">{t}</span></div>''' for n,t in pins)
trial=f'''<div id="card" style="position:relative;width:1200px;height:1500px;background:{PAPER};color:{INK};overflow:hidden;padding:96px 104px 0">{NOISE}
{topbar('TRIAL ODDS','FOR INVESTORS · THE SCIENCE SIDE','#1A66CC',INK,'rgba(17,28,22,0.2)')}
<div style="margin-top:44px;font-family:'Newsreader',serif;font-size:84px;line-height:0.98;letter-spacing:-0.02em">100 drugs enter trials.<br><span style="font-style:italic;color:{AZ}">8 come out.</span></div>
<div style="position:relative;margin-top:48px;display:flex;gap:44px;align-items:flex-start">
  <div>{gridsvg}<div style="margin-top:10px;font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{MUT}">EACH CAPSULE IS ONE DRUG IN CLINICAL TRIALS</div></div>
  <div style="position:relative;flex:1;height:452px">{legend}</div>
</div>
<div style="position:relative;margin-top:84px;display:grid;grid-template-columns:430px minmax(0,1fr);gap:40px;align-items:start">
  <div style="background:#fff;border-radius:6px;padding:26px 28px 30px;box-shadow:0 18px 40px rgba(17,28,22,0.14),0 2px 6px rgba(17,28,22,0.08);transform:rotate(-2deg);margin-top:8px">
    <div style="font-family:'IBM Plex Mono';font-size:13px;letter-spacing:0.16em;color:{MUT}">PRESS RELEASE</div>
    <div style="margin-top:12px;font-family:'Newsreader',serif;font-size:31px;line-height:1.1">Company announces <span style="background:rgba(28,116,224,0.18);padding:0 4px">positive</span> Phase 2 results</div>
    {pr_lines}
  </div>
  <div><div style="font-family:'IBM Plex Mono';font-size:16px;letter-spacing:0.14em;color:{MUT};margin-bottom:6px">5 QUESTIONS BEFORE YOU BELIEVE "POSITIVE"</div>{pinh}</div>
</div>
{footer('SOURCE: BIO, INFORMA, QLS 2021 · NOT INVESTMENT ADVICE',INK,MUT,'rgba(17,28,22,0.18)')}
</div>'''

# ================= 2. BIOMARKER: crowd -> filter -> gauges =================
def person(x,y,marked,fade=False):
    col=AZ if marked else ('#B7C1BB' if fade else '#8F9B94')
    return f'<g><circle cx="{x}" cy="{y}" r="11" fill="{col}"/><path d="M{x-17},{y+42} Q{x-17},{y+16} {x},{y+16} Q{x+17},{y+16} {x+17},{y+42} Z" fill="{col}"/></g>'
import random
random.seed(7)
marked=set(random.sample(range(32),9))
crowd=''
for i in range(32):
    c,r=i%8,i//8
    crowd+=person(30+c*46,20+r*62,i in marked)
crowdsvg=f'<svg width="380" height="270" viewBox="0 0 380 270" aria-hidden="true">{crowd}</svg>'
sel=''.join(person(30+i*46,20,True) for i in range(9))
selsvg=f'<svg width="430" height="70" viewBox="0 0 430 70" aria-hidden="true">{sel}</svg>'
def gauge(pct,label,color,strong):
    R=150; cx=170; cy=170; maxp=20.0
    def pt(p):
        a=math.pi*(1-p/maxp); return cx+R*math.cos(a), cy-R*math.sin(a)
    x0,y0=pt(0); x1,y1=pt(maxp); xp,yp=pt(pct)
    ticks=''.join(f'<line x1="{cx+(R+14)*math.cos(math.pi*(1-t/maxp))}" y1="{cy-(R+14)*math.sin(math.pi*(1-t/maxp))}" x2="{cx+(R+24)*math.cos(math.pi*(1-t/maxp))}" y2="{cy-(R+24)*math.sin(math.pi*(1-t/maxp))}" stroke="{MUT}" stroke-width="2"/>' for t in [0,5,10,15,20])
    lbls=''.join(f'<text x="{cx+(R+46)*math.cos(math.pi*(1-t/maxp))}" y="{cy-(R+46)*math.sin(math.pi*(1-t/maxp))+6}" font-family="IBM Plex Mono" font-size="15" fill="{MUT}" text-anchor="middle">{t}%</text>' for t in [0,10,20])
    return f'''<svg width="380" height="250" viewBox="-60 -50 460 250" aria-hidden="true">
<path d="M{x0},{y0} A{R},{R} 0 0 1 {x1},{y1}" fill="none" stroke="rgba(17,28,22,0.12)" stroke-width="30"/>
<path d="M{x0},{y0} A{R},{R} 0 0 1 {xp},{yp}" fill="none" stroke="{color}" stroke-width="30" />
{ticks}{lbls}
<text x="{cx}" y="{cy-10}" font-family="Newsreader" font-size="76" fill="{color}" text-anchor="middle">{pct}%</text>
</svg><div style="margin-top:-6px;text-align:center;font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{color if strong else MUT};font-weight:{600 if strong else 400}">{label}</div>'''
bio=f'''<div id="card" style="position:relative;width:1200px;height:1500px;background:{PAPER};color:{INK};overflow:hidden;padding:96px 104px 0">{NOISE}
{topbar('BY THE NUMBERS','FOR INVESTORS · THE SCIENCE SIDE','#1A66CC',INK,'rgba(17,28,22,0.2)')}
<div style="margin-top:44px;font-family:'Newsreader',serif;font-size:80px;line-height:1.0;letter-spacing:-0.02em">Pick the right patients.<br><span style="font-style:italic;color:{AZ}">Double the odds.</span></div>
<div style="margin-top:22px;font-size:26px;line-height:1.4;color:#38453E;max-width:930px">Drug programmes that used a biomarker to choose patients reached approval twice as often.</div>
<div style="position:relative;margin-top:50px;display:grid;grid-template-columns:380px 1fr;gap:40px;align-items:center">
  <div><div style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{MUT};margin-bottom:10px">EVERYONE WITH THE DISEASE</div>{crowdsvg}</div>
  <div style="position:relative;height:270px">
    <svg width="100%" height="270" viewBox="0 0 512 270" preserveAspectRatio="none" aria-hidden="true" style="position:absolute;inset:0"><path d="M0,10 L250,95 L250,175 L0,260 Z" fill="rgba(28,116,224,0.10)" stroke="{AZ}" stroke-width="2"/><rect x="250" y="95" width="262" height="80" fill="rgba(28,116,224,0.10)"/></svg>
    <div style="position:absolute;left:44px;top:118px;font-family:'IBM Plex Mono';font-size:16px;letter-spacing:0.14em;font-weight:600;color:{AZD}">BIOMARKER TEST</div>
    <div style="position:absolute;left:262px;top:104px">{selsvg.replace('width="430"','width="240"').replace('viewBox="0 0 430 70"','viewBox="0 0 430 70"')}</div>
    <div style="position:absolute;left:262px;top:186px;font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{AZD}">ONLY PATIENTS WITH<br>THE MARKER ENROL</div>
  </div>
</div>
<div style="position:relative;margin-top:44px;padding-top:20px;border-top:1px solid rgba(17,28,22,0.18);font-family:'IBM Plex Mono';font-size:16px;letter-spacing:0.14em;color:{MUT}">CHANCE OF APPROVAL FROM PHASE 1</div>
<div style="position:relative;margin-top:24px;display:grid;grid-template-columns:1fr 1fr;gap:40px;justify-items:center">
  <div>{gauge(7.9,'ALL DRUGS',INK,False)}</div>
  <div>{gauge(15.9,'WITH A SELECTION BIOMARKER',AZ,True)}</div>
</div>
<div style="position:relative;margin-top:40px;display:flex;align-items:center;gap:22px;background:#fff;border-radius:6px;padding:22px 28px;box-shadow:0 10px 30px rgba(17,28,22,0.10)"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.14em;font-weight:600;color:#fff;background:{AZ};padding:6px 10px;border-radius:3px;white-space:nowrap">ASK THE FOUNDER</span><span style="font-family:'Newsreader',serif;font-style:italic;font-size:36px;line-height:1.1">How do you pick your patients?</span></div>
{footer('SOURCE: BIO, INFORMA, QLS 2021 · NOT INVESTMENT ADVICE',INK,MUT,'rgba(17,28,22,0.18)')}
</div>'''

# ================= 3. PATENT CLOCK: dial =================
CX,CY,R=330,330,250; TOT=25.0
def ang(y): return -math.pi/2 + 2*math.pi*y/TOT
def P(y,r): a=ang(y); return CX+r*math.cos(a), CY+r*math.sin(a)
def arc(y0,y1,r):
    x0,yy0=P(y0,r); x1,yy1=P(y1,r); large=1 if (y1-y0)/TOT>0.5 else 0
    return f'M{x0:.1f},{yy0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{yy1:.1f}'
ticks=''
for y in range(0,26):
    r1=R+30; r2=R+(46 if y%5==0 else 38)
    x1,y1=P(y,r1); x2,y2=P(y,r2)
    ticks+=f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK2}" stroke-width="{2.5 if y%5==0 else 1.2}" opacity="{0.8 if y%5==0 else 0.4}"/>'
lab=''
for y in [0,5,10,15,20]:
    x,yy=P(y,R+74); lab+=f'<text x="{x:.1f}" y="{yy+8:.1f}" font-family="IBM Plex Mono" font-size="20" font-weight="600" fill="{INK2}" text-anchor="middle">{y}</text>'
sx,sy=P(22.5,R)
spc_label=f'<text x="{sx-6:.1f}" y="{sy+7:.1f}" font-family="IBM Plex Mono" font-size="19" font-weight="600" fill="#B23A17" text-anchor="middle">SPC</text>'
dial=f'''<svg width="660" height="660" viewBox="-40 -40 740 740" aria-hidden="true">
<defs><pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="{INK2}" stroke-width="2.4" opacity="0.45"/></pattern></defs>
<circle cx="{CX}" cy="{CY}" r="{R+30}" fill="#fff" opacity="0.55"/>
<path d="{arc(0,11,R)}" fill="none" stroke="url(#hatch)" stroke-width="56"/>
<path d="{arc(0,11,R)}" fill="none" stroke="{INK2}" stroke-width="1" opacity="0.3"/>
<path d="{arc(11,20,R)}" fill="none" stroke="{OR}" stroke-width="56"/>
<path d="{arc(20,25,R)}" fill="none" stroke="{OR}" stroke-width="56" opacity="0.28"/>
<path d="{arc(20,25,R)}" fill="none" stroke="{OR}" stroke-width="2" stroke-dasharray="6 6" transform="translate(0,0)"/>
{ticks}{lab}
{spc_label}
</svg>'''
def callout(top,left,title,body,color,w=300):
    return f'''<div style="position:absolute;top:{top}px;left:{left}px;width:{w}px"><div style="height:3px;width:44px;background:{color};margin-bottom:12px"></div><div style="font-family:'IBM Plex Mono';font-size:16px;letter-spacing:0.12em;font-weight:600;color:{color}">{title}</div><div style="margin-top:6px;font-size:22px;line-height:1.3;color:#3a3630">{body}</div></div>'''
patent=f'''<div id="card" style="position:relative;width:1200px;height:1500px;background:{WARM};color:{INK2};overflow:hidden;padding:96px 104px 0">{NOISE}
{topbar('THE TAKE','FOR SCIENTISTS · THE BUSINESS SIDE','#C93D1A',INK2,'rgba(26,22,19,0.2)')}
<div style="margin-top:44px;font-family:'Newsreader',serif;font-size:60px;line-height:1.04;letter-spacing:-0.02em">Your patent clock starts the day you file.<br><span style="font-style:italic;color:{OR}">Your first sale comes a decade later.</span></div>
<div style="position:relative;margin-top:30px;height:700px">
  <div style="position:absolute;left:-30px;top:10px">{dial}</div>
  {callout(30,700,'YEAR 0 · YOU FILE','The clock starts. Lab work, trials and approval all run on it.',INK2)}
  {callout(250,700,'ABOUT 10 YEARS · NO SALES','First human trial to approval took 10.5 years on average, 2011 to 2020.',INK2)}
  {callout(470,700,'YEAR 20 · PATENT ENDS','What is left after approval is your selling window.',ORD)}
  <div style="position:absolute;left:170px;top:268px;width:260px;text-align:center"><div style="font-family:'Newsreader',serif;font-size:96px;line-height:1;color:{OR}">~9</div><div style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;color:{MUT2};margin-top:6px">YEARS LEFT TO SELL</div></div>
</div>
<div style="position:relative;margin-top:10px;display:flex;align-items:center;gap:22px;border:2px dashed {OR};border-radius:6px;padding:20px 26px"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.14em;font-weight:600;color:#fff;background:#C93D1A;padding:6px 10px;border-radius:3px;white-space:nowrap">EUROPE'S FIX</span><span style="font-size:24px;line-height:1.3">A supplementary protection certificate adds up to 5 years, capped at 15 years after approval.</span></div>
{footer('ILLUSTRATIVE · EPC ART. 63 · EU REG. 469/2009 · NOT LEGAL ADVICE',INK2,MUT2,'rgba(26,22,19,0.18)')}
</div>'''
for name,html in [('trial',trial),('bio',bio),('patent',patent)]:
    open(f'{name}-render.html','w').write(head+html+'\n</body></html>')
    open(f'{name}.card.html','w').write(html)
