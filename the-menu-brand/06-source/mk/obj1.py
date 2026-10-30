from mock import *
from common import mh,THH,LH,MH
def m_art(x,y,w,color):return f'<use href="#mg" x="{x}" y="{y}" width="{w}" height="{w*mh/1000:.1f}" style="color:{color}"/>'
def clamshell():
    W,H,D=420,170,230;x0,y0=60,150
    def fa():
        return f'<rect x="{x0}" y="{y0+80}" width="{W}" height="{H-80}" fill="{AUB}"/>'+m_art(x0-30,y0+60,240,LIME)+m_art(x0+190,y0+60,240,LIME)+logo('lk',AUB,0,0,200,0,f'translate({x0+W/2-100} {y0+12})')
    return svgwrap(760,430,box3d(x0,y0,W,H,D,LIME,'#E3EF69','#A9B530',fa=fa(),ta=lambda m:f'<g transform="{m}">{logo("lk",AUB,0,0,250,0,"translate(85 40)")}</g>',sa=lambda m:f'<g transform="{m}"><rect width="300" height="200" fill="{AUB}"/>{logo("mg",LIME,0,0,90,0,"translate(30 90)")}</g>'))
def meal_box():
    W,H,D=380,150,200;x0,y0=70,170
    def fa():
        return f'<circle cx="{x0+W/2}" cy="{y0+H/2+6}" r="52" fill="{LIME}"/>'+f'<svg x="{x0+W/2-48}" y="{y0+H/2-42}" width="96" height="96" viewBox="0 0 400 400">{bowl(5,400,None,AUB,IVORY)[bowl(5,400).index(">")+1:-6]}</svg>'+f'<text x="{x0+22}" y="{y0+H-18}" font-family="DM Sans" font-weight="800" font-size="13" letter-spacing="3" fill="{LIME}">480 KCAL</text>'
    return svgwrap(700,400,box3d(x0,y0,W,H,D,AUB,'#4B2B3E','#241019',fa=fa(),ta=lambda m:f'<g transform="{m}">{logo("lk",IVORY,0,0,230,0,"translate(75 45)")}</g>',sa=lambda m:f'<g transform="{m}">{m_art(-10,40,170,LIME)}</g>'))
def window_box():
    W,H,D=380,170,210;x0,y0=70,150
    def fa():
        return f'<rect x="{x0}" y="{y0}" width="{W}" height="{H}" fill="{IVORY}"/><path d="M{x0+90},{y0+H-12} L{x0+90},{y0+60} Q{x0+90},{y0+20} {x0+130},{y0+20} L{x0+W-130},{y0+20} Q{x0+W-90},{y0+20} {x0+W-90},{y0+60} L{x0+W-90},{y0+H-12}Z" fill="#fff" opacity=".85"/>'+f'<svg x="{x0+W/2-65}" y="{y0+40}" width="130" height="120" viewBox="0 0 400 400" preserveAspectRatio="none">{bowl(6,400,None,AUB,IVORY)[bowl(6,400).index(">")+1:-6]}</svg>'+f'<path d="M{x0+90},{y0+H-12} L{x0+90},{y0+60} Q{x0+90},{y0+20} {x0+130},{y0+20} L{x0+W-130},{y0+20} Q{x0+W-90},{y0+20} {x0+W-90},{y0+60} L{x0+W-90},{y0+H-12}Z" fill="url(#gClear)"/>'+logo('wm',AUB,0,0,70,0,f'translate({x0+14} {y0+14})')
    return svgwrap(700,400,box3d(x0,y0,W,H,D,IVORY,'#fff','#C9C1B0',fa=fa(),ta=lambda m:f'<g transform="{m}"><rect width="400" height="260" fill="{LIME}"/>{logo("lk",AUB,0,0,220,0,"translate(80 50)")}</g>'))
def bag_shop(color=AUB,ink=IVORY,pat=LIME,w=300,h=360,gus=110,py=150):
    x0,y0=60,90
    gx=KX*gus*.8;gy=KY*gus*.8
    front=P((x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h))
    side=P((x0+w,y0),(x0+w+gx,y0-gy),(x0+w+gx,y0+h-gy),(x0+w,y0+h))
    o=shadow(x0+w/2+gx/2,y0+h+12,w*.62,16,.4)
    # handles (behind)
    hx1,hx2=x0+w*.28,x0+w*.72
    o+=f'<path d="M{hx1+gx*.4},{y0-gy*.4+10} C{hx1+gx*.4},{y0-gy-60} {hx2+gx*.4},{y0-gy-60} {hx2+gx*.4},{y0-gy*.4+10}" fill="none" stroke="{color}" stroke-width="7"/>'
    o+=face(side,shade_c:=(color if color!=AUB else '#2A1420'),'gShR')
    o+=f'<path d="M{x0+w+gx/2},{y0-gy/2} L{x0+w+gx/2+0.1},{y0+h-gy/2}" stroke="#000" stroke-opacity=".18" stroke-width="2"/>'
    o+=face(front,color,'gShV')
    o+=clipped(front,m_art(x0-20,y0+h-py,w*.95,pat)+m_art(x0+w*.5,y0+h-py,w*.95,pat))
    o+=f'<path d="M{x0},{y0+34} L{x0+w},{y0+34}" stroke="#000" stroke-opacity=".12" stroke-width="2"/>'
    o+=logo('lk',ink,0,0,w*.66,0,f'translate({x0+w*.17} {y0+80})')
    # handle holes + rope front
    o+=f'<path d="M{hx1},{y0+18} C{hx1},{y0-62} {hx2},{y0-62} {hx2},{y0+18}" fill="none" stroke="{color}" stroke-width="7"/><path d="M{hx1},{y0+18} C{hx1},{y0-62} {hx2},{y0-62} {hx2},{y0+18}" fill="none" stroke="url(#gShV)" stroke-width="7"/>'
    return svgwrap(w+gx+120,h+130,o)
def bag_sos():
    x0,y0=100,110;w,h=190,330;gus=70;gx=KX*gus*.8;gy=KY*gus*.8
    front=P((x0,y0+30),(x0+w,y0+30),(x0+w,y0+h),(x0,y0+h))
    side=P((x0+w,y0+30),(x0+w+gx,y0+30-gy),(x0+w+gx,y0+h-gy),(x0+w,y0+h))
    o=shadow(x0+w/2+gx/2,y0+h+10,w*.7,14,.38)
    o+=face(side,'#CFC7B6','gShR')
    # folded top (two folds)
    o+=face(P((x0,y0+30),(x0+w,y0+30),(x0+w+gx,y0+30-gy),(x0+gx,y0+30-gy)),'#fff','gTop')
    o+=face(front,IVORY,'gShV')
    o+=clipped(front,f'<rect x="{x0}" y="{y0+30}" width="{w}" height="64" fill="{LIME}"/>'+logo('lk',AUB,0,0,w*.7,0,f'translate({x0+w*.15} {y0+130})')+m_art(x0-10,y0+h-100,w*.9,AUB))
    o+=f'<path d="M{x0},{y0+94} L{x0+w},{y0+94}" stroke="#000" stroke-opacity=".12" stroke-width="2"/>'
    # round seal
    o+=f'<circle cx="{x0+w/2}" cy="{y0+92}" r="30" fill="{AUB}"/><circle cx="{x0+w/2}" cy="{y0+92}" r="30" fill="url(#gSh)"/>'+logo('mg',LIME,0,0,36,0,f'translate({x0+w/2-18} {y0+80})')
    return svgwrap(w+gx+200,h+160,o)
if __name__=='__main__':
    items=[clamshell(),meal_box(),window_box(),bag_shop(),bag_sos(),bag_shop(LIME,AUB,AUB,w=220,h=250,gus=80,py=70)]
    html=f'<body style="margin:0;background:#E9E1D0">{SYM}{DEFS}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:20px;width:1700px">'+''.join(f'<div style="background:#E9E1D0">{i}</div>' for i in items)+'</div></body>'
    open('mk/o1.html','w').write(html)
