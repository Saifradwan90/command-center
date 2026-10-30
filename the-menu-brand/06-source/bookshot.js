let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
const path=require('path');
(async()=>{const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:1600,height:900}});
await p.goto('file://'+path.resolve('book.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const n=await p.locator('.page').count();
for(let i=0;i<n;i++){await p.locator('.page').nth(i).screenshot({path:`pv/p${String(i+1).padStart(2,'0')}.png`});}
if(process.argv[2]==='pdf')await p.pdf({path:'pkg/The-Menu_Brand-Guidelines.pdf',width:'1600px',height:'900px',printBackground:true});
await b.close();console.log(n);})();
