from common import *
import s1,s2,s3,s4,s5
secs=[('01','Strategy','الاستراتيجية',s1.P,['Foundation','Positioning','Audience','Competitive landscape','Personality','Brand idea']),
('02','Verbal identity','الهوية اللفظية',s2.P,['Voice principles','Tone by context','Tagline system','Menu naming','Copy in action']),
('03','Visual identity','الهوية البصرية',s3.P,['Logo & anatomy','Clear space','Logo suite','Arabic lockups','Colour & pairings','Typography','Shape language','Posters','Icons','Illustration','Motion','Misuse']),
('04','Applications','التطبيقات',s4.P,['Stationery','Menu','Packaging','Uniform','Signage','Digital','Loyalty']),
('05','Launch & governance','الإطلاق والحوكمة',s5.P[:-1],['Rollout','Campaign','KPIs','Handover'])]
cover=page(AUB,f'''<div class="abs" style="right:-120px;bottom:-250px;width:1000px;color:{LIME}">{lk(LIME,'mg')}</div><div class="abs" style="left:110px;top:230px;width:760px">{lk(IVORY,'lk')}</div>
<div class="meta" style="left:110px;top:90px;color:{IVORY}">BRAND BOOK · v2.0</div><div class="meta" style="left:110px;bottom:110px;color:{IVORY}">Complete brand identity system</div>
<div class="abs" style="left:110px;bottom:70px;font-family:'IBM Plex Sans Arabic';font-weight:600;font-size:26px;color:{IVORY};opacity:.7;direction:rtl">دليل الهوية المتكامل</div>''',IVORY)
start=3;items='';n=start
for num,en,ar_,pgs,subs in secs:
    items+=f'<div style="display:flex;align-items:baseline;gap:18px;border-bottom:2px solid {AUB};padding:16px 0"><span class="serif" style="font-size:44px;width:80px;color:{AUB}">{num}</span><span class="serif" style="font-size:44px;flex:1">{en}</span><span class="h-ar" style="font-size:32px">{ar_}</span><span style="font-size:20px;font-weight:800;width:60px;text-align:right">{n}</span></div><div style="padding:8px 0 4px 98px;font-size:15px;opacity:.6;letter-spacing:.5px">{" · ".join(subs)}</div>'
    n+=len(pgs)
toc=page(IVORY,hdr('','Contents','المحتويات')+f'<div class="abs" style="left:110px;top:170px;width:1380px">{items}</div>')
pages=[cover,toc]+s1.P+s2.P+s3.P+s4.P+s5.P
print(build(pages,'book2.html'),'pages; last section starts at',n)
