from geom import parts,dims
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
    if k>=1:return (0,0,0,100)
    return tuple(round(v*100) for v in ((1-r-k)/(1-k),(1-g-k)/(1-k),(1-b-k)/(1-k),k))
def lk(cls='',color='currentColor',kind='lk',style=''):
    vb={'lk':(LW,LH),'wm':(LW,THH),'mn':(LW,MH),'mg':(1000,mh)}[kind]
    return f'<svg class="{cls}" style="color:{color};{style}" viewBox="0 0 {vb[0]:.2f} {vb[1]:.2f}"><use href="#{kind}"/></svg>'
SYM=f'''<svg width="0" height="0" style="position:absolute"><defs>
<symbol id="lk" viewBox="0 0 {LW} {LH:.2f}"><g fill="currentColor" fill-rule="evenodd"><path d="{parts['the']}"/><path d="{parts['menu']}"/><path d="{parts['tag']}"/></g></symbol>
<symbol id="wm" viewBox="0 0 {LW} {THH:.2f}"><g fill="currentColor" fill-rule="evenodd"><path d="{parts['the']}"/><path d="{parts['menu']}"/></g></symbol>
<symbol id="mn" viewBox="0 0 {LW} {MH:.2f}"><path fill="currentColor" fill-rule="evenodd" d="{parts['menu_only']}"/></symbol>
<symbol id="mg" viewBox="0 0 1000 {mh:.2f}"><path fill="currentColor" fill-rule="evenodd" d="{parts['m']}"/></symbol>
</defs></svg>'''
def mono_sq(bg,fg,size,rx=0,extra=''):
    return f'<div class="sq" style="width:{size}px;height:{size}px;background:{bg};border-radius:{rx}px;{extra}">{lk("",fg,"mg","width:56%")}</div>'
def hdr(n,en,ar,dark=False):
    return f'<div class="hdr"><span class="n">{n}</span><span class="t">{en}</span><span class="ar">{ar}</span></div>'
P=[]
# 1 cover
P.append(f'''<section class="page" style="background:{AUB};color:{IVORY}">
<div style="position:absolute;right:-120px;bottom:-250px;width:1000px;color:{LIME};opacity:1">{lk("","currentColor","mg")}</div>
<div style="position:absolute;left:110px;top:240px;width:760px">{lk("",IVORY)}</div>
<div class="meta" style="left:110px;top:90px">BRAND GUIDELINES · v1.0</div><div class="meta" style="left:110px;bottom:80px">Eat well. Taste more.</div>
<div class="meta" style="left:110px;bottom:110px;opacity:.6;letter-spacing:2px">دليل الهوية البصرية</div></section>''')
# 2 idea
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("01","Brand idea","فكرة العلامة")}
<div style="position:absolute;left:110px;top:200px;width:760px"><div class="eyebrow">POSITIONING</div><h1 class="serif" style="font-size:112px;line-height:.98;margin:20px 0 28px">Healthy food.<br><em style="color:{AUB}">Exceptional</em> taste.</h1>
<p class="lead">The Menu proves that eating well and craving more are the same thing. Flavour is the reason people choose us — and the reason they come back.</p>
<p class="ar-lead">أكل صحي. نكهة استثنائية.</p></div>
<div class="col3" style="left:960px;top:200px;width:530px">
<div class="pill" style="background:{AUB};color:{IVORY}"><b>01 · Flavour leads</b><span>Taste is the headline, health is the proof.</span></div>
<div class="pill" style="background:{LIME};color:{AUB}"><b>02 · Fresh, never preachy</b><span>Clean, confident and generous — no diet-culture tone.</span></div>
<div class="pill" style="background:#fff;color:{AUB};border:1.5px solid {AUB}22"><b>03 · Premium, approachable</b><span>Global-brand polish with a neighbourhood warmth.</span></div></div></section>''')
# 3 anatomy
P.append(f'''<section class="page" style="background:#fff">{hdr("02","The logo","الشعار")}
<div class="anat" style="left:300px;top:250px;width:1000px">{lk("",AUB)}
<div class="ann top" style="left:0;top:-110px"><span>the — editorial serif, lowercase</span><i></i></div>
<div class="ann top" style="right:0;top:-110px;align-items:flex-end;text-align:right"><span>menu — custom lettering, sculpted &amp; soft</span><i></i></div>
<div class="ann bot" style="left:80px;bottom:-100px"><i></i><span>Tagline — spaced capitals, +16% tracking</span></div></div></div>
<div class="note" style="left:110px;bottom:36px;width:1380px">The wordmark is bespoke lettering, not a typeface. Never retype it — always use the supplied artwork. Distinguishing gestures: the flowing foot of the <b>m</b>, the angled bar of the <b>e</b> and the tail of the <b>u</b>.</div></section>''')
# 4 clear space & min size
cs=0.5*MH
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("03","Clear space & minimum size","المساحة الآمنة والحد الأدنى")}
<div style="position:absolute;left:110px;top:200px;width:820px;height:520px;background:#fff;border-radius:6px"></div>
<div class="cs" style="left:200px;top:300px;width:640px"><div class="csbox"></div>{lk("",AUB)}<span class="x tl">½x</span><span class="x tr">½x</span><span class="x bl">½x</span><span class="x br">½x</span></div>
<div class="note" style="left:110px;top:740px;width:820px"><b>x</b> = x-height of “menu”. Keep ½x free on all sides, in every application.</div>
<div style="position:absolute;left:1000px;top:200px;width:490px"><div class="eyebrow">MINIMUM SIZE</div>
<div class="minrow"><div style="width:150px">{lk("",AUB)}</div><span>Full logo · 150 px / 38 mm</span></div>
<div class="minrow"><div style="width:100px">{lk("",AUB,"wm")}</div><span>Without tagline · 100 px / 25 mm</span></div>
<div class="minrow"><div style="width:72px">{lk("",AUB,"mn")}</div><span>“menu” only · 72 px / 18 mm</span></div>
<div class="minrow"><div style="width:28px">{lk("",AUB,"mg")}</div><span>Monogram m · 28 px / 7 mm</span></div>
<p class="small" style="margin-top:26px">Below 150 px the tagline becomes illegible: switch to the wordmark without tagline.</p></div></section>''')
# 5 suite
def tile(bg,inner,label,fg=AUB,extra=''):
    return f'<div class="tile" style="background:{bg};color:{fg};{extra}">{inner}<span class="cap" style="color:{fg}">{label}</span></div>'
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("04","Logo suite","منظومة الشعار")}
<div class="grid" style="left:110px;top:190px;width:1380px;grid-template-columns:repeat(3,1fr);grid-auto-rows:270px">
{tile("#fff",lk("w70",AUB),"Primary · on ivory/white")}
{tile(AUB,lk("w70",IVORY),"Reverse · on aubergine",IVORY)}
{tile(LIME,lk("w70",AUB),"On lime")}
{tile("#fff",lk("w60",AUB,"wm"),"Without tagline")}
{tile(AUB,lk("w60",LIME,"mn"),"“menu” · signage",LIME)}
{tile("#fff",lk("w70","#000"),"One colour · black")}</div>
<div class="row" style="left:110px;top:760px">{mono_sq(LIME,AUB,100)}{mono_sq(AUB,LIME,100)}{mono_sq(IVORY,AUB,100,0,"border:1px solid #0001")}{mono_sq(AUB,LIME,100,24)}{mono_sq(LIME,AUB,100,24)}<span class="small" style="align-self:center;margin-left:14px;max-width:600px">Monogram · social avatars · favicon · stamps · app icon (rounded). The monogram never replaces the logo on first contact.</span></div></section>''')
# 6 colour
cards=[(AUB,'Aubergine','Primary','45%',IVORY),(LIME,'Lime','Signal','20%',AUB),(IVORY,'Ivory','Canvas','30%',AUB),(APR,'Apricot','Optional flavour accent','5%',AUB)]
cc=''
for h,n,r,p,t in cards:
    R=rgb(h);K=cmyk(h)
    cc+=f'<div class="chip" style="background:{h};color:{t};{"border:1px solid #0002" if h==IVORY else ""}"><div class="pct">{p}</div><b>{n}</b><span>{r}</span><dl><dt>HEX</dt><dd>{h}</dd><dt>RGB</dt><dd>{R[0]} {R[1]} {R[2]}</dd><dt>CMYK*</dt><dd>{K[0]} {K[1]} {K[2]} {K[3]}</dd></dl></div>'
P.append(f'''<section class="page" style="background:#fff">{hdr("05","Colour","الألوان")}
<div class="chips" style="left:110px;top:190px">{cc}</div>
<div class="note" style="left:110px;bottom:80px;width:1380px">* CMYK values are starting-point conversions. Match to Pantone / press proofs before print; lime is outside the CMYK gamut and will print duller than on screen. Apricot is a proposed accent — not part of the original mark.</div></section>''')
# 7 pairings
pairs=[(AUB,IVORY),(AUB,LIME),(IVORY,AUB),(LIME,AUB),(LIME,IVORY),(APR,IVORY)]
pp=''
for bg,fg in pairs:
    r=cr(bg,fg);ok='AAA' if r>=7 else 'AA' if r>=4.5 else 'AA Large' if r>=3 else 'Fail'
    cls='bad' if ok=='Fail' else ''
    pp+=f'<div class="pair" style="background:{bg};color:{fg}"><div class="big serif">Aa</div><div class="ratio">{r:.1f}:1</div><div class="bdg {cls}">{ok}</div></div>'
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("06","Colour pairings & contrast","ثنائيات الألوان")}
<div class="grid" style="left:110px;top:190px;width:1380px;grid-template-columns:repeat(6,1fr);grid-auto-rows:340px">{pp}</div>
<div class="note" style="left:110px;top:600px;width:1380px"><b>Always:</b> aubergine on lime or ivory · ivory on aubergine · lime as a field with aubergine type.<br><b>Never:</b> lime or apricot type on ivory (fails contrast) · lime on white.</div>
<div style="position:absolute;left:110px;top:700px;width:1380px;height:70px;display:flex;border-radius:6px;overflow:hidden"><div style="flex:45;background:{AUB}"></div><div style="flex:30;background:{IVORY};border:1px solid #0002"></div><div style="flex:20;background:{LIME}"></div><div style="flex:5;background:{APR}"></div></div><div class="small" style="position:absolute;left:110px;top:780px">Proportion of use: 45 / 30 / 20 / 5</div></section>''')
# 8 type
P.append(f'''<section class="page" style="background:#fff">{hdr("07","Typography","الخطوط")}
<div class="tcol" style="left:110px;top:190px"><div class="eyebrow">DISPLAY · FRAUNCES</div><div class="serif" style="font-size:76px;line-height:1">Taste<br>more.</div><p class="small">Headlines, menu items, editorial moments. Soft, warm, high-contrast — echoes the “the”.</p></div>
<div class="tcol" style="left:590px;top:190px"><div class="eyebrow">TEXT & UI · DM SANS</div><div style="font-family:'DM Sans';font-weight:700;font-size:68px;line-height:1.05;letter-spacing:-1px">Eat well.<br>Taste more.</div><p style="font-family:'DM Sans';font-size:20px;line-height:1.5;margin-top:18px;max-width:380px">Roasted aubergine, charred lime, toasted seeds — a bowl built for flavour first. 520 kcal · 38 g protein.</p><p class="small">Taglines (spaced caps, +16% tracking), body copy, labels.</p></div>
<div class="tcol" style="left:1060px;top:190px;direction:rtl;text-align:right"><div class="eyebrow" style="direction:ltr;text-align:left">ARABIC · IBM PLEX SANS ARABIC</div><div style="font-family:'IBM Plex Sans Arabic';font-weight:700;font-size:54px;line-height:1.35">أكل صحي.<br>نكهة استثنائية.</div><p style="font-family:'IBM Plex Sans Arabic';font-size:21px;line-height:1.8;margin-top:12px">طبق مصمم للنكهة أولاً، بمكونات طازجة وتوازن مدروس.</p></div>
<div class="note" style="left:110px;bottom:80px;width:1380px">Hierarchy — Display (Fraunces 600) · Subhead (DM Sans 700) · Body (DM Sans 400/500) · Tagline (DM Sans 600, caps, +16%). All three families are open-source (Google Fonts). Pairings are proposals: confirm against your brand needs.</div></section>''')
# 9 pattern
cells=''
for r in range(4):
    for c in range(4):
        off=(r%2)*200
        cells+=f'<div style="position:absolute;left:{c*400-200+off}px;top:{r*180-30}px;width:360px;color:{AUB}">{lk("","currentColor","mg")}</div>'
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("08","The m — graphic device","الحرف m كعنصر بصري")}
<div class="pat" style="left:110px;top:190px;width:880px;height:500px;background:{LIME}"><div style="position:absolute;inset:0;overflow:hidden">{cells.replace(AUB,AUB)}</div></div>
<div class="pat" style="left:1030px;top:190px;width:460px;height:500px;background:{AUB}"><div style="position:absolute;left:-120px;top:70px;width:760px;color:{LIME}">{lk("","currentColor","mg")}</div><div style="position:absolute;left:30px;top:30px;width:230px;color:{IVORY}">{lk("","currentColor","wm")}</div></div>
<div class="note" style="left:110px;top:730px;width:1380px">Oversize and crop the m so it bleeds off the edge. Alternate aubergine and lime. Use as packaging wraps, bag sides, menu covers and social backgrounds — always paired with, never instead of, the logo.</div></section>''')
# 10 misuse
bad=[("Don’t stretch or squash",lk("w70",AUB),"transform:scaleX(1.25) scaleY(.7)"),("Don’t rotate",lk("w70",AUB),"transform:rotate(-12deg)"),("Don’t add shadows or effects",lk("w70",AUB),"filter:drop-shadow(6px 6px 0 #7a5a7a) drop-shadow(0 0 8px #d8e457)"),("Don’t recolour",lk("w70","#c0392b"),""),("Don’t put lime on ivory",lk("w70",LIME),"bg:"+IVORY),("Don’t use on busy backgrounds",lk("w70",AUB),"bg:repeating-linear-gradient(45deg,#d8e457 0 20px,#371c2b 20px 40px)"),("Don’t outline",f'<div class="w70" style="-webkit-text-stroke:0">{lk("w70","transparent","lk","")}</div>',"outline"),("Don’t rebuild the lettering",'<div style="font-family:Fraunces;font-weight:800;font-size:90px;color:'+AUB+';line-height:1">the menu</div>',"")]
mt=''
for t,svg,st in bad:
    bgc='#fff';sty=''
    if st.startswith('bg:'):bgc=st[3:]
    elif st=='outline':
        svg=f'<svg class="w70" viewBox="0 0 {LW} {LH:.2f}" style="overflow:visible"><g fill="none" stroke="{AUB}" stroke-width="5" fill-rule="evenodd"><path d="{parts["the"]}"/><path d="{parts["menu"]}"/><path d="{parts["tag"]}"/></g></svg>'
    else:sty=st
    inner=svg.replace('class="w70"','class="w70"',1)
    if sty:inner=f'<div style="{sty};width:58%;display:flex;justify-content:center">{svg}</div>'.replace('class="w70"','style="width:100%"')
    mt+=f'<div class="tile bad" style="background:{bgc}">{inner}<span class="cap" style="color:#c0392b;background:#fffd;padding:2px 8px;border-radius:4px;left:12px">✕ {t}</span></div>'
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("09","Logo misuse","الاستخدامات الخاطئة")}
<div class="grid" style="left:110px;top:190px;width:1380px;grid-template-columns:repeat(4,1fr);grid-auto-rows:285px">{mt}</div></section>''')
# 11 packaging
def boxsvg():
    pat=''.join(f'<use href="#mg" x="{-40+i*300}" y="{150+(0 if i%2==0 else 0)}" width="360" height="{360*mh/1000:.1f}" style="color:{AUB}"/>' for i in range(4))
    return f'''<svg viewBox="0 0 760 460" style="width:100%"><defs><clipPath id="bx"><path d="M60,120 L220,40 L540,40 L700,120 L700,400 Q700,420 680,420 L80,420 Q60,420 60,400 Z"/></clipPath></defs>
<ellipse cx="380" cy="436" rx="320" ry="14" fill="#0002"/><g clip-path="url(#bx)"><rect width="760" height="460" fill="{LIME}"/><path d="M60,120 L220,40 L540,40 L700,120Z" fill="#fff" opacity=".18"/><rect x="0" y="250" width="760" height="220" fill="{AUB}"/>{pat.replace(f'color:{AUB}',f'color:{LIME}')}</g>
<g transform="translate(250 130) scale(.26)" style="color:{AUB}"><use href="#lk" width="1000" height="{LH:.1f}"/></g></svg>'''
def bagsvg():
    return f'''<svg viewBox="0 0 520 520" style="width:100%"><ellipse cx="260" cy="500" rx="190" ry="12" fill="#0002"/><path d="M170,150 L170,70 Q170,40 200,40 L320,40 Q350,40 350,70 L350,150" fill="none" stroke="{AUB}" stroke-width="14"/>
<rect x="70" y="140" width="380" height="350" rx="6" fill="{AUB}"/><rect x="70" y="140" width="380" height="26" fill="#fff" opacity=".07"/>
<g transform="translate(120 190) scale(.28)" style="color:{IVORY}"><use href="#lk" width="1000" height="{LH:.1f}"/></g>
<g clip-path="url(#bg)"><use href="#mg" x="250" y="330" width="260" height="{260*mh/1000:.1f}" style="color:{LIME}"/></g><clipPath id="bg"><rect x="70" y="140" width="380" height="350"/></clipPath></svg>'''
P.append(f'''<section class="page" style="background:#E9E1D0">{hdr("10","Packaging","التغليف")}
<div style="position:absolute;left:110px;top:190px;width:760px">{boxsvg()}</div><div style="position:absolute;left:960px;top:150px;width:520px">{bagsvg()}</div>
<div class="note" style="left:110px;bottom:70px;width:1380px">Flat illustrative mock-ups — replace with die-lines. Lime stock + aubergine ink for boxes; aubergine kraft + ivory/lime for bags.</div></section>''')
# 12 signage
slats=''.join(f'<i style="left:{x}px"></i>' for x in range(0,680,14))
P.append(f'''<section class="page" style="background:#fff">{hdr("11","Signage","اللافتات")}
<div class="sign day" style="left:110px;top:190px"><div class="blocks"></div><div style="position:absolute;left:90px;top:210px;width:500px;color:{AUB};filter:drop-shadow(5px 7px 3px #0004)">{lk("",AUB,"mn")}</div><span class="cap">DAY · beige stone · raised aubergine letters</span></div>
<div class="sign night" style="left:810px;top:190px"><div class="fascia">{slats}</div><div style="position:absolute;left:90px;top:218px;width:500px;color:{LIME};filter:drop-shadow(0 0 14px {LIME}cc) drop-shadow(0 0 40px {LIME}88)">{lk("",LIME,"mn")}</div><span class="cap" style="color:{LIME}">NIGHT · metal fascia · lime face-lit letters</span></div>
<div class="note" style="left:110px;top:700px;width:1380px"><b>Rule:</b> aubergine letters only on light stone; on the dark vertical-slat metal use lime (face-lit) or ivory. Recommended build: 3D letters, 40–60 mm return, simplified inner joints, min. 12 mm stroke at the thinnest point of the <b>m</b> foot.</div></section>''')
# 13 digital
P.append(f'''<section class="page" style="background:{IVORY}">{hdr("12","Digital","الواجهات الرقمية")}
<div class="row" style="left:110px;top:190px;gap:30px">{mono_sq(AUB,LIME,200,100)}{mono_sq(LIME,AUB,200,100)}{mono_sq(IVORY,AUB,200,100,"border:1px solid #0002")}</div>
<div class="post" style="left:110px;top:430px;background:{LIME};color:{AUB}"><div class="serif" style="font-size:58px;line-height:1;font-weight:600">Eat well.<br>Taste more.</div><div style="position:absolute;left:34px;bottom:30px;width:150px">{lk("",AUB,"wm")}</div></div>
<div class="post" style="left:560px;top:430px;background:{AUB};color:{IVORY}"><div style="position:absolute;right:-60px;top:20px;width:320px;color:{LIME}">{lk("","currentColor","mg")}</div><div style="font-family:'DM Sans';font-weight:800;font-size:44px;line-height:1.05;position:absolute;left:34px;bottom:90px;width:300px">Aubergine,<br>charred lime,<br>zero guilt.</div><div style="position:absolute;left:34px;bottom:30px;width:150px">{lk("",IVORY,"wm")}</div></div>
<div class="post" style="left:1010px;top:430px;background:#fff;color:{AUB};border:1px solid #0001"><div style="position:absolute;left:34px;top:30px;width:150px">{lk("",AUB,"wm")}</div><div style="position:absolute;left:34px;top:130px;right:34px;font-family:'DM Sans'"><b style="font-size:22px;letter-spacing:3px">MENU · BOWLS</b><div style="margin-top:14px;font-size:19px;line-height:2.1;border-top:2px solid {AUB};padding-top:10px">Charred Aubergine Bowl <span style="float:right">42</span><br>Lime & Tahini Chicken <span style="float:right">46</span><br>Green Goddess Salad <span style="float:right">38</span></div></div></div>
<div style="position:absolute;left:800px;top:240px;width:690px;font-size:18px;line-height:1.6" class="small">Avatars: monogram only. Post templates: lime or aubergine field, logo bottom-left, one bold line of copy. Menu: aubergine on ivory, prices right-aligned.</div></section>''')
# 14 next
P.append(f'''<section class="page" style="background:{AUB};color:{IVORY}">{hdr("13","Next steps","الخطوات التالية",True)}
<div style="position:absolute;left:110px;top:200px;width:1000px;font-size:26px;line-height:1.9;font-family:'DM Sans'">
<div class="step"><b>01</b> Designer refinement of the wordmark curves (hand-tuned Béziers) and final kerning.</div>
<div class="step"><b>02</b> Arabic wordmark — a companion lockup built with the same sculpted logic.</div>
<div class="step"><b>03</b> Trademark search for “The Menu” (descriptive name) + handles/domains.</div>
<div class="step"><b>04</b> Pantone & CMYK press proofs; fascia shop-drawings with the sign maker.</div>
<div class="step"><b>05</b> Icon set, photography direction and motion principles.</div></div>
<div style="position:absolute;right:-150px;bottom:-230px;width:900px;color:{LIME}">{lk("","currentColor","mg")}</div>
<div style="position:absolute;left:110px;bottom:80px;width:300px">{lk("",IVORY,"wm")}</div></section>''')
CSS=f'''
@font-face{{font-family:'DM Sans';src:url('fonts/DMSans.ttf');font-weight:100 1000}}
@font-face{{font-family:'Fraunces';src:url('fonts/Fraunces.ttf');font-weight:100 900}}
@font-face{{font-family:'IBM Plex Sans Arabic';src:url('fonts/IBMPlexSansArabic-Medium.ttf');font-weight:400 500}}
@font-face{{font-family:'IBM Plex Sans Arabic';src:url('fonts/IBMPlexSansArabic-Bold.ttf');font-weight:600 800}}
@page{{size:1600px 900px;margin:0}}
*{{box-sizing:border-box}}body{{margin:0;background:#888;font-family:'DM Sans',sans-serif;color:{AUB}}}
.page{{position:relative;width:1600px;height:900px;overflow:hidden;page-break-after:always;break-after:page}}
.hdr{{position:absolute;left:110px;top:70px;right:110px;display:flex;align-items:baseline;gap:18px;font-weight:700}}
.hdr .n{{font-size:15px;letter-spacing:3px;opacity:.5}}.hdr .t{{font-size:34px;font-family:Fraunces;font-weight:600}}.hdr .ar{{margin-left:auto;font-family:'IBM Plex Sans Arabic';font-size:22px;opacity:.6;font-weight:500}}
.meta{{position:absolute;font-size:15px;letter-spacing:4px;font-weight:600;text-transform:uppercase}}
.serif{{font-family:Fraunces,serif;font-weight:600}}.eyebrow{{font-size:14px;letter-spacing:4px;font-weight:700;opacity:.55}}
.lead{{font-size:24px;line-height:1.5;max-width:640px}}.ar-lead{{font-family:'IBM Plex Sans Arabic';font-size:34px;font-weight:700;margin-top:30px}}
.col3{{position:absolute;display:flex;flex-direction:column;gap:20px}}.pill{{border-radius:10px;padding:30px 34px;display:flex;flex-direction:column;gap:8px}}.pill b{{font-size:26px}}.pill span{{font-size:19px;opacity:.85}}
.note{{position:absolute;font-size:18px;line-height:1.6;opacity:.85}}.small{{font-size:16px;line-height:1.55;opacity:.7}}
.w70{{width:70%}}.w60{{width:60%}}svg{{display:block}}
.anat{{position:absolute}}.ann{{position:absolute;font-size:15px;font-weight:600;letter-spacing:.5px;white-space:nowrap;display:flex;flex-direction:column;gap:6px}}.ann i{{display:block;width:2px;height:60px;background:{AUB}}}.ann.top{{top:auto}}.ann span{{display:block}}
.cs{{position:absolute}}.csbox{{position:absolute;inset:-{cs*0.64:.0f}px;border:2px dashed {AUB}66;background:{LIME}22}}.cs svg{{position:relative}}.x{{position:absolute;font-size:13px;font-weight:700;background:{AUB};color:{IVORY};padding:2px 6px;border-radius:3px}}.x.tl{{left:-{cs*0.64:.0f}px;top:-{cs*0.64:.0f}px}}.x.tr{{right:-{cs*0.64:.0f}px;top:-{cs*0.64:.0f}px}}.x.bl{{left:-{cs*0.64:.0f}px;bottom:-{cs*0.64:.0f}px}}.x.br{{right:-{cs*0.64:.0f}px;bottom:-{cs*0.64:.0f}px}}
.minrow{{display:flex;align-items:center;gap:26px;padding:20px 0;border-bottom:1px solid #0002}}.minrow span{{font-size:16px;opacity:.7}}.minrow>div{{flex:none}}
.grid{{position:absolute;display:grid;gap:18px}}.tile{{position:relative;border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden;border:1px solid #0001}}.tile .cap{{position:absolute;left:18px;bottom:14px;font-size:14px;font-weight:600;opacity:.75}}.tile.bad{{border:1.5px solid #c0392b55}}
.row{{position:absolute;display:flex;gap:18px}}.sq{{display:flex;align-items:center;justify-content:center;flex:none}}
.chips{{position:absolute;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;width:1380px}}.chip{{height:480px;border-radius:10px;padding:30px;display:flex;flex-direction:column;position:relative}}.chip .pct{{font-size:64px;font-family:Fraunces;font-weight:600}}.chip b{{font-size:28px;margin-top:6px}}.chip span{{font-size:16px;opacity:.8}}.chip dl{{margin:auto 0 0;display:grid;grid-template-columns:70px 1fr;row-gap:6px;font-size:17px}}.chip dt{{opacity:.7;font-weight:600}}.chip dd{{margin:0;font-weight:700}}
.pair{{border-radius:8px;position:relative;padding:22px;display:flex;flex-direction:column;justify-content:space-between;border:1px solid #0002}}.pair .big{{font-size:110px;line-height:1}}.pair .ratio{{font-size:30px;font-weight:700}}.bdg{{font-size:15px;font-weight:700;letter-spacing:1px;border:1.5px solid currentColor;border-radius:20px;padding:3px 12px;width:max-content}}.bdg.bad{{border-style:dashed;text-decoration:line-through}}
.tcol{{position:absolute;width:430px}}.tcol .eyebrow{{margin-bottom:22px}}
.pat{{position:absolute;border-radius:8px;overflow:hidden}}
.sign{{position:absolute;width:680px;height:470px;border-radius:8px;overflow:hidden}}.sign .cap{{position:absolute;left:18px;bottom:14px;font-size:14px;font-weight:600;opacity:.8}}.sign.day{{background:linear-gradient(135deg,#e3d8c3,#c6b9a1)}}.sign.day .blocks{{position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 78px,#8d7f6855 78px 80px),repeating-linear-gradient(90deg,transparent 0 238px,#8d7f6844 238px 240px)}}.sign.night{{background:#1b181d}}.sign.night .fascia{{position:absolute;left:0;right:0;top:110px;height:250px;background:#2b292e}}.fascia i{{position:absolute;top:0;bottom:0;width:2px;background:#000;opacity:.35}}
.post{{position:absolute;width:420px;height:420px;border-radius:6px;overflow:hidden;padding:34px}}
.step{{display:flex;gap:26px;border-bottom:1px solid #ffffff22;padding:6px 0}}.step b{{color:{LIME};font-family:Fraunces;font-size:30px}}
'''
html=f'<!doctype html><html><head><meta charset="utf-8"><title>The Menu — Brand Guidelines</title><style>{CSS}</style></head><body>{SYM}{"".join(P)}</body></html>'
open('book.html','w').write(html)
print(len(P),'pages',len(html)//1024,'KB')
