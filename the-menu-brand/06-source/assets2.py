import math,random
AUB='#371C2B';LIME='#D8E457';IVORY='#F4EFE6';APR='#F2A65A'
ICONS={
'bowl':'<path d="M5 22h38c0 11-8.5 18-19 18S5 33 5 22z"/><path d="M15 43h18"/><path d="M14 16c0-4 3-7 7-7M26 14c0-3 2-5 5-5"/>',
'leaf':'<path d="M9 39C9 21 21 10 40 8c0 19-11 31-29 31z"/><path d="M9 39 29 19"/>',
'flame':'<path d="M24 5c2 8 13 12 13 25a13 13 0 0 1-26 0c0-6 3-10 6-13 0 4 2 6 4 6 0-6-2-11 3-18z"/>',
'lime':'<circle cx="24" cy="24" r="18"/><circle cx="24" cy="24" r="12.5"/><path d="M24 11.5v25M11.5 24h25M15 15l18 18M33 15 15 33"/>',
'bag':'<path d="M9 16h30l3 27H6z"/><path d="M17 16v-3a7 7 0 0 1 14 0v3"/>',
'scooter':'<circle cx="11" cy="34" r="5.5"/><circle cx="38" cy="34" r="5.5"/><path d="M16.5 34H29l6-17h6"/><path d="M29 34 22 19h-9"/>',
'clock':'<circle cx="24" cy="24" r="18"/><path d="M24 12v13l8 5"/>',
'pin':'<path d="M24 44S9 30 9 19.5a15 15 0 0 1 30 0C39 30 24 44 24 44z"/><circle cx="24" cy="19.5" r="5.5"/>',
'heart':'<path d="M24 41S5 29.5 5 17a9.5 9.5 0 0 1 19-3 9.5 9.5 0 0 1 19 3c0 12.500-19 24-19 24z"/>',
'spark':'<path d="M24 3c2 12.500 8.500 19 21 21-12.500 2-19 8.500-21 21-2-12.500-8.500-19-21-21C15.500 22 22 15.500 24 3z"/>',
'sprout':'<path d="M24 43V25"/><path d="M24 27c0-10-8-15-17-15 0 10 6 15 17 15z"/><path d="M24 23c0-8 6-13 17-13 0 10-6 13-17 13z"/>',
'cup':'<path d="M11 13h26l-3 30H14z"/><path d="M9 13h30"/><path d="M24 4v9"/><path d="M13 25h22"/>',
'cutlery':'<path d="M12 5v11a5 5 0 0 0 10 0V5M17 5v38"/><path d="M35 43V5c-6 4-8 12-8 21h8"/>',
'qr':'<rect x="6" y="6" width="14" height="14" rx="2"/><rect x="28" y="6" width="14" height="14" rx="2"/><rect x="6" y="28" width="14" height="14" rx="2"/><path d="M28 28h6v6h-6zM38 28h4M28 38h4M36 38h6v4"/>',
'check':'<circle cx="24" cy="24" r="18"/><path d="M15 25l7 7 12-14"/>',
'chat':'<path d="M7 9h34v24H23l-11 8v-8H7z"/><path d="M15 18h18M15 25h11"/>',
}
def icon_svg(name,color=AUB,sw=3.2,size=96):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'
def icon_inline(name,color='currentColor',sw=3.2):
    return f'<svg viewBox="0 0 48 48" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="width:100%;height:100%">{ICONS[name]}</svg>'
def bowl(seed=1,size=400,bg=None,rim=AUB,inner=IVORY,cols=None):
    c=size/2;R=size*.46;ri=R*.86;uid=f"b{seed}{int(size)}"
    pal=[(LIME,AUB),(APR,AUB),(AUB,LIME),(IVORY,APR)]
    rot=(seed*37)%90
    o=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
    if bg:o+=f'<rect width="{size}" height="{size}" fill="{bg}"/>'
    o+=f'<circle cx="{c}" cy="{c}" r="{R}" fill="{rim}"/><circle cx="{c}" cy="{c}" r="{ri}" fill="{inner}"/>'
    def pt(r,a):return c+r*math.cos(math.radians(a)),c+r*math.sin(math.radians(a))
    r0=R*.2;r1=ri*.94
    for i,(fill,ink) in enumerate(pal):
        a0=rot+i*90+3;a1=rot+(i+1)*90-3
        x0,y0=pt(r1,a0);x1,y1=pt(r1,a1);x2,y2=pt(r0,a1);x3,y3=pt(r0,a0)
        d=f'M{x0:.1f},{y0:.1f}A{r1:.1f},{r1:.1f} 0 0 1 {x1:.1f},{y1:.1f}L{x2:.1f},{y2:.1f}A{r0:.1f},{r0:.1f} 0 0 0 {x3:.1f},{y3:.1f}Z'
        o+=f'<clipPath id="{uid}{i}"><path d="{d}"/></clipPath><path d="{d}" fill="{fill}" {"stroke=%s stroke-width=1.5"%chr(34)+inner+chr(34) if fill==inner else ""}/>'
        am=rot+i*90+45;px,py=pt((r0+r1)/2,am)
        g=''
        if i==0:   # greens: leaves
            for k in range(-2,3):
                for m in range(-2,3):
                    x=px+k*size*.085+(m%2)*size*.04;y=py+m*size*.075
                    g+=f'<path d="M{x-size*.035:.1f},{y:.1f}Q{x:.1f},{y-size*.045:.1f} {x+size*.035:.1f},{y:.1f}Q{x:.1f},{y+size*.045:.1f} {x-size*.035:.1f},{y:.1f}Z" fill="{ink}" transform="rotate({(k*30+m*20)%90} {x:.1f} {y:.1f})"/>'
        if i==1:   # cubes
            for k in range(-2,3):
                for m in range(-2,3):
                    x=px+k*size*.075;y=py+m*size*.075
                    g+=f'<rect x="{x-size*.024:.1f}" y="{y-size*.024:.1f}" width="{size*.048:.1f}" height="{size*.048:.1f}" rx="{size*.014:.1f}" fill="{ink}" transform="rotate(20 {x:.1f} {y:.1f})"/>'
        if i==2:   # aubergine slices
            for k in range(-2,3):
                for m in range(-2,3):
                    x=px+k*size*.08+(m%2)*size*.04;y=py+m*size*.07
                    g+=f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{size*.03:.1f}" ry="{size*.018:.1f}" fill="{ink}" transform="rotate(-25 {x:.1f} {y:.1f})"/>'
        if i==3:   # chickpeas
            for k in range(-3,4):
                for m in range(-3,4):
                    x=px+k*size*.05+(m%2)*size*.025;y=py+m*size*.05
                    g+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size*.016:.1f}" fill="{ink}"/>'
        o+=f'<g clip-path="url(#{uid}{i})">{g}</g>'
    o+=f'<circle cx="{c}" cy="{c}" r="{r0*.98:.1f}" fill="{IVORY}"/><circle cx="{c}" cy="{c}" r="{r0*.55:.1f}" fill="{APR}"/>'
    return o+'</svg>'
if __name__=='__main__':
    html='<body style="margin:0;background:#F4EFE6;padding:20px;width:1500px;display:flex;flex-wrap:wrap;gap:16px">'
    for n in ICONS:html+=f'<div style="width:120px;height:120px;background:#fff;display:flex;align-items:center;justify-content:center">{icon_svg(n,AUB,3.2,84)}</div>'
    for s in (1,2,3):html+=f'<div style="width:300px">{bowl(s,300,LIME if s==1 else AUB if s==2 else APR,AUB if s!=2 else LIME)}</div>'
    open('ic.html','w').write(html+'</body>')
