from PIL import Image
import glob,sys
d=sys.argv[1];fs=sorted(glob.glob(d+'/p*.png'))
for k in range(0,len(fs),6):
    ims=[Image.open(f).resize((800,450)) for f in fs[k:k+6]];rows=(len(ims)+1)//2
    sh=Image.new('RGB',(1610,rows*460),'#555')
    for i,im in enumerate(ims):sh.paste(im,((i%2)*810,(i//2)*460))
    sh.save(f'{d}/sheet{k//6+1}.png')
print(len(fs))
