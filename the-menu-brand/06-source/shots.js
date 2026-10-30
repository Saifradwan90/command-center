let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
const path=require('path'),fs=require('fs');
(async()=>{const file=process.argv[2],outdir=process.argv[3];fs.mkdirSync(outdir,{recursive:true});
const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:1600,height:900}});
await p.goto('file://'+path.resolve(file));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
const n=await p.locator('.page').count();
for(let i=0;i<n;i++)await p.locator('.page').nth(i).screenshot({path:`${outdir}/p${String(i+1).padStart(2,'0')}.png`});
if(process.argv[4])await p.pdf({path:process.argv[4],width:'1600px',height:'900px',printBackground:true});
await b.close();console.log(n);})();
