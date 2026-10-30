const fs=require('fs');let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
(async()=>{const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:+process.argv[4]||1600,height:+process.argv[5]||900}});
await p.goto('file://'+require('path').resolve(process.argv[2]));await p.screenshot({path:process.argv[3]});await b.close();})();
