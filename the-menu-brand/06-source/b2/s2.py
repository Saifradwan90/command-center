from common import *
P=[]
P.append(divider('02','Verbal identity','الهوية اللفظية',LIME,AUB,AUB))
# voice principles
vp=[('واثق لا متعالٍ','Confident, never snobby','نتكلم كمن يعرف الطعم، لا كمن يحاضر في الصحة.'),('شهيّ لا مُبالغ','Appetising, never loud','نصف بالحواس: مقرمش، مدخّن، حامضي، كريمي.'),('واضح ومختصر','Clear & short','جملة واحدة تكفي. الأرقام عند الحاجة.'),('دافئ وخفيف الظل','Warm & playful','ابتسامة في المنتصف، دون سخرية من أحد.'),('صادق في الصحة','Honest about health','لا وعود طبية، لا «سمّ» ولا «ديتوكس».')]
cards=''
for i,(a,e,d) in enumerate(vp):
    x=110+(i%3)*465;y=170+(i//3)*270;bg=[AUB,LIME,'#fff','#fff',AUB][i];fg=[IVORY,AUB,AUB,AUB,LIME][i]
    cards+=f'<div class="card ar" style="left:{x}px;top:{y}px;width:445px;height:250px;background:{bg};color:{fg}"><div class="eyebrow" style="direction:ltr;text-align:right;color:{fg}">0{i+1} · {e}</div><h3 style="margin-top:12px">{a}</h3><p>{d}</p></div>'
dd=f'''<div class="card ar" style="left:{110+2*465}px;top:440px;width:445px;height:250px;background:{AUB};color:{IVORY}"><div class="eyebrow" style="direction:ltr;text-align:right;color:{IVORY}">DO / DON’T</div><p style="margin-top:12px;color:{LIME}">✓ وعاء الباذنجان المشوي — 480 سعرة، صفر تنازل.</p><p style="margin-top:12px;opacity:.7;text-decoration:line-through">✕ سعرات أقل! ابدأ حميتك الآن!</p></div>'''
P.append(page(IVORY,hdr('2.1','Voice principles','مبادئ الصوت','VERBAL')+cards+dd+f'<div class="rtl abs" style="right:110px;top:730px;width:1380px;font-size:21px;line-height:1.7;opacity:.85"><b>صيغة الكتابة:</b> عربية بيضاء قريبة من اللهجة المحكية دون إسفاف، مع جمل قصيرة وأفعال أمر محبّبة (كُل، ذُق، جرّب). الإنجليزية للأسماء والعبارة الأساسية فقط.</div>'))
# tone by context
rows=[('المنيو','Menu','وصفي وحسّي','«باذنجان مشوي على الفحم، طحينة بالليمون، رمان مقرمش.»'),('السوشيال','Social','مرح وسريع','«الباذنجان وصل… والتوقعات ارتفعت. 🍆»'),('التغليف','Packaging','قصير وذكي','«افتح… وتذوّق.»'),('خدمة العملاء','Support','هادئ ومطمئن','«نعتذر عن التأخير، وجبتك في الطريق وعلينا مشروب.»'),('الواجهة والمطبوعات','Print','واثق وموجز','«كُل صح. تذوّق أكثر.»')]
tr=''.join(f'<tr><td style="width:170px;font-weight:700;font-family:IBM Plex Sans Arabic;font-size:21px">{a}<div class="small" style="font-family:DM Sans;font-size:13px;letter-spacing:2px">{e}</div></td><td style="width:200px;font-size:20px"><span class="pill" style="font-family:IBM Plex Sans Arabic;letter-spacing:0">{t}</span></td><td style="font-size:22px;line-height:1.7">{ex}</td></tr>' for a,e,t,ex in rows)
P.append(page('#fff',hdr('2.2','Tone by context','النبرة حسب السياق','VERBAL')+f'<div class="abs rtl" style="right:110px;top:170px;width:1380px"><table class="rtl"><thead><tr><th>السياق</th><th>النبرة</th><th>مثال</th></tr></thead><tbody>{tr}</tbody></table></div>'))
# tagline system
tl=[('Eat well. Taste more.','كُل صح. تذوّق أكثر.','MASTER'),('Flavour is the first ingredient.','النكهة أول المكوّنات.','PRODUCT'),('Healthy, with a plot twist.','صحي… بمفاجأة.','CAMPAIGN'),('Fresh by day. Crave by night.','طازج نهارًا. مُشتهى ليلًا.','CAMPAIGN'),('Read the menu. Taste the rest.','اقرأ المنيو… وذُق الباقي.','OPENING'),('Good for you. Great for you.','لك وبنكهتك.','LOYALTY')]
tt=''
for i,(e,a,k) in enumerate(tl):
    big=i==0
    x=110 if big else 110+((i-1)%2)*460;y=170 if big else 170+((i-1)//2)*220;w=910 if big else 450;h=200 if big else 200
    if big:tt+=f'<div class="card" style="left:110px;top:170px;width:{w}px;height:{300}px;background:{AUB};color:{IVORY}"><div class="eyebrow" style="color:{LIME}">{k}</div><div class="serif" style="font-size:78px;line-height:1.05;margin-top:12px">{e}</div><div class="h-ar" style="font-size:44px;direction:rtl;text-align:left;color:{LIME};margin-top:16px">{a}</div></div>'
    else:
        y=500+((i-1)//3)*0;x=110+(i-1)*(300+8) if i<=3 else 0
tt=tt[:tt.rfind('<div class="card"')] if False else tt
alts=''
for i,(e,a,k) in enumerate(tl[1:]):
    x=110+(i%3)*310 if False else 0
alt=''.join(f'<div class="card" style="left:{110+(i%3)*465}px;top:{500+(i//3)*150}px;width:445px;height:135px;background:{[LIME,"#fff"][i%2]};border:1px solid #0001;padding:20px 24px"><div class="eyebrow">{k}</div><div class="serif" style="font-size:25px;margin-top:6px;line-height:1.15">{e}</div><div class="h-ar" style="font-size:22px;direction:rtl;text-align:right;margin-top:4px">{a}</div></div>' for i,(e,a,k) in enumerate(tl[1:]))
P.append(page(IVORY,hdr('2.3','Tagline system','منظومة العبارات','VERBAL')+tt+alt+
 f'<div class="abs rtl" style="right:110px;top:170px;width:440px;font-size:21px;line-height:1.75"><div class="eyebrow" style="direction:ltr;text-align:right">HOW TO USE</div><p style="margin:14px 0"><b>العبارة الأم</b> ترافق الشعار دائمًا.<br><b>عبارات الحملات</b> تُستخدم بدل الأم في الإعلانات فقط، لمدة محدودة.<br><b>القاعدة:</b> لا تُركَّب عبارتان معًا.</p></div>'))
# naming system
P.append(page('#fff',hdr('2.4','Menu naming system','نظام تسمية الأصناف','VERBAL')+f'''
<div class="abs" style="left:110px;top:170px;width:620px"><div class="eyebrow">FORMULA</div><div style="margin-top:16px;display:flex;flex-direction:column;gap:10px">{''.join(f'<div style="background:{c};color:{f};border-radius:10px;padding:18px 24px;font-size:24px;font-weight:700">{t}</div>' for t,c,f in [('① طريقة الطهي · Charred',AUB,IVORY),('② المكوّن البطل · Aubergine',LIME,AUB),('③ لمسة النكهة · Lime & Tahini','#F4EFE6',AUB)])}</div>
<div style="margin-top:22px;font-size:20px;line-height:1.6;opacity:.85">مثال: <b>Charred Aubergine Bowl</b> — وعاء الباذنجان المشوي بالليمون والطحينة.</div></div>
<div class="abs rtl" style="right:110px;top:170px;width:700px"><div class="eyebrow" style="direction:ltr;text-align:right">MENU STRUCTURE · هيكل المنيو</div>
<table class="rtl" style="margin-top:12px"><tbody>{''.join(f'<tr><td style="width:60px"><span style="display:block;width:38px;height:38px">{A2.icon_inline(i)}</span></td><td style="font-size:24px;font-weight:700;width:150px">{a}</td><td style="font-family:DM Sans;direction:ltr;opacity:.6;width:120px">{e}</td><td style="font-size:18px;opacity:.8">{d}</td></tr>' for i,a,e,d in [('bowl','الأوعية','Bowls','الوجبات الرئيسية'),('leaf','الخُضر','Greens','سلطات بشخصية'),('flame','الراب','Wraps','لفائف مشوية'),('sprout','الجانبية','Sides','مقرمشات وإضافات'),('cup','المشروبات','Sips','عصائر وشاي بارد'),('heart','الحلوى','Sweet','حلويات خفيفة')])}</tbody></table></div>
<div class="note" style="left:110px;bottom:40px;width:1380px;font-size:17px">وسوم غذائية موحّدة بأيقونات: <b>High-protein · Plant-based · Gluten-aware · Spicy</b> — مع السعرات والبروتين على كل صنف.</div>'''))
# copy examples
ex=[('Instagram','الباذنجان وصل… والتوقعات ارتفعت 🍆\nوعاء مشوي على الفحم، طحينة بالليمون. 480 سعرة، 0 تنازل.','#fff'),('Delivery box','افتح… وتذوّق.\nSorry, no fork-pairing required — الطعم يكفي.','#D8E457'),('Napkin','امسح بكل حب 💚\nWipe with love.','#F4EFE6'),('WhatsApp confirm','تم استلام طلبك ✅\nنجهّز وعاءك الآن — يوصلك خلال ٢٥ دقيقة.\nThe Menu','#fff'),('Loyalty','كل ٩ وجبات… العاشرة علينا.\nTaste more, pay less.',AUB),('Window decal','Healthy, with a plot twist.\nصحي… بمفاجأة.',AUB)]
cc=''.join(f'<div class="card rtl" style="position:relative;background:{bg};color:{IVORY if bg==AUB else AUB};height:300px;border:1px solid #0001"><div class="eyebrow" style="direction:ltr;text-align:right;color:inherit">{n}</div><div style="margin-top:16px;font-size:23px;line-height:1.75;white-space:pre-line;font-weight:600">{t}</div></div>' for n,t,bg in ex)
P.append(page(IVORY,hdr('2.5','Copy in action','نصوص جاهزة للاستخدام','VERBAL')+f'<div class="abs" style="left:110px;top:170px;width:1380px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px">{cc}</div>'))
