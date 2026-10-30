import sys;sys.path.insert(0,'..');sys.path.insert(0,'.')
import os;os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')
from geom import parts,dims
from arabic import ar,AH,dims_ar,ar_menu_only
import assets2 as A2
LW,LH,MH,THH,mh=dims['LW'],dims['LH'],dims['MH'],dims['THH'],dims['mh']
AUB='#371C2B';LIME='#D8E457';IVORY='#F4EFE6';APR='#F2A65A'
def lum(h):
    h=h.lstrip('#');r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c:c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def cr(a,b):
    l1,l2=sorted([lum(a),lum(b)],reverse=True);return (l1+.05)/(l2+.05)
def rgb(h):h=h.lstrip('#');return tuple(int(h[i:i+2],16) for i in (0,2,4))
def cmyk(h):
    r,g,b=[x/255 for x in rgb(h)];k=1-max(r,g,b)
    return tuple(round(v*100) for v in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
VB={'lk':(LW,LH),'wm':(LW,THH),'mn':(LW,MH),'mg':(1000,mh),'alk':(1000,AH),'awm':(1000,dims_ar['THH']),'amn':(1000,dims_ar['MH'])}
def lk(color='currentColor',kind='lk',style='',cls=''):
    w,h=VB[kind];return f'<svg class="{cls}" style="color:{color};{style}" viewBox="0 0 {w:.2f} {h:.2f}"><use href="#{kind}"/></svg>'
SYM=f'''<svg width="0" height="0" style="position:absolute"><defs>
<symbol id="lk" viewBox="0 0 {LW} {LH:.2f}"><g fill="currentColor" fill-rule="evenodd"><path d="{parts['the']}"/><path d="{parts['menu']}"/><path d="{parts['tag']}"/></g></symbol>
<symbol id="wm" viewBox="0 0 {LW} {THH:.2f}"><g fill="currentColor" fill-rule="evenodd"><path d="{parts['the']}"/><path d="{parts['menu']}"/></g></symbol>
<symbol id="mn" viewBox="0 0 {LW} {MH:.2f}"><path fill="currentColor" fill-rule="evenodd" d="{parts['menu_only']}"/></symbol>
<symbol id="mg" viewBox="0 0 1000 {mh:.2f}"><path fill="currentColor" fill-rule="evenodd" d="{parts['m']}"/></symbol>
<symbol id="alk" viewBox="0 0 1000 {AH:.2f}"><g fill="currentColor"><path d="{ar['the']}"/><path d="{ar['menu']}"/><path d="{ar['tag']}"/></g></symbol>
<symbol id="awm" viewBox="0 0 1000 {dims_ar['THH']:.2f}"><g fill="currentColor"><path d="{ar['the']}"/><path d="{ar['menu']}"/></g></symbol>
<symbol id="amn" viewBox="0 0 1000 {dims_ar['MH']:.2f}"><path fill="currentColor" d="{ar_menu_only}"/></symbol>
</defs></svg>'''
def ic(name,color='currentColor',size=40,sw=3.2):
    return f'<span style="display:inline-block;width:{size}px;height:{size}px;color:{color}">{A2.icon_inline(name,"currentColor",sw)}</span>'
def bowl(seed,size,bg=None,rim=AUB,inner=IVORY):
    return A2.bowl(seed,size,bg,rim,inner).replace('<svg ','<svg style="width:100%;height:100%;display:block" ',1)
def hdr(n,en,ar_,part=''):
    return f'<div class="hdr"><span class="n">{n}</span><span class="t">{en}</span><span class="part">{part}</span><span class="ar">{ar_}</span></div>'
def page(bg,body,color=AUB,cls=''):
    return f'<section class="page {cls}" style="background:{bg};color:{color}">{body}</section>'
def divider(num,en,ar_,bg=AUB,fg=IVORY,accent=LIME):
    return page(bg,f'''<div style="position:absolute;left:110px;top:150px;font-family:Fraunces;font-weight:600;font-size:420px;line-height:1;color:{accent}">{num}</div>
<div style="position:absolute;left:110px;bottom:150px"><div class="eyebrow" style="color:{fg}">PART {num}</div><div class="serif" style="font-size:96px;line-height:1.02;margin-top:14px">{en}</div></div>
<div style="position:absolute;right:110px;bottom:150px;font-family:'IBM Plex Sans Arabic';font-weight:700;font-size:80px;direction:rtl">{ar_}</div>
<div style="position:absolute;right:-60px;top:-80px;width:620px;color:{accent};opacity:.9">{lk('currentColor','mg')}</div>''',fg)
def mono_sq(bg,fg,size,rx=0,extra=''):
    return f'<div class="sq" style="width:{size}px;height:{size}px;background:{bg};border-radius:{rx}px;{extra}">{lk(fg,"mg","width:56%")}</div>'
CSS=f'''
@font-face{{font-family:'DM Sans';src:url('fonts/DMSans.ttf');font-weight:100 1000}}
@font-face{{font-family:'Fraunces';src:url('fonts/Fraunces.ttf');font-weight:100 900}}
@font-face{{font-family:'IBM Plex Sans Arabic';src:url('fonts/IBMPlexSansArabic-Medium.ttf');font-weight:400 500}}
@font-face{{font-family:'IBM Plex Sans Arabic';src:url('fonts/IBMPlexSansArabic-Bold.ttf');font-weight:600 800}}
@font-face{{font-family:'Lalezar';src:url('fonts/Lalezar-Regular.ttf')}}
@page{{size:1600px 900px;margin:0}}
*{{box-sizing:border-box}}body{{margin:0;background:#888;font-family:'DM Sans','IBM Plex Sans Arabic',sans-serif;color:{AUB}}}
.page{{position:relative;width:1600px;height:900px;overflow:hidden;page-break-after:always;break-after:page}}
.hdr{{position:absolute;left:110px;top:64px;right:110px;display:flex;align-items:baseline;gap:18px;font-weight:700}}
.hdr .n{{font-size:15px;letter-spacing:3px;opacity:.5}}.hdr .t{{font-size:34px;font-family:Fraunces;font-weight:600}}.hdr .part{{font-size:12px;letter-spacing:3px;opacity:.45;font-weight:700}}.hdr .ar{{margin-left:auto;font-family:'IBM Plex Sans Arabic';font-size:24px;opacity:.65;font-weight:600}}
.meta{{position:absolute;font-size:15px;letter-spacing:4px;font-weight:600;text-transform:uppercase}}
.serif{{font-family:Fraunces,serif;font-weight:600}}.eyebrow{{font-size:14px;letter-spacing:4px;font-weight:700;opacity:.55}}
.abs{{position:absolute}}.rtl{{direction:rtl;text-align:right;font-family:'IBM Plex Sans Arabic',sans-serif}}
.h-ar{{font-family:'IBM Plex Sans Arabic';font-weight:700}}
.note{{position:absolute;font-size:18px;line-height:1.6;opacity:.85}}.small{{font-size:16px;line-height:1.55;opacity:.72}}
svg{{display:block}}
.grid{{position:absolute;display:grid;gap:18px}}.tile{{position:relative;border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;border:1px solid #0001}}.tile .cap{{position:absolute;left:18px;bottom:14px;font-size:14px;font-weight:600;opacity:.75}}
.row{{position:absolute;display:flex;gap:18px}}.sq{{display:flex;align-items:center;justify-content:center;flex:none}}
.card{{border-radius:12px;padding:30px;position:absolute}}.card h3{{margin:0 0 10px;font-size:26px}}.card p{{margin:0;font-size:18px;line-height:1.55;opacity:.85}}
.card.ar h3,.card.ar p{{font-family:'IBM Plex Sans Arabic'}}.card.ar{{direction:rtl;text-align:right}}.card.ar h3{{font-size:30px}}.card.ar p{{font-size:21px;line-height:1.7}}
.pill{{display:inline-block;border-radius:30px;padding:6px 16px;font-size:15px;font-weight:700;letter-spacing:1px;border:1.5px solid currentColor}}
.tag{{display:inline-block;background:{AUB};color:{IVORY};border-radius:4px;padding:3px 9px;font-size:13px;font-weight:700;letter-spacing:1px}}
table{{border-collapse:collapse;width:100%}}td,th{{text-align:left;padding:10px 14px;border-bottom:1px solid #0002;font-size:17px;vertical-align:top}}th{{font-size:13px;letter-spacing:2px;opacity:.6}}
.rtl td,.rtl th{{text-align:right}}
'''
def build(pages,out='book2.html'):
    html=f'<!doctype html><html dir="ltr"><head><meta charset="utf-8"><title>The Menu — Brand Book</title><style>{CSS}</style></head><body>{SYM}{"".join(pages)}</body></html>'
    open(out,'w').write(html);return len(pages)
