import sys,os,math
sys.path.insert(0,os.path.abspath('b2'));sys.path.insert(0,os.path.abspath('.'))
from common import *   # chdir to brand dir; gives lk, SYM, bowl, A2, colors, dims
import itertools
_id=itertools.count(1)
def uid(p='u'):return f'{p}{next(_id)}'
DEFS='''<svg width="0" height="0" style="position:absolute"><defs>
<linearGradient id="gSh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".30"/><stop offset=".35" stop-color="#fff" stop-opacity=".04"/><stop offset=".7" stop-color="#000" stop-opacity=".06"/><stop offset="1" stop-color="#000" stop-opacity=".30"/></linearGradient>
<linearGradient id="gShR" x1="1" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".34"/><stop offset="1" stop-color="#000" stop-opacity=".12"/></linearGradient>
<linearGradient id="gShV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".2"/></linearGradient>
<linearGradient id="gTop" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity=".34"/></linearGradient>
<linearGradient id="gGloss" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".75"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="gClear" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset=".4" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#cfd8dc" stop-opacity=".35"/></linearGradient>
<radialGradient id="gDome" cx=".35" cy=".25" r=".9"><stop offset="0" stop-color="#fff" stop-opacity=".7"/><stop offset=".5" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#9fb4b8" stop-opacity=".35"/></radialGradient>
<filter id="fSh" x="-60%" y="-500%" width="220%" height="1100%"><feGaussianBlur stdDeviation="9"/></filter>
<filter id="fSh2" x="-60%" y="-500%" width="220%" height="1100%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="fPaper" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="3" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
</defs></svg>'''
def P(*pts):return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
def logo(kind,color,x,y,w,rot=0,mat=None):
    from common import VB
    vw,vh=VB[kind];h=w*vh/vw
    t=mat if mat else f'translate({x:.1f} {y:.1f}) rotate({rot})'
    return f'<g transform="{t}" style="color:{color}"><use href="#{kind}" width="{w:.1f}" height="{h:.1f}"/></g>'
def shadow(cx,cy,rx,ry,op=.35):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#000" opacity="{op}" filter="url(#fSh)"/>'
def face(d,fill,shade='gSh',extra=''):
    return f'<path d="{d}" fill="{fill}"/><path d="{d}" fill="url(#{shade})"/>{extra}'
def clipped(d,content):
    i=uid('c');return f'<clipPath id="{i}"><path d="{d}"/></clipPath><g clip-path="url(#{i})">{content}</g>'
def mpat(x,y,w,color,rows,cols,dx,dy,off=0):
    s='';
    from common import mh
    for r in range(rows):
        for c in range(cols):
            s+=f'<use href="#mg" x="{x+c*dx+(r%2)*off:.1f}" y="{y+r*dy:.1f}" width="{w}" height="{w*mh/1000:.1f}" style="color:{color}"/>'
    return s
def svgwrap(w,h,body,style=''):
    return f'<svg viewBox="0 0 {w} {h}" style="width:100%;height:auto;overflow:visible;{style}">{body}</svg>'
KX,KY=.55,.38   # oblique projection factors
def box3d(x0,y0,w,h,D,cf,ct,cs,fa=None,ta=None,sa=None,radius=0):
    """front rect at (x0,y0) w×h ; depth D drawn up-right. art callbacks get transform matrix strings."""
    dx,dy=KX*D,KY*D
    front=P((x0,y0),(x0+w,y0),(x0+w,y0+h),(x0,y0+h))
    top=P((x0,y0),(x0+w,y0),(x0+w+dx,y0-dy),(x0+dx,y0-dy))
    side=P((x0+w,y0),(x0+w+dx,y0-dy),(x0+w+dx,y0+h-dy),(x0+w,y0+h))
    o=shadow(x0+w/2+dx/2,y0+h+10,w*.62,16,.4)
    o+=face(front,cf,'gShV')
    if fa:o+=clipped(front,fa)
    o+=face(side,cs,'gShR')
    if sa:o+=clipped(side,sa(f'matrix({KX},{-KY},0,1,{x0+w},{y0})'))
    o+=face(top,ct,'gTop')
    if ta:o+=clipped(top,ta(f'matrix(1,0,{-KX},{KY},{x0+KX*D},{y0-KY*D})'))
    return o
