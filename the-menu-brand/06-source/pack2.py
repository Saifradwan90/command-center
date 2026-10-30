import os,json,shutil
from geom import parts,dims
from arabic import ar,AH,dims_ar,ar_menu_only
import assets2 as A2
AUB='#371C2B';LIME='#D8E457';IVORY='#F4EFE6';BLACK='#000';WHITE='#FFF'
LW,LH,mh=dims['LW'],dims['LH'],dims['mh']
root='pkg2';
for d in ['svg/arabic','svg/icons','svg/illustrations','svg/patterns','png','docs']:os.makedirs(f'{root}/{d}',exist_ok=True)
def wr(p,s):open(f'{root}/{p}','w').write(s)
cols={'aubergine':AUB,'ivory':IVORY,'black':BLACK,'white':WHITE,'lime':LIME}
for n,c in cols.items():
    wr(f'svg/arabic/the-menu_ar-logo-full-{n}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {AH:.2f}" role="img"><title>ذا منيو — كُل صح. تذوّق أكثر.</title><g fill="{c}"><path id="the" d="{ar["the"]}"/><path id="menu" d="{ar["menu"]}"/><path id="tagline" d="{ar["tag"]}"/></g></svg>')
    wr(f'svg/arabic/the-menu_ar-logo-wordmark-{n}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {dims_ar["THH"]:.2f}" role="img"><title>ذا منيو</title><g fill="{c}"><path id="the" d="{ar["the"]}"/><path id="menu" d="{ar["menu"]}"/></g></svg>')
    sc=LH/AH;W=1000+120+1000*sc
    wr(f'svg/arabic/the-menu_bilingual-horizontal-{n}.svg',f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {LH:.2f}" role="img"><title>The Menu · ذا منيو</title><g fill="{c}" fill-rule="evenodd" id="latin"><path d="{parts["the"]}"/><path d="{parts["menu"]}"/><path d="{parts["tag"]}"/></g><rect x="1060" y="20" width="3" height="{LH-40:.1f}" fill="{c}" opacity=".35"/><g id="arabic" transform="translate(1120 0) scale({sc:.4f})" fill="{c}"><path d="{ar["the"]}"/><path d="{ar["menu"]}"/><path d="{ar["tag"]}"/></g></svg>')
for n in A2.ICONS:
    wr(f'svg/icons/icon-{n}.svg',A2.icon_svg(n,AUB,3.2,96).replace(f'stroke="{AUB}"','stroke="currentColor"'))
sheet='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 420"><rect width="640" height="420" fill="#fff"/>'
for i,n in enumerate(A2.ICONS):
    x=(i%4)*160+40;y=(i//4)*100+20
    sheet+=f'<g transform="translate({x} {y})" fill="none" stroke="{AUB}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">{A2.ICONS[n]}</g>'
wr('svg/icons/_icon-sheet.svg',sheet+'</svg>')
for s,(bg,rim,inner) in enumerate([(LIME,AUB,IVORY),(AUB,LIME,AUB),(APR:='#F2A65A',AUB,IVORY),(IVORY,AUB,IVORY),(LIME,AUB,IVORY),(AUB,LIME,AUB)],1):
    wr(f'svg/illustrations/bowl-{s:02d}.svg',A2.bowl(s,800,bg,rim,inner))
# patterns
def pattern(bg,fg):
    cells=''
    for r in range(8):
        for c in range(6):
            cells+=f'<g transform="translate({c*400-200+(r%2)*200} {r*180-30}) scale({360/1000})" fill="{fg}" fill-rule="evenodd"><path d="{parts["m"]}"/></g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200"><rect width="1200" height="1200" fill="{bg}"/><clipPath id="c"><rect width="1200" height="1200"/></clipPath><g clip-path="url(#c)">{cells}</g></svg>'
wr('svg/patterns/m-pattern-lime.svg',pattern(LIME,AUB));wr('svg/patterns/m-pattern-aubergine.svg',pattern(AUB,LIME));wr('svg/patterns/m-pattern-ivory.svg',pattern(IVORY,AUB))
