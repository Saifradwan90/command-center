import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen
class Seg(BasePen):
    def __init__(s,gs):super().__init__(gs);s.ops=[]
    def _moveTo(s,p):s.ops.append(('M',[p]))
    def _lineTo(s,p):s.ops.append(('L',[p]))
    def _curveToOne(s,a,b,c):s.ops.append(('C',[a,b,c]))
    def _qCurveToOne(s,a,b):s.ops.append(('Q',[a,b]))
    def _closePath(s):s.ops.append(('Z',[]))
    def _endPath(s):s.ops.append(('Z',[]))
def shape(fontfile,text,size,var=None):
    blob=hb.Blob.from_file_path(fontfile);face=hb.Face(blob);font=hb.Font(face)
    buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(font,buf,{"kern":True,"liga":True})
    tt=TTFont(fontfile);gs=tt.getGlyphSet();order=tt.getGlyphOrder();sc=size/tt['head'].unitsPerEm
    x=0;ops=[]
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        sp=Seg(gs);gs[order[info.codepoint]].draw(sp)
        for c,pts in sp.ops:
            ops.append((c,[((x+pos.x_offset+px)*sc,-(pos.y_offset+py)*sc) for px,py in pts]))
        x+=pos.x_advance
    xs=[p[0] for _,pts in ops for p in pts];ys=[p[1] for _,pts in ops for p in pts]
    return ops,(min(xs),min(ys),max(xs),max(ys))
def tx(ops,dx,dy,s=1.0):
    return ''.join(c+' '.join(f'{p[0]*s+dx:.2f} {p[1]*s+dy:.2f}' for p in pts) for c,pts in ops)
LAL='fonts/Lalezar-Regular.ttf';PLEX='fonts/IBMPlexSansArabic-Medium.ttf'
mo,mb=shape(LAL,'منيو',300);to,tb=shape(LAL,'ذا',300);go,gb=shape(PLEX,'كُل صح. تذوّق أكثر.',60)
ms=1000/(mb[2]-mb[0]);MH=(mb[3]-mb[1])*ms
ts=0.30*ms;the_w=(tb[2]-tb[0])*ts;the_h=(tb[3]-tb[1])*ts;gap=0.10*MH
gs_=700/(gb[2]-gb[0]);tag_h=(gb[3]-gb[1])*gs_;tgap=0.17*MH
top=the_h+gap
ar=dict(
 the=tx(to,1000-the_w-tb[0]*ts,-tb[1]*ts,ts),
 menu=tx(mo,-mb[0]*ms,top-mb[1]*ms,ms),
 tag=tx(go,(1000-700)/2-gb[0]*gs_,top+MH+tgap-gb[1]*gs_,gs_))
AH=top+MH+tgap+tag_h
ar_menu_only=tx(mo,-mb[0]*ms,-mb[1]*ms,ms)
dims_ar=dict(AH=AH,MH=MH,THH=top+MH)
if __name__=='__main__':print(AH,MH,the_w,the_h,tag_h,len(ar['menu']))
