import json
C=json.load(open('curves.json'))
X0,Y0=175.0,93.0       # lockup origin (source px)
S=1000/810.0            # normalise lockup width to 1000 units
def d(curves,ox,oy,sc):
    o=''
    f=lambda v,off:f'{(v-off)*sc:.2f}'
    for v in curves:
        o+=f"M{f(v['start'][0],ox)} {f(v['start'][1],oy)}"
        for s in v['segs']:
            if s[0]=='L':o+=f"L{f(s[1],ox)} {f(s[2],oy)}"
            else:o+=f"C{f(s[1],ox)} {f(s[2],oy)} {f(s[3],ox)} {f(s[4],oy)} {f(s[5],ox)} {f(s[6],oy)}"
        o+='Z'
    return o
W=C['word']
the=[W[i] for i in (5,6,7,8)]; menu=[W[i] for i in (3,1,4,2,0)]
tag=C['tag']
# bbox lockup: x 175..985, y 93..385
LW=1000.0; LH=(385-93)*S
parts=dict(
 the=d(the,X0,Y0,S), menu=d(menu,X0,Y0,S), tag=d(tag,X0,Y0,S),
)
# menu-only (no the): origin at menu top-left
MY0=158.0
parts['menu_only']=d(menu,X0,MY0,S); MH=(329-MY0)*S
parts['the_menu']=d(the+menu,X0,Y0,S); THH=(329-93)*S
# monogram glyph (m) normalised to its own bbox
mx0,my0,mx1,my1=1108,180,1382,333
ms=1000/(mx1-mx0)
parts['m']=d(C['mono'],mx0,my0,ms); mh=(my1-my0)*ms
dims=dict(LW=LW,LH=LH,MH=MH,THH=THH,mh=mh,S=S)
if __name__=='__main__':print({k:len(v) for k,v in parts.items()},dims)
