const fs=require('fs'),path=require('path');let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
const sizes=JSON.parse(fs.readFileSync('sizes.json'));
(async()=>{const b=await pw.chromium.launch();
fs.mkdirSync('pkg/png',{recursive:true});fs.mkdirSync('pkg/pdf',{recursive:true});
for(const [k,[w,h]] of Object.entries(sizes)){
 const f=`the-menu_${k}`;const svg=fs.readFileSync(`pkg/svg/${f}.svg`,'utf8');
 const PW=2400,PH=Math.round(PW*h/w);
 const p=await b.newPage({viewport:{width:PW,height:PH}});
 await p.setContent(`<body style="margin:0;background:transparent"><div style="width:${PW}px;height:${PH}px">${svg.replace('<svg ','<svg width="100%" height="100%" ')}</div></body>`);
 try{await p.screenshot({path:`pkg/png/${f}.png`,omitBackground:true});}catch(e){console.log("png fail",f,e.message.split("\n")[0]);}
 if(!k.startsWith('logo-wordmark')||true){const pp=await b.newPage();await pp.setContent(`<style>@page{size:${w}px ${h}px;margin:0}body{margin:0}</style>${svg.replace('<svg ','<svg width="'+w+'" height="'+h+'" ')}`);
  await pp.pdf({path:`pkg/pdf/${f}.pdf`,width:w+'px',height:h+'px',printBackground:true,pageRanges:'1'});await pp.close();}
 await p.close();}
await b.close();})();
