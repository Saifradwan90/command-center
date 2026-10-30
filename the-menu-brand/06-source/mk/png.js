let pw;try{pw=require('playwright')}catch(e){pw=require('/opt/node22/lib/node_modules/playwright')}
const fs=require('fs');
(async()=>{const names=JSON.parse(fs.readFileSync('mk/names.json'));const b=await pw.chromium.launch();const p=await b.newPage({viewport:{width:1600,height:1200}});
for(const n of names){const svg=fs.readFileSync(`pkg3/svg/the-menu_mockup_${n}.svg`,'utf8');
const vb=svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const w=1600,h=Math.round(1600*vb[2]/vb[1]);await p.setViewportSize({width:w,height:h});
await p.setContent(`<body style="margin:0;background:transparent"><div style="width:${w}px;height:${h}px">${svg.replace('<svg ','<svg width="100%" height="100%" style="overflow:visible" ')}</div></body>`);
await p.screenshot({path:`pkg3/png/the-menu_mockup_${n}.png`,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});}
await b.close();console.log('ok');})();
