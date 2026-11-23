import math
exec(open('/home/claude/posts/d23/common.py').read())
HATCH='repeating-linear-gradient(-45deg,rgba(26,22,19,0.55) 0 2px,transparent 2px 8px)'
HATCHS='repeating-linear-gradient(-45deg,rgba(17,28,22,0.5) 0 2px,transparent 2px 8px)'
cards={}

# ---------------- 1. CAR-T price (business) ----------------
def pbar(lbl,val,txt,style,col,strike=False):
    w=val/1290000*100
    s=f'<span style="position:absolute;left:-6px;right:-6px;top:50%;height:3px;background:{INK2};transform:rotate(-1.5deg)"></span>' if strike else ''
    return f'''<div style="display:grid;grid-template-columns:300px 1fr;gap:22px;align-items:center">
<div>{mono(lbl,15,MUT2,600)}<div style="font-family:'Newsreader',serif;font-size:44px;line-height:1.05;color:{col};margin-top:4px">{txt}</div></div>
<div style="position:relative;height:44px;background:rgba(26,22,19,0.06);border-radius:6px"><div style="position:absolute;left:0;top:0;bottom:0;width:{w:.1f}%;border-radius:6px;{style}"></div>{s}</div></div>'''
def dots(n,col,per_row,size=14,gap=6,hollow=False):
    st=f'border:2px solid {col}' if hollow else f'background:{col}'
    return f'<div style="display:grid;grid-template-columns:repeat({per_row},{size}px);gap:{gap}px">'+''.join(f'<span style="width:{size}px;height:{size}px;border-radius:50%;{st}"></span>' for _ in range(n))+'</div>'
c1=f'''
{H('China cut a CAR-T price by 78%.','Below what a dose cost to make.',OR,74)}
<div style="display:flex;flex-direction:column;gap:26px">
{pbar('LAUNCH PRICE',1290000,'¥1.29M',f'background:{HATCH};box-shadow:inset 0 0 0 1.5px rgba(26,22,19,0.5)',INK2,True)}
{pbar('COST TO MAKE ONE DOSE, 2025',550000,'¥550,000',f'background:#fff;box-shadow:inset 0 0 0 2.5px {INK2}',INK2)}
{pbar('NEW REIMBURSED PRICE',288600,'¥288,600',f'background:{OR}',OR)}
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:stretch">
<div style="background:#fff;border-radius:8px;padding:26px 28px;box-shadow:0 12px 32px rgba(26,22,19,0.10)">
{mono('PATIENTS TREATED SO FAR',15,MUT2,600)}
<div style="font-family:'Newsreader',serif;font-size:58px;line-height:1;margin-top:10px">1,200</div>
<div style="font-size:20px;color:{MUT2};margin:6px 0 18px">in six years since launch</div>
{dots(12,INK2,16)}
<div style="margin-top:40px;padding-top:16px;border-top:1px solid rgba(26,22,19,0.15)">{mono('AVERAGE PER YEAR',15,MUT2,600)}<div style="font-family:'Newsreader',serif;font-size:44px;line-height:1;margin-top:8px">~200</div>{dots(2,INK2,16)}</div>
</div>
<div style="background:#fff;border-radius:8px;padding:26px 28px;box-shadow:0 12px 32px rgba(26,22,19,0.10)">
{mono('EXTRA PATIENTS EXPECTED, PER YEAR',15,ORD,600)}
<div style="font-family:'Newsreader',serif;font-size:58px;line-height:1;margin-top:10px;color:{OR}">~11,000</div>
<div style="font-size:20px;color:{MUT2};margin:6px 0 18px">once covered, says the CEO</div>
{dots(110,OR,16)}
</div>
</div>
<div style="display:grid;grid-template-columns:1fr 430px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#3a332c"><b style="font-weight:600">The trade.</b> JW Therapeutics accepts a price below last year's cost to reach far more patients, then plans to make its own viral vectors to bring the cost down.</div>
{note('THE LESSON','Model your cost per dose at the price a <span style="color:#E0451F;font-style:italic">payer will pay.</span>',-2,MUT2)}
</div>'''
cards['2026-11-23-cart-price']=bcard('CELL THERAPY PRICING',c1,'SOURCES: YICAI, 36KR, NOV 2026 · 1 DOT = 100 PATIENTS')

# ---------------- 2. patent cliff (science) ----------------
LOE=[('Eliquis',2026.85,14.3,0),('Prevnar 13',2026.95,6.4,1),('Gardasil 9',2028.45,6.8,2),('Jardiance',2028.6,11.8,1),('Keytruda',2028.95,32.6,0),('Ocrevus',2029.2,9.9,2),('Darzalex',2029.4,17.8,1),('Cosentyx',2029.95,8.3,2),('Vabysmo',2030.2,8.9,0)]
W,Hh=992,650; x0,x1=40,950; base=560
def X(y): return x0+(y-2026)/(2030.5-2026)*(x1-x0)
svg=f'<svg width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" aria-hidden="true">'
# cliff ground: plateau then drop
svg+=f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="{INK}" stroke-width="2"/>'
for yr in range(2026,2031):
    svg+=f'<line x1="{X(yr):.0f}" y1="{base}" x2="{X(yr):.0f}" y2="{base+12}" stroke="{INK}" stroke-width="2"/><text x="{X(yr):.0f}" y="{base+44}" text-anchor="middle" font-family="IBM Plex Mono" font-size="20" fill="{INK}">{yr}</text>'
lvl=[90,200,330]
for n,y,s,l in LOE:
    r=math.sqrt(s)*11.5
    cx=X(y); cy=base-r-[6,190,370][l]
    col=AZ if n=='Keytruda' else INK
    fill=AZ if n=='Keytruda' else 'none'
    svg+=f'<line x1="{cx:.0f}" y1="{cy+r:.0f}" x2="{cx:.0f}" y2="{base}" stroke="{col}" stroke-width="1.5" stroke-dasharray="3 4" opacity="0.6"/>'
    if n=='Keytruda':
        svg+=f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="{AZ}"/>'
        svg+=f'<text x="{cx:.0f}" y="{cy-6:.0f}" text-anchor="middle" font-family="Newsreader" font-size="34" fill="#fff">$32.6B</text><text x="{cx:.0f}" y="{cy+26:.0f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="17" font-weight="600" letter-spacing="2" fill="#fff">KEYTRUDA</text>'
    else:
        svg+=f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
        svg+=f'<text x="{cx:.0f}" y="{cy-r-26:.0f}" text-anchor="middle" font-family="IBM Plex Mono" font-size="16" font-weight="600" letter-spacing="1.5" fill="{INK}">{n.upper()}</text><text x="{cx:.0f}" y="{cy-r-6:.0f}" text-anchor="middle" font-family="Newsreader" font-size="22" fill="{INK}">${s}B</text>'
svg+='</svg>'
c2=f'''
{H('$300 billion in drug sales','loses protection by 2030.',AZ,82)}
<div>
<div style="display:flex;justify-content:space-between;align-items:baseline">{mono('BIGGEST LOSSES OF EXCLUSIVITY, BY DATE',15,MUT,600)}{mono('CIRCLE = SALES IN THE YEAR BEFORE',15,MUT)}</div>
<div style="margin-top:8px">{svg}</div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 400px;gap:24px;align-items:center">
<div style="background:#fff;border-radius:8px;padding:24px 24px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">{mono('AT RISK',15,MUT,600)}<div style="font-family:'Newsreader',serif;font-size:52px;line-height:1;margin-top:10px;white-space:nowrap">~1 in 6</div><div style="font-size:19px;color:{MUT};margin-top:8px;line-height:1.3">dollars of industry sales, 2025 to 2030</div></div>
<div style="background:#fff;border-radius:8px;padding:24px 24px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">{mono('TO BUILD A NEW ONE',15,MUT,600)}<div style="font-family:'Newsreader',serif;font-size:52px;line-height:1;margin-top:10px;white-space:nowrap">~10.5 yrs</div><div style="font-size:19px;color:{MUT};margin-top:8px;line-height:1.3">on average, from Phase 1 to approval</div></div>
{note('SO PHARMA DOES THIS','It buys what it can\'t build in time. <span style="color:#1C74E0;font-style:italic">Know who needs your asset.</span>',2,MUT)}
</div>'''
cards['2026-11-24-patent-cliff']=scard('THE PATENT CLIFF',c2,'SOURCES: EVALUATE 2025 · BIO, INFORMA, QLS 2021')

# ---------------- 3. EIC (business) ----------------
def funnel_row(lbl,n,txt,col,maxn=923):
    w=n/maxn*100
    return f'''<div style="display:grid;grid-template-columns:250px 1fr 120px;gap:20px;align-items:center"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;font-weight:600;color:{MUT2}">{lbl}</span><span style="position:relative;height:56px;background:rgba(26,22,19,0.06);border-radius:5px"><span style="position:absolute;left:0;top:0;bottom:0;width:{max(w,1.2):.1f}%;background:{col};border-radius:5px"></span></span><span style="font-family:'Newsreader',serif;font-size:52px;line-height:1;color:{col if col!='#fff' else INK2}">{txt}</span></div>'''
c3=f'''
{H('Up to €2.5M you never pay back.','And it is the smaller half.',OR,72)}
<div style="background:#fff;border-radius:8px;padding:28px 30px 30px;box-shadow:0 12px 32px rgba(26,22,19,0.10)">
<div style="display:flex;justify-content:space-between;align-items:baseline">{mono('EIC ACCELERATOR, MAXIMUM PER COMPANY',15,MUT2,600)}{mono('€ MILLION',15,MUT2)}</div>
<div style="display:flex;height:120px;margin-top:18px;border-radius:6px;overflow:hidden">
<div style="width:20%;background:{OR};color:#fff;padding:14px 16px"><div style="font-family:'Newsreader',serif;font-size:40px;line-height:1">2.5</div><div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.12em;font-weight:600;margin-top:6px">GRANT</div></div>
<div style="width:80%;background:{HATCH};box-shadow:inset 0 0 0 2px rgba(26,22,19,0.55);padding:14px 18px;position:relative"><div style="background:#fff;display:inline-block;padding:8px 14px 10px;border-radius:4px"><div style="font-family:'Newsreader',serif;font-size:40px;line-height:1">0.5 to 10</div><div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.12em;font-weight:600;margin-top:6px">EQUITY, EIC FUND</div></div></div>
</div>
<div style="margin-top:14px;font-size:20px;color:{MUT2}">85% of the 61 companies picked in February 2026 got both.</div>
</div>
<div style="display:flex;flex-direction:column;gap:18px">
<div>{mono('ONE CUT-OFF, OCTOBER 2025',15,MUT2,600)}</div>
{funnel_row('FULL APPLICATIONS',923,'923',INK2)}
{funnel_row('REACHED INTERVIEW',121,'121',INK2)}
{funnel_row('FUNDED',61,'61',OR)}
</div>
<div style="display:grid;grid-template-columns:1fr 440px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#3a332c"><b style="font-weight:600">Roughly 1 in 15</b> full applications gets funded. At the final interview it is about 1 in 2, in front of a jury of investors and entrepreneurs.</div>
{note('HOW TO WRITE IT','Like an investment memo, <span style="color:#E0451F;font-style:italic">not a research grant.</span>',-2,MUT2)}
</div>'''
cards['2026-11-25-eic-accelerator']=bcard('EU FUNDING',c3,'SOURCES: EIC, FEB 2026 · EUACC CUT-OFF DATA')

# ---------------- 4. China licensing (science) ----------------
def vbar(yr,p,col,h=500):
    bh=p/35*h
    return f'''<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:{h+90}px;gap:10px"><div style="font-family:'Newsreader',serif;font-size:52px;line-height:1;color:{col}">{p}%</div><div style="width:150px;height:{bh:.0f}px;background:{col if col==AZ else 'transparent'};{'' if col==AZ else 'background:'+HATCHS+';box-shadow:inset 0 0 0 2px rgba(17,28,22,0.5);'}border-radius:6px 6px 0 0"></div><div style="font-family:'IBM Plex Mono';font-size:18px;letter-spacing:0.1em;font-weight:600">{yr}</div></div>'''
def donut(p,size,col,label):
    r=size/2-14; C=2*math.pi*r
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true"><circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="rgba(17,28,22,0.1)" stroke-width="24"/><circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{col}" stroke-width="24" stroke-dasharray="{C*p/100:.1f} {C:.1f}" transform="rotate(-90 {size/2} {size/2})"/><text x="{size/2}" y="{size/2+16}" text-anchor="middle" font-family="Newsreader" font-size="{int(size/4.2)}" fill="{col}">{label}</text></svg>'''
c4=f'''
{H('Almost 1 in 3 licensing deals','is now for a drug from China.',AZ,82)}
<div style="display:grid;grid-template-columns:1fr 360px;gap:40px;align-items:end">
<div>
{mono('CHINA\'S SHARE OF GLOBAL LICENSING DEALS',15,MUT,600)}
<div style="display:flex;gap:36px;align-items:flex-end;margin-top:14px;border-bottom:2px solid {INK};padding-bottom:0">
{vbar('2020',5,INK)}{vbar('2024',21,INK)}{vbar('H1 2025',32,AZ)}
</div>
</div>
<div style="background:#fff;border-radius:8px;padding:26px 26px 28px;box-shadow:0 12px 32px rgba(17,28,22,0.10);text-align:center">
{mono('NEW MOLECULES ENTERING HUMAN TRIALS, H1 2025',14,MUT,600)}
<div style="margin-top:18px;display:flex;justify-content:center">{donut(46,270,AZ,'46%')}</div>
<div style="font-size:20px;line-height:1.3;color:{MUT};margin-top:8px">came from Chinese companies, up from <b style="color:{INK};font-weight:600">about 17%</b> a decade ago</div>
</div>
</div>
<div style="display:grid;grid-template-columns:1fr 440px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#2A3530"><b style="font-weight:600">Why.</b> Faster, cheaper trials get Chinese biotechs to human data sooner, and human data is what pharma pays most for.</div>
{note('ASK EVERY BIOTECH YOU BACK','Which Chinese molecule is closest, and <span style="color:#1C74E0;font-style:italic">how far ahead is it?</span>',2,MUT)}
</div>'''
cards['2026-11-26-china-licensing']=scard('WHERE PHARMA SHOPS',c4,'SOURCES: JEFFERIES VIA BIOWORLD · GOLDMAN SACHS 2025')

# ---------------- 5. EU HTA (business) ----------------
steps=[('JAN 2025','Cancer drugs and advanced therapies','10 assessments in year one'),('2026','About 50 assessments planned','High risk devices join'),('JAN 2028','Orphan drugs','For rare diseases'),('2030','Every new medicine','All newly approved drugs')]
st=''
for i,(d,t,s) in enumerate(steps):
    top=(3-i)*70
    hl=i==3
    st+=f'''<div style="margin-top:{top}px;background:{OR if hl else '#fff'};color:{'#fff' if hl else INK2};border-radius:8px;padding:20px 20px 22px;box-shadow:0 12px 32px rgba(26,22,19,0.10)"><div style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;font-weight:600;{'' if hl else 'color:'+ORD}">{d}</div><div style="font-family:'Newsreader',serif;font-size:31px;line-height:1.08;margin-top:8px">{t}</div><div style="font-size:18px;margin-top:8px;{'opacity:0.9' if hl else 'color:'+MUT2}">{s}</div></div>'''
def pico(l,w,d):
    return f'''<div style="border:2px solid {INK2};border-radius:8px;padding:16px 16px 18px;background:#fff"><div style="font-family:'Newsreader',serif;font-size:54px;line-height:0.9;color:{OR}">{l}</div><div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.12em;font-weight:600;margin-top:8px">{w}</div><div style="font-size:17px;line-height:1.3;color:{MUT2};margin-top:6px">{d}</div></div>'''
c5=f'''
{H('One EU check on your drug.','Soon for every new medicine.',OR,80)}
<div>{mono('JOINT CLINICAL ASSESSMENT, EU HTA REGULATION',15,MUT2,600)}<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;align-items:start;margin-top:14px">{st}</div></div>
<div>
<div style="display:flex;justify-content:space-between;align-items:baseline">{mono('WHAT THE ASSESSORS ASK: PICO',15,MUT2,600)}{mono('90 DAYS FROM FINAL PICO TO DOSSIER',15,ORD,600)}</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:14px">
{pico('P','POPULATION','Which patients?')}{pico('I','INTERVENTION','Your drug, how used')}{pico('C','COMPARATOR','Versus what? Can be several')}{pico('O','OUTCOMES','Which results count')}
</div></div>
<div style="display:grid;grid-template-columns:1fr 450px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#3a332c"><b style="font-weight:600">Early red flags:</b> single blinded trials, and trials run mostly outside Europe, where patients and standard care differ.</div>
{note('BEFORE PHASE 3','Pick your comparator and trial sites <span style="color:#E0451F;font-style:italic">with the EU assessment in mind.</span>',-2,MUT2)}
</div>'''
cards['2026-11-27-eu-hta']=bcard('EU MARKET ACCESS',c5,'SOURCES: IQWIG · ICON, MAR 2026 · REGULATION (EU) 2021/2282')

# ---------------- 6. satri-cel (science) ----------------
def tcell(x,y,col):
    s=f'<circle cx="{x}" cy="{y}" r="44" fill="{col}"/>'
    for a in (-35,0,35):
        ax=x+44*math.cos(math.radians(a)); ay=y+44*math.sin(math.radians(a))
        bx=x+70*math.cos(math.radians(a)); by=y+70*math.sin(math.radians(a))
        s+=f'<line x1="{ax:.0f}" y1="{ay:.0f}" x2="{bx:.0f}" y2="{by:.0f}" stroke="{col}" stroke-width="6"/>'
        for d in (-1,1):
            cx2=bx+14*math.cos(math.radians(a+d*40)); cy2=by+14*math.sin(math.radians(a+d*40))
            s+=f'<line x1="{bx:.0f}" y1="{by:.0f}" x2="{cx2:.0f}" y2="{cy2:.0f}" stroke="{col}" stroke-width="6" stroke-linecap="round"/>'
    s+=f'<text x="{x}" y="{y+7}" text-anchor="middle" font-family="IBM Plex Mono" font-size="17" font-weight="600" fill="#fff">CAR-T</text>'
    return s
def target_cells(x,y,n,col,mark,lbl):
    s=''
    for i in range(n):
        cx=x+(i%3)*58; cy=y+(i//3)*58
        s+=f'<circle cx="{cx}" cy="{cy}" r="24" fill="{col}" opacity="0.9"/>'
        if mark: s+=f'<rect x="{cx-24-6}" y="{cy-5}" width="10" height="10" fill="{AZ}" transform="rotate(45 {cx-24} {cy})"/>'
    s+=f'<text x="{x+58}" y="{y+(math.ceil(n/3))*58+6}" text-anchor="middle" font-family="IBM Plex Mono" font-size="15" font-weight="600" letter-spacing="1.5" fill="{INK}">{lbl}</text>'
    return s
def chip(lbl,on,tag=''):
    bg=AZ if on else 'transparent'; bd='none' if on else '2px dashed rgba(17,28,22,0.3)'
    fg='#fff' if on else MUT
    t=f'<div style="font-family:IBM Plex Mono;font-size:13px;letter-spacing:0.08em;color:{AZD};margin-top:6px;font-weight:600;height:16px">{tag}</div>'
    return f'''<div style="display:flex;flex-direction:column;align-items:center;width:130px"><div style="width:118px;height:118px;border-radius:50%;background:{bg};border:{bd};display:flex;align-items:center;justify-content:center;color:{fg};font-family:'IBM Plex Mono';font-size:28px;font-weight:600">{'●' if on else ''}</div><div style="font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.08em;font-weight:600;margin-top:10px;text-align:center;line-height:1.3;color:{INK if on else MUT}">{lbl}</div>{t}</div>'''
def panel(title,target,chips,verdict):
    return f'''<div style="background:#fff;border-radius:8px;padding:26px 28px 28px;box-shadow:0 12px 32px rgba(17,28,22,0.10);min-width:0">
{mono(title,15,AZD,600)}
<div style="font-family:'Newsreader',serif;font-size:40px;line-height:1.05;margin-top:8px">Target: <span style="font-style:italic;color:{AZ}">{target}</span></div>
<div style="margin-top:8px;font-family:'IBM Plex Mono';font-size:14px;letter-spacing:0.12em;color:{MUT}">WHERE THE CAR-T WILL FIND IT</div>
<div style="display:flex;justify-content:space-between;margin-top:16px">{chips}</div>
<div style="margin-top:16px;padding-top:14px;border-top:1px solid rgba(17,28,22,0.15);font-size:20px;line-height:1.35;color:#2A3530">{verdict}</div>
</div>'''
c6=f'''
{H('The first solid tumour CAR-T','was approved in China.',AZ,76)}
<div style="display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:26px">
{panel('BLOOD CANCERS','CD19',chip('CANCER<br>CELLS',True)+chip('NORMAL<br>B CELLS',True,'EXPENDABLE')+chip('OTHER<br>ORGANS',False),'Patients can live without B cells, so hitting them too is acceptable.')}
{panel('GASTRIC CANCER · SATRI-CEL','Claudin18.2',chip('CANCER<br>CELLS',True)+chip('STOMACH<br>LINING',True,'ONLY HERE')+chip('OTHER<br>ORGANS',False),'High in gastric cancer, in healthy tissue only the stomach lining. Solid tumours rarely offer this.')}
</div>
<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px">
<div style="background:#fff;border-radius:8px;padding:22px 26px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">{mono('EXTRA HURDLE 1',14,MUT,600)}<div style="font-family:'Newsreader',serif;font-size:32px;line-height:1.1;margin-top:8px">Get into the tumour</div><div style="font-size:19px;line-height:1.35;color:{MUT};margin-top:8px">Dense tissue around many solid tumours keeps T cells out.</div></div>
<div style="background:#fff;border-radius:8px;padding:22px 26px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">{mono('EXTRA HURDLE 2',14,MUT,600)}<div style="font-family:'Newsreader',serif;font-size:32px;line-height:1.1;margin-top:8px">Survive once inside</div><div style="font-size:19px;line-height:1.35;color:{MUT};margin-top:8px">The tumour sends signals that switch T cells off.</div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 450px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#2A3530"><b style="font-weight:600">Approved in June 2026</b> for advanced gastric cancer that progressed after at least two prior treatments.</div>
{note('WHEN YOU LOOK AT ONE','Start with the target. <span style="color:#1C74E0;font-style:italic">Where else in the body is it?</span>',2,MUT)}
</div>'''
cards['2026-11-28-solid-tumour-cart']=scard('CELL THERAPY',c6,'SOURCES: CARSGEN, ONCLIVE, CAIXIN · JUNE 2026 · SCHEMATIC')

# ---------------- 7. Lilly vs Merck (science) ----------------
def co(name,drug,sales,share,share_lbl,approved,clock,col):
    return f'''<div style="background:#fff;border-radius:8px;padding:26px 28px 28px;box-shadow:0 12px 32px rgba(17,28,22,0.10)">
<div style="display:flex;justify-content:space-between;align-items:baseline">{mono(name,17,col if col==AZ else INK,600)}{mono('2025',15,MUT)}</div>
<div style="font-family:'Newsreader',serif;font-size:36px;line-height:1.05;margin-top:6px;font-style:italic">{drug}</div>
<div style="display:flex;gap:22px;align-items:center;margin-top:14px">{donut(share,190,col,str(share)+'%')}<div><div style="font-family:'Newsreader',serif;font-size:50px;line-height:1">{sales}</div><div style="font-size:18px;color:{MUT};margin-top:6px;line-height:1.3">{share_lbl}</div></div></div>
<div style="margin-top:16px;padding-top:14px;border-top:1px solid rgba(17,28,22,0.15);display:flex;justify-content:space-between;font-size:19px"><span>First approved <b style="font-weight:600">{approved}</b></span><span style="color:{col if col==AZ else INK}">{clock}</span></div>
</div>'''
def race(lbl,yrs,txt,col):
    return f'''<div style="display:grid;grid-template-columns:190px 1fr 190px;gap:18px;align-items:center"><span style="font-family:'IBM Plex Mono';font-size:15px;letter-spacing:0.12em;font-weight:600">{lbl}</span><span style="position:relative;height:30px;background:rgba(17,28,22,0.07);border-radius:15px"><span style="position:absolute;left:0;top:0;bottom:0;width:{yrs/9.5*100:.1f}%;background:{col if col==AZ else 'transparent'};{'' if col==AZ else 'background:'+HATCHS+';box-shadow:inset 0 0 0 2px rgba(17,28,22,0.5);'}border-radius:15px"></span></span><span style="font-family:'Newsreader',serif;font-size:30px;color:{col if col==AZ else INK}">{txt}</span></div>'''
c7=f'''
{H('Two giants, one drug each.','Only one is short on time.',AZ,80)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px">
{co('ELI LILLY','Tirzepatide','$36.5B',56,'of Lilly\'s total revenue','2022','World\'s top seller',AZ)}
{co('MERCK','Keytruda','$31.7B',55,'of Merck\'s drug sales','2014','Main patent ends 2028',INK)}
</div>
<div style="display:flex;flex-direction:column;gap:16px">
{mono('YEARS FROM FIRST APPROVAL TO WORLD\'S BEST SELLER',15,MUT,600)}
{race('KEYTRUDA',9,'9 years',INK)}
{race('TIRZEPATIDE',3.6,'under 4 years',AZ)}
</div>
<div style="display:grid;grid-template-columns:1fr 450px;gap:34px;align-items:center">
<div style="font-size:24px;line-height:1.38;color:#2A3530"><b style="font-weight:600">Same dependence, different clock.</b> Tirzepatide passed Keytruda in 2025. Merck has to replace its top seller within a few years.</div>
{note('WHEN YOU VALUE PHARMA','Ask how many years of protection <span style="color:#1C74E0;font-style:italic">the top drug has left.</span>',2,MUT)}
</div>'''
cards['2026-11-29-one-drug-companies']=scard('PHARMA CONCENTRATION',c7,'SOURCES: 2025 RESULTS VIA FIERCE PHARMA, BIOPHARMA DIVE, STAT')

import sys
for k,v in cards.items():
    open(f'/home/claude/posts/d23/{k}.html','w').write(page(v))
print(list(cards))
