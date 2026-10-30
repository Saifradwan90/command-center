from mock import *
from common import mh,LH
from obj1 import m_art
def inner(svgstr):return svgstr[svgstr.index('>')+1:-6]
def food(seed,x,y,w,h,rim=AUB,inn=IVORY,bg=None):
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 400 400" preserveAspectRatio="none">{inner(A2.bowl(seed,400,bg,rim,inn))}</svg>'
def hw(y,y0,h,wt,wb):return wt-(wt-wb)*(y-y0)/h
def bowl_paper(color=AUB,pat=LIME,ink=IVORY,seed=7,rimc=None):
    cx,yr=270,150;wt,wb=175,122;hgt=170;ry=52
    yb=yr+hgt;rimc=rimc or LIME
    body=f'M{cx-wt},{yr} L{cx-wb},{yb} A{wb},{ry*wb/wt:.1f} 0 0 0 {cx+wb},{yb} L{cx+wt},{yr} A{wt},{ry} 0 0 1 {cx-wt},{yr}Z'
    o=shadow(cx,yb+ry*.7+8,wt*.95,22,.4)
    o+=face(body,color,'gSh')
    # pattern + logo on body
    o+=clipped(body,m_art(cx-wt-20,yb-52,wt*1.0,pat)+m_art(cx+20,yb-52,wt*1.0,pat)+logo('lk',ink,0,0,150,0,f'translate({cx-75} {yr+56})'))
    # rim + interior with food
    o+=f'<ellipse cx="{cx}" cy="{yr}" rx="{wt}" ry="{ry}" fill="{rimc}"/><ellipse cx="{cx}" cy="{yr}" rx="{wt-9}" ry="{ry-6}" fill="#2a1420"/>'
    o+=food(seed,cx-(wt-12),yr-(ry-8),(wt-12)*2,(ry-8)*2)
    # dome lid
    dome=f'M{cx-wt+4},{yr} C{cx-wt+4},{yr-130} {cx+wt-4},{yr-130} {cx+wt-4},{yr} A{wt-4},{ry-2} 0 0 1 {cx-wt+4},{yr}Z'
    o+=f'<path d="{dome}" fill="url(#gDome)"/><path d="M{cx-wt+40},{yr-30} C{cx-wt+60},{yr-90} {cx-20},{yr-100} {cx+10},{yr-96}" fill="none" stroke="#fff" stroke-opacity=".65" stroke-width="6" stroke-linecap="round"/>'
    o+=f'<ellipse cx="{cx}" cy="{yr}" rx="{wt+3}" ry="{ry+2}" fill="none" stroke="{rimc}" stroke-width="5"/>'
    return svgwrap(540,380,o)
def bowl_pet(sleeve=LIME,ink=AUB,seed=9):
    cx,yr=270,130;wt,wb=170,120;hgt=170;ry=50;yb=yr+hgt
    body=f'M{cx-wt},{yr} L{cx-wb},{yb} A{wb},{ry*wb/wt:.1f} 0 0 0 {cx+wb},{yb} L{cx+wt},{yr} A{wt},{ry} 0 0 1 {cx-wt},{yr}Z'
    o=shadow(cx,yb+ry*.7+8,wt*.95,22,.35)
    o+=f'<path d="{body}" fill="#e9f1f2" fill-opacity=".55"/>'
    # food inside body (lower part) + visible on top
    o+=clipped(body,food(seed,cx-wt+10,yb-110,wt*2-20,150,AUB,IVORY,None).replace('preserveAspectRatio="none"','preserveAspectRatio="none"'))
    o+=f'<path d="{body}" fill="url(#gClear)"/>'
    # sleeve band
    y1,y2=yr+55,yr+120;w1,w2=hw(y1,yr,hgt,wt,wb),hw(y2,yr,hgt,wt,wb);r1,r2=ry*w1/wt,ry*w2/wt
    band=f'M{cx-w1},{y1} A{w1},{r1} 0 0 0 {cx+w1},{y1} L{cx+w2},{y2} A{w2},{r2} 0 0 1 {cx-w2},{y2}Z'
    o+=face(band,sleeve,'gSh')+clipped(band,logo('wm',ink,0,0,112,0,f'translate({cx-56} {y1+14})'))
    # rim & dome
    o+=f'<ellipse cx="{cx}" cy="{yr}" rx="{wt}" ry="{ry}" fill="#fff" fill-opacity=".35" stroke="#fff" stroke-opacity=".7" stroke-width="3"/>'
    o+=food(seed,cx-wt+14,yr-ry+10,(wt-14)*2,(ry-10)*2)
    dome=f'M{cx-wt},{yr} C{cx-wt},{yr-120} {cx+wt},{yr-120} {cx+wt},{yr} A{wt},{ry} 0 0 1 {cx-wt},{yr}Z'
    o+=f'<path d="{dome}" fill="url(#gDome)"/><path d="M{cx-wt+36},{yr-26} C{cx-wt+60},{yr-84} {cx-20},{yr-92} {cx+10},{yr-88}" fill="none" stroke="#fff" stroke-opacity=".7" stroke-width="6" stroke-linecap="round"/>'
    return svgwrap(540,360,o)
def cup_hot(body=IVORY,band=LIME,pat=AUB,ink=AUB,lid=AUB):
    cx,yt=140,110;wt,wb=88,62;hgt=210;ry=22;yb=yt+hgt
    path=f'M{cx-wt},{yt} L{cx-wb},{yb} A{wb},{ry*wb/wt:.1f} 0 0 0 {cx+wb},{yb} L{cx+wt},{yt} A{wt},{ry} 0 0 1 {cx-wt},{yt}Z'
    o=shadow(cx,yb+16,wt*.9,12,.38)
    o+=face(path,body,'gSh')
    # sleeve
    y1,y2=yt+55,yt+150;w1,w2=hw(y1,yt,hgt,wt,wb),hw(y2,yt,hgt,wt,wb)
    sl=f'M{cx-w1},{y1} A{w1},{ry*w1/wt:.1f} 0 0 0 {cx+w1},{y1} L{cx+w2},{y2} A{w2},{ry*w2/wt:.1f} 0 0 1 {cx-w2},{y2}Z'
    o+=face(sl,band,'gSh')+clipped(sl,logo('wm',ink,0,0,100,0,f'translate({cx-50} {y1+30})'))
    o+=clipped(path,m_art(cx-wt,yb-40,wt*1.4,pat))
    # lid
    o+=f'<path d="M{cx-wt-6},{yt} L{cx-wt+2},{yt-18} Q{cx},{yt-34} {cx+wt-2},{yt-18} L{cx+wt+6},{yt}Z" fill="{lid}"/><path d="M{cx-wt-6},{yt} L{cx-wt+2},{yt-18} Q{cx},{yt-34} {cx+wt-2},{yt-18} L{cx+wt+6},{yt}Z" fill="url(#gSh)"/>'
    o+=f'<ellipse cx="{cx}" cy="{yt}" rx="{wt+6}" ry="{ry+3}" fill="{lid}"/><ellipse cx="{cx}" cy="{yt}" rx="{wt+6}" ry="{ry+3}" fill="url(#gTop)"/><ellipse cx="{cx+22}" cy="{yt-3}" rx="13" ry="4.5" fill="#000" opacity=".5"/>'
    return svgwrap(280,370,o)
def cup_cold(drink=LIME,seed=3,sticker=AUB):
    cx,yt=140,100;wt,wb=84,60;hgt=230;ry=21;yb=yt+hgt
    path=f'M{cx-wt},{yt} L{cx-wb},{yb} A{wb},{ry*wb/wt:.1f} 0 0 0 {cx+wb},{yb} L{cx+wt},{yt} A{wt},{ry} 0 0 1 {cx-wt},{yt}Z'
    o=shadow(cx,yb+16,wt*.9,12,.35)
    o+=f'<path d="{path}" fill="#e9f1f2" fill-opacity=".5"/>'
    lvl=yt+40;wl=hw(lvl,yt,hgt,wt,wb)
    liq=f'M{cx-wl},{lvl} L{cx-wb},{yb} A{wb},{ry*wb/wt:.1f} 0 0 0 {cx+wb},{yb} L{cx+wl},{lvl} A{wl},{ry*wl/wt:.1f} 0 0 1 {cx-wl},{lvl}Z'
    o+=f'<path d="{liq}" fill="{drink}"/><path d="{liq}" fill="url(#gSh)"/>'
    # straw
    o+=f'<path d="M{cx+10},{yt-60} L{cx+22},{yb-30}" stroke="{AUB}" stroke-width="9" stroke-linecap="round"/><path d="M{cx+10},{yt-60} L{cx+22},{yb-30}" stroke="#fff" stroke-opacity=".25" stroke-width="3"/>'
    o+=f'<path d="{path}" fill="url(#gClear)"/>'
    o+=f'<circle cx="{cx-6}" cy="{yt+120}" r="38" fill="{sticker}"/><circle cx="{cx-6}" cy="{yt+120}" r="38" fill="url(#gSh)"/>'+logo('mg',LIME,0,0,44,0,f'translate({cx-28} {yt+106})')
    # dome lid
    o+=f'<path d="M{cx-wt-4},{yt} C{cx-wt-4},{yt-52} {cx+wt+4},{yt-52} {cx+wt+4},{yt} A{wt+4},{ry+2} 0 0 1 {cx-wt-4},{yt}Z" fill="url(#gDome)"/><ellipse cx="{cx}" cy="{yt}" rx="{wt+6}" ry="{ry+3}" fill="none" stroke="#fff" stroke-opacity=".8" stroke-width="3"/>'
    return svgwrap(280,390,o)
def bottle(liquid=LIME,label=IVORY,ink=AUB,cap=AUB):
    cx=110;o=shadow(cx,372,60,10,.38)
    body='M84,110 L84,62 Q84,48 92,40 L92,20 L128,20 L128,40 Q136,48 136,62 L136,110 Q158,128 158,160 L158,350 Q158,364 144,364 L76,364 Q62,364 62,350 L62,160 Q62,128 84,110Z'
    o+=f'<path d="{body}" fill="#dfeaec" fill-opacity=".55"/>'
    o+=clipped(body,f'<rect x="50" y="120" width="120" height="260" fill="{liquid}"/>')
    o+=f'<path d="{body}" fill="url(#gClear)"/><path d="M72,150 L72,340" stroke="#fff" stroke-opacity=".6" stroke-width="5" stroke-linecap="round"/>'
    o+=f'<rect x="62" y="190" width="96" height="120" fill="{label}"/><rect x="62" y="190" width="96" height="120" fill="url(#gSh)"/>'+logo('wm',ink,0,0,72,0,'translate(74 208)')+f'<text x="110" y="292" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="8" letter-spacing="2" fill="{ink}">COLD PRESSED · 330ML</text>'
    o+=f'<rect x="88" y="10" width="44" height="26" rx="4" fill="{cap}"/><rect x="88" y="10" width="44" height="26" rx="4" fill="url(#gSh)"/>'
    return svgwrap(220,390,o)
def sauce(color=AUB,ink=LIME,w=100):
    cx=w;o=shadow(cx,150,70,10,.38)
    body=f'M{cx-64},70 L{cx-50},140 A50,12 0 0 0 {cx+50},140 L{cx+64},70Z'
    o+=face(body,color,'gSh')+clipped(body,logo('wm',ink,0,0,78,0,f'translate({cx-39} 84)'))
    o+=f'<ellipse cx="{cx}" cy="70" rx="68" ry="15" fill="{color}"/><ellipse cx="{cx}" cy="70" rx="68" ry="15" fill="url(#gTop)"/><ellipse cx="{cx}" cy="66" rx="68" ry="12" fill="#fff" fill-opacity=".14"/>'
    return svgwrap(2*w,170,o)
def jar(layers=(LIME,APR,AUB,IVORY)):
    cx=130;o=shadow(cx,300,80,12,.38)
    body='M70,90 Q58,100 58,120 L58,270 Q58,292 80,292 L180,292 Q202,292 202,270 L202,120 Q202,100 190,90Z'
    o+=f'<path d="{body}" fill="#e5eef0" fill-opacity=".5"/>'
    lay=''.join(f'<rect x="50" y="{130+i*38}" width="160" height="38" fill="{c}"/>' for i,c in enumerate(layers))
    o+=clipped(body,lay)+f'<path d="{body}" fill="url(#gClear)"/><path d="M72,130 L72,270" stroke="#fff" stroke-opacity=".6" stroke-width="5" stroke-linecap="round"/>'
    o+=f'<rect x="64" y="64" width="132" height="30" rx="6" fill="{AUB}"/><rect x="64" y="64" width="132" height="30" rx="6" fill="url(#gSh)"/>'+logo('wm',LIME,0,0,70,0,'translate(95 72)')
    return svgwrap(260,320,o)
if __name__=='__main__':
    items=[bowl_paper(),bowl_pet(),cup_hot(),cup_cold(),bottle(),sauce(),jar(),bowl_paper(LIME,AUB,AUB,3,AUB)]
    html=f'<body style="margin:0;background:#E9E1D0">{SYM}{DEFS}<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:20px;width:1700px">'+''.join(f'<div>{i}</div>' for i in items)+'</div></body>'
    open('mk/o2.html','w').write(html)
