import numpy as np, potrace, json
from PIL import Image, ImageFilter
SRC='/root/.claude/uploads/48498a66-9993-5a91-bcd2-0b0fe8c46378/4630a574-image.png'
im=Image.open(SRC).convert('RGB')
def otsu(g):
    h,_=np.histogram(g,bins=256,range=(0,256));tot=g.size;s=sum(i*h[i] for i in range(256));sb=wb=0;mx=0;t=0
    for i in range(256):
        wb+=h[i]
        if wb==0:continue
        wf=tot-wb
        if wf==0:break
        sb+=i*h[i];v=wb*wf*(sb/wb-(s-sb)/wf)**2
        if v>mx:mx=v;t=i
    return t
def trace(box,scale=8,med=17,blur=1.6,turd=40,alpha=1.15,opt=1.0,bias=0):
    c=im.crop(box).resize(((box[2]-box[0])*scale,(box[3]-box[1])*scale),Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur*scale/4))
    g=np.asarray(c.convert('L')).astype(float);t=otsu(g)+bias
    m=Image.fromarray(((g<t)*255).astype('uint8')).filter(ImageFilter.MedianFilter(med));mk=np.asarray(m)>127
    pl=potrace.Bitmap(~mk).trace(turdsize=turd,alphamax=alpha,opticurve=True,opttolerance=opt)
    curves=[]
    for cv in pl:
        sp=cv.start_point;segs=[];pts=[(sp.x,sp.y)]
        for s in cv.segments:
            if s.is_corner:segs.append(('L',s.c.x,s.c.y));segs.append(('L',s.end_point.x,s.end_point.y));pts+=[(s.c.x,s.c.y),(s.end_point.x,s.end_point.y)]
            else:segs.append(('C',s.c1.x,s.c1.y,s.c2.x,s.c2.y,s.end_point.x,s.end_point.y));pts+=[(s.c1.x,s.c1.y),(s.c2.x,s.c2.y),(s.end_point.x,s.end_point.y)]
        xs=[p[0]/scale+box[0] for p in pts];ys=[p[1]/scale+box[1] for p in pts]
        curves.append(dict(start=[sp.x/scale+box[0],sp.y/scale+box[1]],segs=[[s[0]]+[ (v/scale+(box[0] if i%2==0 else box[1])) for i,v in enumerate(s[1:])] for s in segs],bbox=[min(xs),min(ys),max(xs),max(ys)]))
    return curves,t
out={}
out['word'],t1=trace((160,85,1000,340));out['tag'],t2=trace((235,355,910,395),turd=6,blur=0.8,opt=0.6,med=5);out['mono'],t3=trace((1100,170,1395,335))
json.dump(out,open('curves.json','w'))
for k,v in out.items():print(k,len(v),'curves',sum(len(c['segs']) for c in v),'segments')
