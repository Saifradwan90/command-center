let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
const path=require('path'),fs=require('fs');
(async()=>{const names=JSON.parse(fs.readFileSync('social.json'));const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:1200,height:2200}});
await p.goto('file://'+path.resolve('social.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
for(const n of names)await p.locator('#'+n).screenshot({path:`pkg2/png/the-menu_${n}.png`});await b.close();})();
