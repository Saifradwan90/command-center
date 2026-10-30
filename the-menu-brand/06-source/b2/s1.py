from common import *
P=[]
P.append(divider('01','Strategy','الاستراتيجية'))
# Foundation
def fcard(x,y,w,h,bg,fg,en,ar_,body_ar,body_en):
    return f'''<div class="card ar" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{fg}">
<div class="eyebrow" style="direction:ltr;text-align:right;color:{fg}">{en}</div><h3 style="margin-top:14px">{ar_}</h3><p>{body_ar}</p><div class="small" style="direction:ltr;text-align:right;margin-top:14px;font-family:'DM Sans';font-size:15px">{body_en}</div></div>'''
P.append(page(IVORY,hdr('1.1','Brand foundation','أساس العلامة','STRATEGY')+
 fcard(110,170,680,300,AUB,IVORY,'PURPOSE','لماذا نوجد','نُثبت أن الأكل الصحي لا يتطلب التنازل عن المتعة، وأن النكهة هي أقصر طريق لعادة أكل أفضل.','Prove that eating well never means giving up pleasure.')+
 fcard(810,170,680,300,LIME,AUB,'VISION','الرؤية','أن يصبح «ذا منيو» الاسم الأول لكل من يريد أن يأكل صحيًا بنكهة تستحق العودة، في كل مدينة نصل إليها.','The first name in healthy food people actually crave.')+
 fcard(110,490,680,300,'#fff',AUB,'MISSION','الرسالة','نطهو وجبات طازجة ومتوازنة غذائيًا، تُبنى على النكهة أولًا، ونقدّمها بتجربة عصرية سريعة وسخيّة.','Fresh, balanced, flavour-first meals — served fast and generously.')+
 f'''<div class="card ar" style="left:810px;top:490px;width:680px;height:300px;background:#fff;color:{AUB}"><div class="eyebrow" style="direction:ltr;text-align:right">VALUES</div><h3 style="margin-top:14px">قيمنا الخمس</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:10px;direction:rtl">{''.join(f'<span class="pill" style="background:{c};color:{f};border-color:transparent;font-family:IBM Plex Sans Arabic;font-size:20px;letter-spacing:0;padding:8px 18px">{t}</span>' for t,c,f in [('النكهة أولًا',AUB,IVORY),('طزاجة بلا تسوية',LIME,AUB),('الوضوح والشفافية',IVORY,AUB),('السخاء',APR,AUB),('الإتقان',AUB,LIME)])}</div>
<div class="small" style="direction:ltr;text-align:right;margin-top:26px;font-size:15px">Flavour first · Uncompromised freshness · Transparency · Generosity · Craft</div></div>'''))
# Positioning
P.append(page('#fff',hdr('1.2','Positioning','التموضع','STRATEGY')+
 f'''<div class="abs rtl" style="right:110px;top:180px;width:760px"><div class="eyebrow" style="direction:ltr;text-align:right">POSITIONING STATEMENT</div>
<p style="font-size:34px;line-height:1.65;font-weight:700;margin:20px 0 0">لأصحاب الأسلوب العصري الذين يريدون أكلًا صحيًا يستحق العودة، <span style="background:{LIME};padding:0 8px">«ذا منيو»</span> هو المطعم الذي يجعل <u style="text-decoration-color:{APR};text-decoration-thickness:5px">النكهة</u> سبب الاختيار، لأن كل طبق يُبنى من مكوّنات طازجة وتتبيلات مدروسة وتوازن غذائي مُعلَن.</p></div>
<div class="abs" style="left:110px;top:180px;width:560px"><div class="eyebrow">VALUE PROPOSITION</div><div class="serif" style="font-size:80px;line-height:1.02;margin:18px 0">Healthy<br>you can <em style="color:{AUB};background:{LIME};padding:0 10px;font-style:italic">crave.</em></div><div class="h-ar" style="font-size:34px;direction:rtl;text-align:left">صحي… تشتهيه.</div></div>
<div class="abs rtl" style="right:110px;top:560px;width:1380px"><div class="eyebrow" style="direction:ltr;text-align:right">REASONS TO BELIEVE · أسباب التصديق</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:18px;direction:rtl">
{''.join(f'<div style="background:{IVORY};border-radius:10px;padding:22px"><div style="width:44px;height:44px;color:{AUB}">{A2.icon_inline(i)}</div><div style="font-size:22px;font-weight:700;margin-top:12px">{t}</div><div style="font-size:17px;opacity:.75;margin-top:4px;line-height:1.5">{d}</div></div>' for i,t,d in [('leaf','طزاجة يومية','مكوّنات تُجهَّز يوميًا ولا تُجمَّد.'),('flame','تتبيلات صنع داخلي','صلصات وتتبيلات تميّز كل طبق.'),('check','شفافية غذائية','سعرات وبروتين على كل صنف.'),('spark','منيو يتجدد','أصناف موسمية يطوّرها الشيف.')])}</div></div>
<div class="note" style="left:110px;bottom:40px;font-size:14px;opacity:.55">* أسباب التصديق افتراضات مقترحة، تُؤكَّد مع فريق التشغيل قبل اعتمادها في الاتصال.</div>'''))
# Audiences
def persona(x,name,role,bg,fg,stats,need,barrier,i):
    return f'''<div class="card ar" style="left:{x}px;top:170px;width:440px;height:560px;background:{bg};color:{fg};padding:26px">
<div style="display:flex;gap:16px;align-items:center;direction:rtl"><div style="width:84px;height:84px;border-radius:50%;overflow:hidden;flex:none;background:{fg}22">{bowl(i,84,None,fg,bg)}</div><div><div style="font-size:30px;font-weight:700">{name}</div><div style="font-size:17px;opacity:.8">{role}</div></div></div>
<div style="margin-top:22px;font-size:19px;line-height:1.7"><b>ما يريده:</b> {need}</div><div style="margin-top:14px;font-size:19px;line-height:1.7"><b>ما يمنعه:</b> {barrier}</div>
<div style="margin-top:20px;display:flex;flex-wrap:wrap;gap:8px;direction:rtl">{''.join(f'<span class="pill" style="font-family:IBM Plex Sans Arabic;letter-spacing:0;font-size:15px">{s}</span>' for s in stats)}</div></div>'''
P.append(page(IVORY,hdr('1.3','Audience','الجمهور','STRATEGY')+
 persona(1050,'لين، 28','مسوّقة في شركة ناشئة',AUB,IVORY,['غداء سريع','تهتم بالشكل','تشارك على الستوري'],'أكل صحي ولذيذ وسريع، وعلبة تستحق الصورة.','سئمت من «الأكل الصحي المسلوق» ومن الصحون المتشابهة.',1)+
 persona(580,'عمر، 35','مهندس ورياضي',LIME,AUB,['يتتبع البروتين','توصيل 3 مرات','حصص كبيرة'],'بروتين عالٍ بنكهة حقيقية، وأرقام غذائية واضحة.','الخيارات الصحية صغيرة وباهتة وغالية.',2)+
 persona(110,'سارة، 38','أمّ لطفلين',  '#fff',AUB,['وجبات عائلية','تقرأ المكوّنات','تقدّر الثقة'],'أطباق صحية يقبلها الأطفال، ومكوّنات معلنة وآمنة.','لا تثق بالمطاعم «الصحية» ذات المكوّنات الغامضة.',3)+
 f'<div class="note" style="left:110px;bottom:34px;font-size:14px;opacity:.55">Proto-personas — فرضيات أولية تُختبر ببحث ميداني (10–15 مقابلة) قبل الإطلاق.</div>'))
# Landscape
def dot(x,y,t,sz,bg,fg,b=False):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:translate(-50%,-50%);width:{sz}px;height:{sz}px;border-radius:50%;background:{bg};color:{fg};display:flex;align-items:center;justify-content:center;text-align:center;font-family:IBM Plex Sans Arabic;font-weight:700;font-size:{18 if not b else 22}px;line-height:1.3;padding:12px;{"box-shadow:0 0 0 10px "+LIME+"66;" if b else ""}">{t}</div>'
P.append(page('#fff',hdr('1.4','Competitive landscape','خريطة المنافسة','STRATEGY')+
 f'''<div class="abs" style="left:110px;top:170px;width:900px;height:640px;background:{IVORY};border-radius:10px">
<div class="abs" style="left:450px;top:0;bottom:0;width:2px;background:{AUB}22"></div><div class="abs" style="top:320px;left:0;right:0;height:2px;background:{AUB}22"></div>
<div class="abs eyebrow" style="left:14px;top:14px">PREMIUM · MODERN</div><div class="abs eyebrow" style="left:14px;bottom:14px">BASIC · UTILITARIAN</div>
<div class="abs eyebrow" style="left:14px;top:300px;transform-origin:left;">◄ FUNCTION-LED</div><div class="abs eyebrow" style="right:14px;top:300px">FLAVOUR-LED ►</div>
{dot(240,470,'سلاسل السلطات والدايت',150,'#fff',AUB)}{dot(240,170,'كافيهات صحية عضوية',150,'#fff',AUB)}{dot(650,490,'وجبات سريعة تقليدية',150,'#fff',AUB)}{dot(700,160,'ذا منيو',190,AUB,LIME,True)}</div>
<div class="abs rtl" style="right:110px;top:180px;width:430px"><div class="eyebrow" style="direction:ltr;text-align:right">THE WHITE SPACE</div><h3 style="font-size:34px;margin:14px 0">المساحة الفارغة</h3>
<p style="font-size:22px;line-height:1.8;margin:0">الصحي غالبًا إما «وظيفي» بلا نكهة، أو «أنيق» بلا شخصية. السريع غالبًا لذيذ لكنه غير صحي. المساحة المتروكة: <b>أكل صحي، عصري، تقوده النكهة</b>.</p>
<div style="margin-top:26px;background:{LIME};border-radius:10px;padding:20px;font-size:20px;font-weight:700;line-height:1.6">نلعب في الزاوية التي لا يشغلها أحد: صحي + شهي + مميَّز بصريًا.</div></div>
<div class="note" style="left:110px;bottom:30px;font-size:14px;opacity:.55">Category archetypes, not named competitors — to be mapped against actual local players.</div>'''))
# Personality
def slider(l_ar,r_ar,v):
    return f'<div style="margin:18px 0;direction:rtl"><div style="display:flex;justify-content:space-between;font-size:20px;font-weight:700"><span>{l_ar}</span><span>{r_ar}</span></div><div style="position:relative;height:10px;background:#ffffff33;border-radius:6px;margin-top:10px"><div style="position:absolute;right:0;top:0;bottom:0;width:{100-v}%;background:transparent"></div><div style="position:absolute;top:-8px;left:{v}%;width:26px;height:26px;border-radius:50%;background:{AUB};transform:translateX(-50%);box-shadow:0 0 0 6px {LIME}"></div></div></div>'
P.append(page(AUB,hdr('1.5','Personality & archetype','الشخصية','STRATEGY')+
 f'''<div class="abs" style="left:110px;top:170px;width:600px;color:{IVORY}"><div class="eyebrow" style="color:{IVORY}">ARCHETYPE</div><div class="serif" style="font-size:96px;line-height:1;margin:18px 0">The Generous Creator</div><div class="h-ar" style="font-size:44px;direction:rtl;text-align:left;color:{LIME}">المبدع الكريم</div>
<p style="font-size:21px;line-height:1.7;opacity:.85;margin-top:26px;max-width:520px">يبتكر بجرأة ويقدّم بسخاء. يحب الطعام ويحترم الجسد. واثق دون تعالٍ، ومرح دون استخفاف.</p></div>
<div class="abs rtl" style="right:110px;top:190px;width:640px;color:{IVORY}">{slider('جريء','هادئ',22)}{slider('مرح','رصين',32)}{slider('عصري','كلاسيكي',20)}{slider('دافئ','بارد',25)}{slider('قريب','فاخر',46)}</div>
<div class="abs" style="left:110px;bottom:70px;display:flex;gap:12px">{''.join(f'<span class="pill" style="color:{LIME};font-family:IBM Plex Sans Arabic;letter-spacing:0;font-size:20px">{t}</span>' for t in ['شهيّ','طازج','واثق','سخيّ','مرِح','واضح'])}</div>''',IVORY))
# Brand idea
P.append(page(LIME,hdr('1.6','Brand idea','الفكرة المركزية','STRATEGY')+
 f'''<div class="abs" style="left:110px;top:170px;width:1380px"><div class="eyebrow">THE BIG IDEA</div><div class="serif" style="font-size:190px;line-height:.92;margin:20px 0 10px;letter-spacing:-4px">Eat well.<br>Taste <em>more.</em></div></div>
<div class="abs rtl" style="right:110px;top:600px;width:620px"><div class="h-ar" style="font-size:60px;line-height:1.2">كُل صح. تذوّق أكثر.</div><p style="font-size:22px;line-height:1.7;margin:14px 0 0">نقلب المعادلة: الصحة لا تُطلب بدل الطعم، بل معه. كل نقطة تماس تقول: الطعم هو السبب، والصحة هي النتيجة.</p></div>
<div class="abs" style="left:110px;top:600px;width:620px;display:flex;flex-direction:column;gap:12px">{''.join(f'<div style="display:flex;gap:16px;align-items:center;font-size:22px;font-weight:700"><span style="width:44px;height:44px;border-radius:50%;background:{AUB};color:{LIME};display:flex;align-items:center;justify-content:center;font-family:Fraunces">{i}</span>{t}</div>' for i,t in [(1,'Flavour leads, health proves.'),(2,'Fresh, never preachy.'),(3,'Premium, yet generous.')])}</div>'''))
