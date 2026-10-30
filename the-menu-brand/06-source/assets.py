import os,json
from geom import parts,dims
AUB='#371C2B';LIME='#D8E457';IVORY='#F4EFE6';BLACK='#000000';WHITE='#FFFFFF'
LW,LH,MH,THH,mh=dims['LW'],dims['LH'],dims['MH'],dims['THH'],dims['mh']
os.makedirs('pkg/svg',exist_ok=True)
def svg(vb_w,vb_h,body,title,bg=None,pad=0):
    r=f'<rect x="{-pad}" y="{-pad}" width="{vb_w+2*pad}" height="{vb_h+2*pad}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {vb_w+2*pad:.2f} {vb_h+2*pad:.2f}" role="img" aria-labelledby="t"><title id="t">{title}</title>{r}{body}</svg>'
def g(id,d,fill):return f'<g id="{id}" fill="{fill}" fill-rule="evenodd"><path d="{d}"/></g>'
def full(fill,bg=None,pad=0):
    return svg(LW,LH,g('the',parts['the'],fill)+g('menu',parts['menu'],fill)+g('tagline',parts['tag'],fill),'The Menu — Eat Well. Taste More.',bg,pad)
def wordmark(fill,bg=None,pad=0):
    return svg(LW,THH,g('the',parts['the'],fill)+g('menu',parts['menu'],fill),'The Menu',bg,pad)
def menu_only(fill,bg=None,pad=0):
    return svg(LW,MH,g('menu',parts['menu_only'],fill),'menu',bg,pad)
def mglyph(fill,bg=None,pad=0):
    return svg(1000,mh,g('m',parts['m'],fill),'The Menu monogram',bg,pad)
def square(bg,fill,rx=0):
    S=1000;sc=0.56;gw=1000*sc;gh=mh*sc
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" role="img" aria-labelledby="t"><title id="t">The Menu monogram</title><rect id="background" width="{S}" height="{S}" rx="{rx}" fill="{bg}"/><g id="m" transform="translate({(S-gw)/2:.2f} {(S-gh)/2:.2f}) scale({sc})" fill="{fill}" fill-rule="evenodd"><path d="{parts["m"]}"/></g></svg>'
cols={'aubergine':AUB,'ivory':IVORY,'black':BLACK,'white':WHITE}
files={}
for n,c in cols.items():
    files[f'logo-full-{n}']=full(c);files[f'logo-wordmark-{n}']=wordmark(c);files[f'logo-menu-{n}']=menu_only(c);files[f'monogram-{n}']=mglyph(c)
files['logo-full-lime']=full(LIME);files['logo-menu-lime']=menu_only(LIME);files['monogram-lime-glyph']=mglyph(LIME)
files['monogram-square-lime']=square(LIME,AUB);files['monogram-square-aubergine']=square(AUB,LIME);files['monogram-square-ivory']=square(IVORY,AUB)
files['app-icon-aubergine']=square(AUB,LIME,220);files['app-icon-lime']=square(LIME,AUB,220)
files['logo-full-on-ivory']=full(AUB,IVORY,90);files['logo-full-on-aubergine']=full(IVORY,AUB,90);files['logo-full-on-lime']=full(AUB,LIME,90)
for k,v in files.items():open(f'pkg/svg/the-menu_{k}.svg','w').write(v)
json.dump({k:[ (float(v.split('viewBox="')[1].split()[2]) ),float(v.split('viewBox="')[1].split()[3].strip('"'))] for k,v in files.items()},open('sizes.json','w'))
print(len(files),'svgs')
