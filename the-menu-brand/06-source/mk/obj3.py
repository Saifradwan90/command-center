from mock import *
from common import mh,LH,THH,MH
from obj1 import m_art
from obj2 import food,inner
def qrsvg(x,y,s,fg=AUB,bg='#fff',seed=3):
    import random;random.seed(seed);n=17;c=s/n;o=f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{bg}"/>'
    def fin(a,b):return f'<rect x="{x+a*c}" y="{y+b*c}" width="{7*c}" height="{7*c}" fill="{fg}"/><rect x="{x+(a+1)*c}" y="{y+(b+1)*c}" width="{5*c}" height="{5*c}" fill="{bg}"/><rect x="{x+(a+2)*c}" y="{y+(b+2)*c}" width="{3*c}" height="{3*c}" fill="{fg}"/>'
    for i in range(n):
        for j in range(n):
            if (i<8 and j<8) or (i>n-9 and j<8) or (i<8 and j>n-9):continue
            if random.random()<.5:o+=f'<rect x="{x+i*c:.1f}" y="{y+j*c:.1f}" width="{c:.1f}" height="{c:.1f}" fill="{fg}"/>'
    return o+fin(0,0)+fin(n-7,0)+fin(0,n-7)
def wrap_sandwich(paper=LIME,pat=AUB):
    o=shadow(270,258,200,16,.38)
    g=f'<g transform="rotate(-9 270 160)">'
    body='M70,120 Q70,90 100,90 L440,90 Q480,90 480,130 L480,190 Q480,230 440,230 L100,230 Q70,230 70,200Z'
    # tortilla / filling end
    g+=f'<path d="{body}" fill="#E8D3A8"/><path d="{body}" fill="url(#gShV)"/>'
    g+=f'<ellipse cx="82" cy="160" rx="22" ry="68" fill="#F0DDB6"/><ellipse cx="82" cy="160" rx="16" ry="56" fill="{LIME}"/><circle cx="80" cy="140" r="10" fill="{APR}"/><circle cx="84" cy="172" r="9" fill="{AUB}"/><circle cx="78" cy="196" r="8" fill="{LIME}" opacity=".8"/>'
    paperp='M180,90 L440,90 Q480,90 480,130 L480,190 Q480,230 440,230 L180,230 L206,160Z'
    g+=f'<path d="{paperp}" fill="{paper}"/>'
    g+=clipped(paperp,m_art(205,172,60,pat)+m_art(255,172,60,pat)+m_art(305,172,60,pat)+m_art(355,172,60,pat)+m_art(405,172,60,pat)+m_art(230,206,60,pat)+m_art(280,206,60,pat)+m_art(330,206,60,pat)+m_art(380,206,60,pat)+logo('lk',pat,0,0,170,0,'translate(250 104)')+f'<rect x="200" y="226" width="300" height="6" fill="#000" opacity=".1"/>')
    g+=f'<path d="{paperp}" fill="url(#gShV)"/><path d="M180,90 L206,160 L180,230" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="2"/>'
    # twisted end
    g+=f'<path d="M480,130 L520,112 L508,160 L520,208 L480,190Z" fill="{paper}"/><path d="M480,130 L520,112 L508,160 L520,208 L480,190Z" fill="url(#gShR)"/><path d="M486,134 L512,120 M486,160 L508,160 M486,186 L512,200" stroke="#000" stroke-opacity=".25" stroke-width="2"/>'
    g+='</g>'
    return svgwrap(560,300,o+g)
def paper_sheet(rot=-6,pat=AUB,bg=IVORY,w=420,h=300,logo_on=True):
    o=shadow(w/2+10,h+20,w*.5,14,.3)
    g=f'<g transform="rotate({rot} {w/2} {h/2})"><rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>'
    g+=f'<g opacity=".95">'+mpat(-10,8,34,pat,12,14,34,22,17)+'</g>'
    if logo_on:g+=f'<rect x="{w/2-125}" y="{h/2-66}" width="250" height="132" fill="{bg}"/>'+logo('lk',AUB,0,0,190,0,f'translate({w/2-95} {h/2-34})')
    g+=f'<rect width="{w}" height="{h}" fill="url(#gShV)"/><path d="M{w},{h} L{w-56},{h} Q{w-20},{h-20} {w},{h-56}Z" fill="#000" opacity=".1"/></g>'
    return svgwrap(w+40,h+50,o+g)
def cutlery_set():
    o=shadow(250,230,220,14,.3)
    wood='#D8B988';wood2='#C29E69'
    def fork(x,y,rot):
        return f'<g transform="translate({x} {y}) rotate({rot})"><path d="M0,0 L6,0 L6,40 Q6,52 12,52 L12,0 L18,0 L18,52 Q24,52 24,40 L24,0 L30,0 L30,44 Q30,66 18,70 L18,170 Q18,176 15,176 Q12,176 12,170 L12,70 Q0,66 0,44Z" fill="{wood}"/><path d="M0,0 L30,0 L30,176 L0,176Z" fill="url(#gSh)" opacity=".4"/></g>'
    def knife(x,y,rot):return f'<g transform="translate({x} {y}) rotate({rot})"><path d="M0,0 Q34,0 34,40 L34,60 L18,60 L18,176 Q18,182 15,182 Q12,182 12,176 L12,60 L0,60Z" fill="{wood}"/><path d="M0,0 L34,0 L34,180 L0,180Z" fill="url(#gSh)" opacity=".4"/></g>'
    o+=fork(60,40,-10)+knife(130,36,-6)
    # sleeve with fork
    o+=f'<g transform="rotate(-8 330 150)"><path d="M250,120 L470,120 L470,196 L250,196Z" fill="{LIME}"/><path d="M250,120 L470,120 L470,196 L250,196Z" fill="url(#gShV)"/>'
    o+=clipped('M250,120 L470,120 L470,196 L250,196Z',logo('wm',AUB,0,0,96,0,'translate(262 138)')+m_art(380,150,110,AUB))+'</g>'
    o+=f'<g transform="translate(398 40) rotate(-8)"><path d="M0,0 L6,0 L6,30 Q6,40 12,40 L12,0 L18,0 L18,40 Q24,40 24,30 L24,0 L30,0 L30,34 Q30,52 18,56 L18,100 L12,100 L12,56 Q0,52 0,34Z" fill="{wood2}"/></g>'
    return svgwrap(520,270,o)
def napkin(c=IVORY):
    o=shadow(130,170,110,12,.3)
    o+=f'<g transform="rotate(-8 130 100)"><rect x="40" y="30" width="180" height="140" fill="{c}"/><rect x="40" y="30" width="180" height="140" fill="url(#gShV)"/><path d="M40,100 L220,100 M130,30 L130,170" stroke="#000" stroke-opacity=".08"/><rect x="104" y="30" width="52" height="140" fill="{LIME}"/><rect x="104" y="30" width="52" height="140" fill="url(#gSh)"/>{logo("mg",AUB,0,0,34,0,"translate(113 88)")}</g>'
    return svgwrap(260,200,o)
def stickers():
    o=f'<rect x="0" y="0" width="560" height="360" rx="10" fill="#fff"/><rect x="0" y="0" width="560" height="360" rx="10" fill="url(#gShV)"/>'
    st=''
    st+=f'<circle cx="90" cy="90" r="62" fill="{LIME}"/>'+logo('mg',AUB,0,0,70,0,'translate(55 72)')
    st+=f'<circle cx="230" cy="90" r="62" fill="{AUB}"/><circle cx="230" cy="90" r="50" fill="none" stroke="{LIME}" stroke-width="2" stroke-dasharray="4 4"/>'+f'<text x="230" y="86" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="13" letter-spacing="2" fill="{LIME}">SEALED</text><text x="230" y="104" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="13" letter-spacing="2" fill="{LIME}">FRESH</text>'
    st+=f'<rect x="320" y="30" width="210" height="120" rx="12" fill="{IVORY}"/>'+logo('wm',AUB,0,0,80,0,'translate(336 44)')+f'<text x="336" y="112" font-family="DM Sans" font-weight="700" font-size="10" letter-spacing="1" fill="{AUB}">ORDER #1042</text><text x="336" y="128" font-family="DM Sans" font-size="9" fill="{AUB}">CHARRED AUBERGINE BOWL · NO ONION</text>'+qrsvg(468,92,50,AUB,IVORY)
    st+=f'<rect x="30" y="180" width="500" height="44" rx="6" fill="{AUB}"/>'+''.join(f'<text x="{44+i*162}" y="208" font-family="DM Sans" font-weight="800" font-size="11" letter-spacing="3" fill="{LIME}" textLength="130">OPEN FOR FLAVOUR</text>' for i in range(3))
    st+=f'<path d="M30,330 L30,270 Q30,244 70,244 Q110,244 110,270 L110,330Z" fill="{LIME}"/>'+logo('mg',AUB,0,0,52,0,'translate(40 282)')
    st+=f'<rect x="130" y="246" width="190" height="84" rx="8" fill="#fff" stroke="{AUB}" stroke-width="2"/><text x="144" y="270" font-family="DM Sans" font-weight="800" font-size="12" fill="{AUB}">NUTRITION / PER BOWL</text><path d="M144,278 L306,278" stroke="{AUB}" stroke-width="2"/><text x="144" y="298" font-family="DM Sans" font-size="11" fill="{AUB}">480 kcal · 38 g protein</text><text x="144" y="316" font-family="DM Sans" font-size="11" fill="{AUB}">High-protein · Plant-aware</text>'
    st+=f'<rect x="340" y="246" width="190" height="84" rx="42" fill="{APR}"/><text x="435" y="294" text-anchor="middle" font-family="Fraunces" font-weight="600" font-size="26" fill="{AUB}">Taste more.</text>'
    # peel shadows
    o+=f'<g filter="url(#fSh2)" opacity=".0"></g>'+st
    return svgwrap(560,360,shadow(280,372,250,12,.3)+o)
def backpack():
    W,H,D=250,250,150;x0,y0=70,80
    def fa():return f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="{LIME}"/>'+logo('lk',AUB,0,0,200,0,f'translate({x0+25} {y0+70})')+f'<rect x="{x0}" y="{y0+H-34}" width="{W}" height="34" fill="{AUB}"/>'
    sa=lambda m:f'<g transform="{m}"><rect width="200" height="260" fill="{AUB}"/>{m_art(-60,150,260,LIME)}</g>'
    o=box3d(x0,y0,W,H,D,LIME,'#E6F26F','#2E1621',fa=fa(),sa=sa,ta=lambda m:f'<g transform="{m}"><rect width="300" height="200" fill="{LIME}"/><rect x="100" y="70" width="100" height="60" fill="{AUB}"/></g>')
    o+=f'<path d="M{x0+40},{y0} L{x0+40},{y0+H}" stroke="#111" stroke-width="12" opacity=".7"/><path d="M{x0+W-40},{y0} L{x0+W-40},{y0+H}" stroke="#111" stroke-width="12" opacity=".7"/>'
    return svgwrap(520,420,o)
def insulated_bag():
    W,H,D=330,190,160;x0,y0=70,140
    def fa():return f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="{AUB}"/>'+logo('lk',IVORY,0,0,170,0,f'translate({x0+W/2-85} {y0+30})')+f'<rect x="{x0}" y="{y0+H-20}" width="{W}" height="20" fill="{LIME}"/>'
    o=box3d(x0,y0,W,H,D,AUB,'#4B2B3E','#241019',fa=fa(),sa=lambda m:f'<g transform="{m}">{m_art(-20,60,200,LIME)}</g>',ta=lambda m:f'<g transform="{m}"><path d="M0,128 L330,128" stroke="{LIME}" stroke-width="5"/></g>')
    o+=f'<path d="M{x0+90},{y0-6} Q{x0+W/2},{y0-70} {x0+W-90},{y0-6}" fill="none" stroke="{LIME}" stroke-width="10" stroke-linecap="round"/>'
    return svgwrap(620,400,o)
def receipt(w=210,h=420):
    o=shadow(w/2+10,h+14,w*.5,10,.3)
    zig=''.join(f'L{w-i*14-7},{h+8} L{w-(i+1)*14},{h}' for i in range(int(w/14)))
    d=f'M0,0 L{w},0 L{w},{h} {zig} L0,{h}Z'
    o+=f'<path d="{d}" fill="#fbfaf6"/><path d="{d}" fill="url(#gSh)" opacity=".5"/>'
    o+=logo('wm',AUB,0,0,w*.5,0,f'translate({w*.25} 20)')
    t=lambda y,a,b,wgt=500:f'<text x="18" y="{y}" font-family="DM Sans" font-weight="{wgt}" font-size="10" fill="{AUB}">{a}</text><text x="{w-18}" y="{y}" text-anchor="end" font-family="DM Sans" font-weight="{wgt}" font-size="10" fill="{AUB}">{b}</text>'
    o+=f'<text x="{w/2}" y="86" text-anchor="middle" font-family="DM Sans" font-size="8" letter-spacing="2" fill="{AUB}">ORDER #1042 · 12:42</text><path d="M18,96 L{w-18},96" stroke="{AUB}" stroke-dasharray="3 3"/>'
    o+=t(116,'1 Charred Aubergine Bowl','42')+t(134,'1 Lime & Tahini Chicken','46')+t(152,'2 Cold-pressed Lime','24')+t(170,'1 Sauce · Tahini','4')
    o+=f'<path d="M18,184 L{w-18},184" stroke="{AUB}" stroke-dasharray="3 3"/>'+t(206,'TOTAL','116',800)
    o+=f'<rect x="18" y="226" width="{w-36}" height="44" fill="{LIME}"/><text x="{w/2}" y="253" text-anchor="middle" font-family="Fraunces" font-weight="600" font-size="16" fill="{AUB}">Eat well. Taste more.</text>'
    o+=qrsvg(w/2-38,288,76)+f'<text x="{w/2}" y="388" text-anchor="middle" font-family="DM Sans" font-size="8" letter-spacing="2" fill="{AUB}">SCAN · EARN A STAMP</text>'
    return svgwrap(w+20,h+30,o)
def pos():
    o=shadow(190,300,160,12,.3)
    o+=f'<path d="M150,250 L230,250 L246,300 L134,300Z" fill="#2b2a2e"/><rect x="20" y="20" width="340" height="236" rx="14" fill="#1a1a1d"/><rect x="32" y="32" width="316" height="212" rx="6" fill="{IVORY}"/>'
    o+=f'<rect x="32" y="32" width="316" height="34" fill="{AUB}"/>'+logo('wm',IVORY,0,0,60,0,'translate(42 38)')
    for i,(s,c) in enumerate([(3,LIME),(4,APR),(5,'#fff'),(6,LIME),(7,'#fff'),(9,APR)]):
        x=44+(i%3)*100;y=80+(i//3)*76
        o+=f'<rect x="{x}" y="{y}" width="92" height="68" rx="8" fill="#fff"/>'+f'<svg x="{x+26}" y="{y+6}" width="40" height="40" viewBox="0 0 400 400">{inner(A2.bowl(s,400,None,AUB,IVORY))}</svg>'+f'<text x="{x+46}" y="{y+60}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="8" fill="{AUB}">Bowl {i+1}</text>'
    o+=f'<rect x="248" y="226" width="92" height="12" rx="6" fill="{LIME}"/>'
    return svgwrap(380,320,o)
if __name__=='__main__':
    items=[wrap_sandwich(),paper_sheet(),cutlery_set(),napkin(),stickers(),backpack(),insulated_bag(),receipt(),pos()]
    html=f'<body style="margin:0;background:#E9E1D0">{SYM}{DEFS}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:20px;width:1700px">'+''.join(f'<div>{i}</div>' for i in items)+'</div></body>'
    open('mk/o3.html','w').write(html)
