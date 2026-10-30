from mock import *
from obj1 import *
from obj2 import *
from obj3 import *
from obj4 import *
import obj1,obj2,obj3,obj4
STONE='radial-gradient(ellipse at 50% 38%,#F4EEE1 0%,#E6DDCB 62%,#D9CFBA 100%)'
def put(svg,l,t,w,rot=0,z=1):
    return f'<div style="position:absolute;left:{l}px;top:{t}px;width:{w}px;transform:rotate({rot}deg);z-index:{z}">{svg}</div>'
def chip(l,t,n,title,sub,fg=AUB):
    return f'<div style="position:absolute;left:{l}px;top:{t}px;color:{fg};max-width:360px"><div style="display:flex;gap:10px;align-items:center"><span style="width:26px;height:26px;border-radius:50%;background:{fg};color:#F4EEE1;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px">{n}</span><b style="font-size:19px">{title}</b></div><div style="font-size:14px;opacity:.7;margin-top:6px;line-height:1.5">{sub}</div></div>'
def mpage(bg,body,n,title,ar_,fg=AUB):
    h=hdr(n,title,ar_,'MOCKUPS')
    if fg!=AUB:h=h.replace('<div class="hdr">',f'<div class="hdr" style="color:{fg}">')
    return page(bg,h+body,fg)
def floorfade(color='#00000010'):return f'<div style="position:absolute;left:0;right:0;bottom:0;height:170px;background:linear-gradient(180deg,transparent,#00000014)"></div>'
P=[]
# cover
P.append(page(AUB,f'''<div style="position:absolute;right:-160px;bottom:-260px;width:1000px;color:{LIME};opacity:.2">{lk(LIME,'mg')}</div>
<div class="meta" style="left:110px;top:90px;color:{IVORY}">PACKAGING &amp; RESTAURANT MOCKUPS · v1.0</div>
<div style="position:absolute;left:110px;top:240px;width:600px;color:{IVORY}">{lk(IVORY,'lk')}<div class="serif" style="font-size:60px;line-height:1.05;margin-top:50px">Every touchpoint,<br>one brand.</div><div class="h-ar" style="font-size:34px;direction:rtl;text-align:left;margin-top:16px;color:{LIME}">كل ما يخص المطعم… بموكاب مرتّب</div></div>
{put(clamshell(),700,430,560)}{put(bag_shop(AUB,IVORY,LIME,w=240,h=290,gus=90),1090,150,420,0,2)}{put(cup_hot(),870,110,210,0,1)}{put(cup_cold(),1330,500,200,0,3)}''',IVORY))
# index
def thumb(n,t,svg,w):
    return f'<div style="background:#fff;border-radius:10px;height:150px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center"><div class="th" style="width:78%;height:112px;display:flex;align-items:center;justify-content:center">{svg}</div><div style="position:absolute;left:10px;bottom:7px;font-size:12px;font-weight:700"><span style="opacity:.45">{n}</span> {t}</div></div>'
idx=[('01','Clamshell box',clamshell(),460),('02','Meal box',meal_box(),460),('03','Window box',window_box(),460),('04','Paper bowl',bowl_paper(),460),('05','PET bowl',bowl_pet(),460),('06','Wrap',wrap_sandwich(),460),('07','Liner paper',paper_sheet(),340),('08','Shopping bag',bag_shop(w=200,h=240,gus=70),250),('09','SOS bag',bag_sos(),230),('10','Hot cup',cup_hot(),170),('11','Cold cup',cup_cold(),170),('12','Bottle',bottle(),110),('13','Sauce cup',sauce(),230),('14','Dessert jar',jar(),150),('15','Cutlery',cutlery_set(),460),('16','Napkin',napkin(),300),('17','Stickers',stickers(),420),('18','Backpack',backpack(),360),('19','Delivery bag',insulated_bag(),420),('20','Receipt',receipt(),150),('21','POS',pos(),330),('22','Apron',apron(),170),('23','Cap',cap(),260),('24','Tee',tee(),170),('25','Neon',neon(),420),('26','Window',window(),420),('27','Floor',obj4.floor(),420)]
cells=''.join(thumb(*i) for i in idx)
P.append(mpage('#fff',f'<div class="grid" style="left:110px;top:150px;width:1380px;grid-template-columns:repeat(7,1fr);grid-auto-rows:150px;gap:10px">{cells}</div>','0.1','The full system · 27 items','المنظومة الكاملة'))
# flat lay
P.append(page(LIME,put(flatlay(),0,0,1600)+f'<div style="position:absolute;left:110px;top:70px;font-family:Fraunces;font-weight:600;font-size:34px;color:{AUB}">The meal set</div><div style="position:absolute;left:110px;top:112px;font-size:15px;color:{AUB};opacity:.7">Tray · liner · bowl · cup · sleeve · cutlery · seal</div>'))
# food boxes
P.append(mpage(STONE,put(clamshell(),90,200,560)+put(meal_box(),640,170,500)+put(window_box(),1090,230,420)+chip(110,640,'01','Clamshell box','Lime board · 230 × 140 × 70 mm · aubergine band + cropped m · matte aqueous varnish')+chip(640,640,'02','Meal box','Aubergine board · 200 × 140 × 70 mm · lime kcal line · compostable')+chip(1090,640,'03','Window salad box','Ivory board · die-cut arch window (PET-free film) · lime lid'),'1','Food boxes','علب الطعام'))
# bowls
P.append(mpage(STONE,put(bowl_paper(),90,200,520)+put(bowl_pet(),610,220,520)+put(bowl_paper(LIME,AUB,AUB,3,AUB),1020,200,480)+chip(110,640,'04','Paper bowl + dome lid','750 ml · aubergine paper · lime rim · rPET dome lid')+chip(640,640,'05','PET bowl + paper sleeve','500 ml clear rPET · lime wrap sleeve (recyclable)')+chip(1090,640,'06','Lime paper bowl','Alt. colourway for vegan / seasonal bowls'),'2','Bowls','الأوعية'))
# sandwich
P.append(mpage(STONE,put(paper_sheet(-5),100,160,470)+put(paper_sheet(4,AUB,LIME,420,300,True),210,400,430,0,2)+put(wrap_sandwich(),680,200,620)+put(bag_sos(),1220,190,330)+chip(110,740,'07','Greaseproof sheets','35 × 35 cm · 40 gsm · ivory + lime · food-safe ink')+chip(680,640,'08','Wrap in print paper','Twist-end wrap · aubergine m-pattern on lime')+chip(1230,640,'09','SOS bag','Folded top + “Sealed fresh” round seal'),'3','Sandwiches & wraps','الساندويش واللفائف'))
# bags
P.append(mpage(STONE,put(bag_shop(),80,120,480)+put(bag_shop(LIME,AUB,AUB,w=220,h=250,gus=80,py=70),560,260,380)+put(bag_shop(IVORY,AUB,AUB,w=200,h=230,gus=70,py=60),930,300,300)+put(bag_sos(),1220,230,300)+chip(110,740,'10','Large shopping bag','32 × 30 × 15 cm · aubergine kraft · twisted handle · cropped lime m')+chip(620,740,'11','Medium bag','Lime stock · aubergine ink')+chip(960,740,'12','Small bag','Ivory stock · pastry & sides'),'4','Bags','الأكياس'))
# cups
P.append(mpage(STONE,put(cup_hot(),90,200,230)+put(cup_hot(AUB,LIME,LIME,AUB,IVORY),330,200,230)+put(cup_hot(LIME,AUB,AUB,LIME,AUB),570,200,230)+put(cup_cold(),840,170,240)+put(cup_cold(APR,5,LIME),1060,170,240)+put(bottle(),1290,150,200)+chip(110,690,'13','Hot cups','8/12 oz · double-wall · 3 colourways')+chip(840,690,'14','Cold cups','16 oz rPET · dome lid · paper straw · round m sticker')+chip(1290,690,'15','Cold-pressed bottle','330 ml glass · ivory label'),'5','Cups & drinks','الأكواب والمشروبات'))
# extras
P.append(mpage(STONE,put(sauce(),90,250,300)+put(sauce(LIME,AUB),340,250,300)+put(sauce(IVORY,AUB),590,250,300)+put(jar(),960,180,230)+put(jar((APR,LIME,IVORY,AUB)),1200,180,230)+put(cutlery_set(),90,430,520)+put(napkin(),660,480,260)+chip(110,190,'16','Sauce cups','2 / 4 oz · 3 colours')+chip(980,560,'17','Dessert jars','180 ml · layered')+chip(110,760,'18','Cutlery kit','FSC wood · paper sleeve')+chip(670,760,'19','Napkin','2-ply · lime band + m'),'6','Sides & extras','الإضافات'))
# stickers
P.append(mpage(STONE,put(stickers(),290,170,1020)+chip(290,700,'20','Label & seal system','Round seals · order label (thermal) · tamper strip · nutrition panel · die-cut m'),'7','Stickers, seals & labels','الملصقات والأختام'))
# delivery
P.append(mpage(STONE,put(backpack(),90,180,520)+put(insulated_bag(),620,200,600)+put(bag_shop(AUB,IVORY,LIME,w=200,h=240,gus=70,py=80),1180,200,340)+chip(110,640,'21','Rider backpack','Lime EPS box · 45 L · reflective strip · aubergine base')+chip(640,640,'22','Insulated catering bag','Aubergine nylon · lime handles')+chip(1200,640,'23','Order bag','Sealed with round label + receipt'),'8','Delivery','التوصيل'))
# receipts & pos
loy=f'<div style="width:430px;height:260px;background:{LIME};border-radius:12px;box-shadow:0 22px 40px #0003;padding:22px;color:{AUB};position:relative"><div style="width:100px">{lk(AUB,"wm")}</div><div style="margin-top:14px;font-weight:800;font-size:18px">Every 9th bowl… the 10th is on us.</div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:16px;justify-items:center">'+''.join(f'<div style="width:42px;height:42px;border-radius:50%;border:2px dashed {AUB if i>=6 else "transparent"};background:{AUB if i<6 else "transparent"};display:flex;align-items:center;justify-content:center">'+(f'<div style="width:24px">{lk(LIME,"mg")}</div>' if i<6 else '')+'</div>' for i in range(10))+'</div></div>'
P.append(mpage(STONE,put(receipt(),110,150,300,-3)+put(receipt(180,300),420,260,220,4)+put(pos(),700,150,440)+f'<div style="position:absolute;left:700px;top:560px;transform:scale(.8);transform-origin:left top">{loy}</div>'+chip(110,720,'24','Receipt & order ticket','80 mm thermal · logo header + QR for loyalty stamp')+chip(1170,250,'25','POS / kiosk screen','Arch bowl tiles · lime action button')+chip(1090,600,'26','Loyalty card','10-stamp card + digital wallet'),'9','Receipts, POS & loyalty','الإيصالات ونقطة البيع'))
# staff
P.append(mpage(STONE,put(apron(),90,170,380)+put(cap(),470,190,400)+put(tee(),860,170,320)+put(tee(LIME,AUB),1160,170,320)+put(badge(),560,470,260)+chip(110,720,'27','Kitchen apron','Aubergine canvas · lime m base')+chip(560,700,'28','Cap & badge','Lime cap · aubergine badge')+chip(1000,700,'29','Team tees','Aubergine + lime colourways'),'10','Staff uniform','زي الفريق'))
# instore
P.append(mpage(STONE,put(neon(),90,170,640)+put(window(),770,170,720)+put(obj4.floor(),90,560,560)+chip(770,670,'30','Neon feature wall','Lime LED neon · aubergine wall')+chip(1010,670,'31','Window decal + hours','White cut vinyl + lime hours strip')+chip(1250,670,'32','Floor decal','Anti-slip · ‘Order here →’'),'11','In-store graphics','الديكور الداخلي'))
# specs
rows=[('Clamshell box','230×140×70 mm','Folding board 350 gsm','Offset 2 spot + matte AQ'),('Meal box','200×140×70 mm','Kraft-back board 300 gsm','Offset 2 spot + aqueous'),('Window box','230×140×70 mm','Board + PLA film window','Offset 2 spot'),('Paper bowl 750 ml','Ø150 mm','Paper + PE-free lining','Flexo 2 spot'),('PET bowl 500 ml','Ø140 mm','rPET + paper sleeve','Sleeve offset 2 spot'),('Wrap paper','350×350 mm','Greaseproof 40 gsm','Flexo 1–2 spot'),('Shopping bag L','320×300×150 mm','Kraft 120 gsm · twisted handle','Flexo 2 spot'),('SOS bag','140×80×250 mm','Kraft 70 gsm','Flexo 1–2 spot'),('Hot cup 12 oz','Ø90 mm','Double-wall board','Offset 2 spot'),('Cold cup 16 oz','Ø95 mm','rPET + dome lid','Sticker print'),('Sauce cup 2/4 oz','Ø60/75 mm','PP + lid','In-mould label'),('Receipt','80 mm','Thermal','1 colour (black)')]
tr=''.join(f'<tr><td style="font-weight:800;width:210px">{a}</td><td style="width:190px">{b}</td><td>{c}</td><td style="width:260px">{d}</td></tr>' for a,b,c,d in rows)
P.append(mpage('#fff',f'<div class="abs" style="left:110px;top:170px;width:1380px"><table><thead><tr><th>ITEM</th><th>SIZE</th><th>MATERIAL</th><th>PRINT</th></tr></thead><tbody>{tr}</tbody></table></div><div class="note" style="left:110px;bottom:36px;width:1380px;font-size:15px">Indicative sizes and materials — confirm with the packaging supplier. Pantone & varnish proofs required (lime prints duller in CMYK). Dielines to be built per supplier template.</div>','12','Spec sheet (indicative)','المواصفات'))
# colour logic
logic=[(LIME,AUB,'Lime = food','Boxes, bowls, wraps — anything that touches food.'),(AUB,IVORY,'Aubergine = premium & delivery','Bags, catering bags, cups, uniforms.'),('#fff',AUB,'Ivory = utility','Sleeves, labels, napkins, paper — quiet, clean surfaces.'),(APR,AUB,'Apricot = flavour flag','One-off promos, limited bowls, sauces.')]
lg=''.join(f'<div class="card" style="position:relative;background:{b};color:{f};height:300px;border:1px solid #0001"><h3 style="font-size:30px">{t}</h3><p>{d}</p></div>' for b,f,t,d in logic)
P.append(mpage(IVORY,f'<div class="abs" style="left:110px;top:180px;width:1380px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px">{lg}</div><div class="abs" style="left:110px;top:520px;width:1380px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px">'+''.join(f'<div style="background:#fff;border-radius:10px;padding:22px"><div class="eyebrow">{a}</div><div style="font-size:20px;font-weight:700;margin-top:8px;line-height:1.4">{b}</div></div>' for a,b in [('RULE 1','Crop the m on the base or the side — never behind the logo.'),('RULE 2','Logo on the biggest clear face; tagline only above 40 mm wide.'),('RULE 3','One colour block per item; max two inks + varnish.')])+'</div>','13','Colour logic & print rules','منطق الألوان والطباعة'))
# closing
P.append(page(AUB,f'<div style="position:absolute;left:110px;top:200px;width:720px">{lk(IVORY,"lk")}</div>'+put(clamshell(),820,230,520,0,2)+put(cup_cold(),1280,320,200,0,3)+put(bowl_paper(),780,470,420,0,1)+f'<div class="meta" style="left:110px;bottom:80px;color:{IVORY}">THE MENU · PACKAGING MOCKUPS v1.0</div>',IVORY))
html=f'<!doctype html><html><head><meta charset="utf-8"><title>The Menu — Packaging Mockups</title><style>{CSS}.th svg{{max-height:112px;width:auto!important;max-width:100%}}</style></head><body>{SYM}{DEFS}{"".join(P)}</body></html>'
open('mockbook.html','w').write(html);print(len(P),'pages',len(html)//1024,'KB')
