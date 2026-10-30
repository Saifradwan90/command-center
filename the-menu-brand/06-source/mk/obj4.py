from mock import *
from common import mh,LH,THH,MH
from obj1 import m_art
from obj2 import food,inner
from obj3 import qrsvg
def apron():
    o=shadow(130,300,100,10,.3)
    d='M92,48 L168,48 L180,118 Q214,132 224,180 L240,300 L20,300 L36,180 Q46,132 80,118Z'
    o+=f'<path d="M96,50 Q130,-6 164,50" fill="none" stroke="{AUB}" stroke-width="9"/><path d="M36,180 L10,222 M224,180 L250,222" stroke="{AUB}" stroke-width="7"/>'
    o+=face(d,AUB,'gSh')+logo('wm',IVORY,0,0,84,0,'translate(88 88)')
    o+=f'<rect x="86" y="214" width="88" height="56" rx="6" fill="#241019"/><rect x="86" y="214" width="88" height="56" rx="6" fill="url(#gSh)" opacity=".5"/>'+clipped(d,m_art(20,276,150,LIME)+m_art(120,276,150,LIME))
    return svgwrap(260,320,o)
def cap(c=LIME,ink=AUB):
    o=shadow(150,170,130,10,.3)
    d='M30,130 Q30,30 150,30 Q270,30 270,130Z'
    o+=face(d,c,'gShV')+f'<path d="M150,30 L150,130" stroke="#000" stroke-opacity=".12"/><path d="M90,38 Q100,90 96,130 M210,38 Q200,90 204,130" stroke="#000" stroke-opacity=".1" fill="none"/>'
    o+=face('M20,130 Q150,108 280,130 Q310,170 240,174 L60,174 Q-10,170 20,130Z',c,'gSh')
    o+=logo('mg',ink,0,0,64,0,'translate(118 66)')
    return svgwrap(300,200,o)
def tee(c=AUB,ink=IVORY):
    o=shadow(130,260,100,10,.3)
    d='M66,22 L106,10 Q130,40 154,10 L194,22 L248,72 L214,104 L192,82 L192,252 L68,252 L68,82 L46,104 L12,72Z'
    o+=face(d,c,'gSh')+logo('lk',ink,0,0,92,0,'translate(84 96)')
    return svgwrap(260,280,o)
def badge():
    o=shadow(70,120,50,8,.3)+f'<rect x="10" y="20" width="120" height="84" rx="10" fill="{AUB}"/><rect x="10" y="20" width="120" height="84" rx="10" fill="url(#gSh)"/>'+logo('wm',IVORY,0,0,50,0,'translate(20 28)')+f'<text x="20" y="84" font-family="DM Sans" font-weight="800" font-size="13" fill="{LIME}">SARA</text><text x="20" y="98" font-family="DM Sans" font-size="8" letter-spacing="2" fill="{IVORY}">TEAM MEMBER</text>'+logo('mg',LIME,0,0,26,0,'translate(98 78)')
    return svgwrap(140,140,o)
def neon():
    o=f'<rect width="640" height="360" fill="#17131a"/><rect y="0" width="640" height="360" fill="url(#gShV)" opacity=".4"/>'
    pm=parts_menu()
    o+=f'<g transform="translate(70 100) scale(.5)" fill="none" stroke="{LIME}" stroke-width="14" stroke-linejoin="round" filter="url(#fSh)" opacity=".9"><path d="{pm}"/></g>'
    o+=f'<g transform="translate(70 100) scale(.5)" fill="none" stroke="{LIME}" stroke-width="7" stroke-linejoin="round"><path d="{pm}"/></g><g transform="translate(70 100) scale(.5)" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="2" stroke-linejoin="round"><path d="{pm}"/></g>'
    o+=f'<text x="320" y="320" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="14" letter-spacing="8" fill="{LIME}" opacity=".7">EAT WELL. TASTE MORE.</text>'
    return svgwrap(640,360,o)
def parts_menu():
    from geom import parts;return parts['menu_only']
def window():
    o=f'<rect width="560" height="360" fill="#6f8d92"/><rect width="560" height="360" fill="url(#gClear)"/><rect x="0" y="0" width="560" height="360" fill="url(#gShV)"/>'
    o+=f'<path d="M0,220 L560,150" stroke="#fff" stroke-opacity=".18" stroke-width="40"/>'
    o+=logo('lk','#fff',0,0,300,0,'translate(130 70)')
    o+=f'<rect x="150" y="262" width="260" height="42" fill="{LIME}"/><text x="280" y="290" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" letter-spacing="4" fill="{AUB}">OPEN · 8AM — 11PM</text>'
    return svgwrap(560,360,o)
def floor():
    o=f'<rect width="560" height="300" fill="#cfc6b6"/>'+''.join(f'<path d="M{x},0 L{x},300" stroke="#8d7f68" stroke-opacity=".3"/>' for x in range(0,560,140))+''.join(f'<path d="M0,{y} L560,{y}" stroke="#8d7f68" stroke-opacity=".3"/>' for y in range(0,300,100))
    o+=f'<g transform="translate(280 160) scale(1,.45)"><circle r="120" fill="#000" opacity=".25" transform="translate(8 10)"/><circle r="120" fill="{LIME}"/><circle r="104" fill="none" stroke="{AUB}" stroke-width="3" stroke-dasharray="6 6"/></g>'
    o+=f'<g transform="translate(280 160) scale(1,.45)">{logo("mg",AUB,0,0,110,0,"translate(-55 -28)")}</g>'+f'<text x="280" y="228" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="12" letter-spacing="5" fill="{AUB}">ORDER HERE →</text>'
    return svgwrap(560,300,o)
def top_bowl(cx,cy,r,seed=3):
    o=f'<circle cx="{cx+6}" cy="{cy+10}" r="{r}" fill="#000" opacity=".28" filter="url(#fSh2)"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{LIME}"/><circle cx="{cx}" cy="{cy}" r="{r-8}" fill="#2a1420"/>'
    o+=food(seed,cx-r+10,cy-r+10,2*r-20,2*r-20)
    o+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gDome)"/><path d="M{cx-r*.7},{cy-r*.4} A{r*.78},{r*.78} 0 0 1 {cx-r*.1},{cy-r*.78}" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width="7" stroke-linecap="round"/>'
    return o
def top_cup(cx,cy,r,c=AUB):
    return f'<circle cx="{cx+5}" cy="{cy+9}" r="{r}" fill="#000" opacity=".28" filter="url(#fSh2)"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/><circle cx="{cx}" cy="{cy}" r="{r*.82}" fill="none" stroke="#fff" stroke-opacity=".15" stroke-width="3"/><ellipse cx="{cx+r*.35}" cy="{cy-r*.35}" rx="{r*.17}" ry="{r*.07}" fill="#000" opacity=".55" transform="rotate(-40 {cx+r*.35} {cy-r*.35})"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gTop)" opacity=".5"/>'+logo('mg',LIME,0,0,r*.7,0,f'translate({cx-r*.35} {cy-r*.1})')
def flatlay():
    W,H=1200,720
    o=f'<rect width="{W}" height="{H}" fill="{LIME}"/>'
    # tray
    o+=f'<rect x="150" y="60" width="900" height="600" rx="26" fill="#000" opacity=".25" filter="url(#fSh)" transform="translate(10 16)"/><rect x="150" y="60" width="900" height="600" rx="26" fill="{AUB}"/><rect x="150" y="60" width="900" height="600" rx="26" fill="url(#gShV)"/>'
    # liner
    o+=f'<g transform="rotate(-4 600 360)"><clipPath id="lc"><rect x="200" y="100" width="800" height="520"/></clipPath><rect x="200" y="100" width="800" height="520" fill="{IVORY}"/><g clip-path="url(#lc)">'+mpat(196,104,46,AUB,8,9,92,64,46)+f'</g></g>'
    o+=f'<clipPath id="cl"><rect x="200" y="100" width="800" height="520"/></clipPath>'
    o+=f'<rect x="560" y="270" width="270" height="150" fill="{IVORY}" transform="rotate(-4 700 340)"/>'+logo('lk',AUB,0,0,215,0,'translate(588 292) rotate(-4)')
    # items
    o+=top_bowl(380,380,170,3)+top_cup(790,250,70,AUB)+top_cup(910,430,62,LIME).replace(LIME+'"/><circle',LIME+'"/><circle',1)
    o+=f'<g transform="translate(700 470) rotate(-12)"><rect width="190" height="90" rx="10" fill="#000" opacity=".25" filter="url(#fSh2)" transform="translate(5 8)"/><rect width="190" height="90" rx="10" fill="{IVORY}"/><rect x="62" width="66" height="90" fill="{LIME}"/>{logo("mg",AUB,0,0,40,0,"translate(75 34)")}</g>'
    o+=f'<g transform="translate(270 150) rotate(-20)"><rect width="26" height="120" rx="6" fill="#000" opacity=".25" filter="url(#fSh2)" transform="translate(4 6)"/><rect width="26" height="120" rx="6" fill="#D8B988"/></g><g transform="translate(300 150) rotate(-20)"><rect width="26" height="120" rx="6" fill="#D8B988"/></g>'
    o+=f'<g transform="translate(930 560) rotate(8)"><circle r="40" fill="#000" opacity=".25" filter="url(#fSh2)" transform="translate(4 8)"/><circle r="40" fill="{AUB}"/><circle r="40" fill="url(#gTop)" opacity=".6"/>{logo("mg",LIME,0,0,36,0,"translate(-18 -10)")}</g>'
    return svgwrap(W,H,o)
if __name__=='__main__':
    items=[apron(),cap(),tee(),tee(LIME,AUB),badge(),neon(),window(),floor(),flatlay()]
    html=f'<body style="margin:0;background:#E9E1D0">{SYM}{DEFS}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:20px;width:1700px">'+''.join(f'<div>{i}</div>' for i in items)+'</div></body>'
    open('mk/o4.html','w').write(html)
