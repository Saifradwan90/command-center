from mockbook import *
import re,os,json
root='pkg3';[os.makedirs(f'{root}/{d}',exist_ok=True) for d in ('svg','png')]
syms=re.search(r'<defs>(.*)</defs>',SYM,re.S).group(1);defs=re.search(r'<defs>(.*)</defs>',DEFS,re.S).group(1)
def standalone(svg):
    m=re.match(r'<svg viewBox="([^"]+)" style="[^"]*">',svg)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+m.group(1)+'"><defs>'+syms+defs+'</defs>'+svg[m.end():]
extra=[('hot-cup-ivory',cup_hot()),('hot-cup-aubergine',cup_hot(AUB,LIME,LIME,AUB,IVORY)),('hot-cup-lime',cup_hot(LIME,AUB,AUB,LIME,AUB)),('cold-cup-lime',cup_cold()),('cold-cup-apricot',cup_cold(APR,5,LIME)),('paper-bowl-aubergine',bowl_paper()),('paper-bowl-lime',bowl_paper(LIME,AUB,AUB,3,AUB)),('shopping-bag-aubergine',bag_shop()),('shopping-bag-lime',bag_shop(LIME,AUB,AUB,w=220,h=250,gus=80,py=70)),('shopping-bag-ivory',bag_shop(IVORY,AUB,AUB,w=200,h=230,gus=70,py=60)),('sauce-cup-aubergine',sauce()),('sauce-cup-lime',sauce(LIME,AUB)),('sauce-cup-ivory',sauce(IVORY,AUB)),('dessert-jar-a',jar()),('dessert-jar-b',jar((APR,LIME,IVORY,AUB))),('tee-aubergine',tee()),('tee-lime',tee(LIME,AUB)),('meal-set-flatlay',flatlay())]
base=[(f'{n}-{t.lower().replace(" ","-").replace("+","").replace("--","-")}',svg) for n,t,svg,w in idx]
allobj=base+[(f'x-{n}',s2) for n,s2 in extra]
names=[]
for n,svg in allobj:
    open(f'{root}/svg/the-menu_mockup_{n}.svg','w').write(standalone(svg));names.append(n)
json.dump(names,open('mk/names.json','w'));print(len(names))
