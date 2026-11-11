from pathlib import Path
import math, random
import resvg_py
from PIL import Image

OUT=Path(__file__).parent
random.seed(24)
DEFS='''<defs>
<radialGradient id="space"><stop stop-color="#45216e"/><stop offset="1" stop-color="#101333"/></radialGradient>
<linearGradient id="gold" x2=".3" y2="1"><stop stop-color="#ffe796"/><stop offset=".55" stop-color="#ffbd49"/><stop offset="1" stop-color="#ec7354"/></linearGradient>
<linearGradient id="purple" x2=".8" y2="1"><stop stop-color="#b984f5"/><stop offset="1" stop-color="#6936af"/></linearGradient>
<linearGradient id="mint" x2="0" y2="1"><stop stop-color="#aff9d9"/><stop offset="1" stop-color="#44bdc6"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#b765df" stop-opacity=".4"/><stop offset="1" stop-color="#b765df" stop-opacity="0"/></radialGradient>
</defs>'''
def path(d,fill,extra=''): return f'<path d="{d}" fill="{fill}" {extra}/>'
def circle(x,y,r,c,extra=''): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {extra}/>'
def ellipse(x,y,rx,ry,c,extra=''): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" {extra}/>'
def text(x,y,s,size=20,c='#fff2d6',extra=''): return f'<text x="{x}" y="{y}" fill="{c}" font-family="Arial" font-size="{size}" {extra}>{s}</text>'
def group(id,body,transform=''): return f'<g id="{id}" transform="{transform}">{body}</g>'
def bg():
    s='<rect width="1280" height="720" fill="url(#space)"/>'
    for i in range(65):
        s+=circle(random.randrange(1280),random.randrange(720),random.choice([2,3,5,8]),random.choice(['#81539f','#53518c','#347285']), 'opacity=".28"')
    return s
def save(name,s):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">{DEFS}{s}</svg>'
    (OUT/f'{name}.svg').write_text(svg,encoding='utf-8')
    (OUT/f'{name}.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg))

blob='M-180,-65 C-210,-132 -136,-201 -69,-175 C-7,-225 92,-181 111,-135 C186,-151 229,-65 191,-9 C231,56 171,133 109,129 C67,190 -32,198 -74,149 C-151,180 -215,111 -191,57 C-236,22 -219,-38 -180,-65Z'
s=bg()+ellipse(620,365,440,320,'url(#halo)')
s+=text(65,67,'01  /  THẾ GIỚI VI MÔ',18,extra='letter-spacing="3"')
s+=text(65,113,'Một tế bào, cả một thế giới.',34,extra='font-weight="bold"')
cell=path(blob,'#753c90','stroke="#b065a9" stroke-width="8"')
cell+=path(blob,'url(#gold)','transform="scale(.92)"')
cell+=path('M-139,-110 C-89,-173 -11,-158 25,-157','none','stroke="#fff2ad" stroke-width="17" stroke-linecap="round"')
for x,y,a in [(-110,55,-30),(100,-80,25),(97,77,-20),(-46,121,14)]:
    cell+=group('organelle'+str(x),'<rect x="-25" y="-12" width="50" height="24" rx="12" fill="#de7660"/>'+path('M-13,0 Q-6,-12 0,0 T13,0','none','stroke="#ffca86" stroke-width="4"'),f'translate({x} {y}) rotate({a})')
for i in range(24):
    x,y=random.randint(-145,145),random.randint(30,125)
    cell+=circle(x,y,random.randint(2,5),'#f7e2a2','opacity=".7"')
cell+=group('nucleus',ellipse(39,44,65,59,'#874cb4')+ellipse(32,34,49,42,'url(#purple)')+ellipse(13,16,18,11,'#dcb2fa')+circle(53,54,15,'#643b93'))
face=''
for x in [-61,0]: face+=ellipse(x,-61,22,28,'#fff8df')+ellipse(x+7,-59,11,15,'#392d5b')+circle(x+10,-65,4,'white')
face+=path('M-67,-102 Q-52,-112 -39,-102 M-17,-105 Q0,-118 15,-104','none','stroke="#a05a56" stroke-width="7" stroke-linecap="round"')
face+=path('M-49,-18 Q-25,5 -7,-19','none','stroke="#623956" stroke-width="8" stroke-linecap="round"')
cell+=group('face',face)
s+=group('cell',cell,'translate(555 410) rotate(-8) scale(1.12)')
for j,(x,y,r) in enumerate([(959,275,50),(1030,467,28),(839,560,18)]):
    v=''
    for k in range(8):
        a=k*math.pi/4; X,Y=math.cos(a)*r*1.4,math.sin(a)*r*1.4
        v+=path(f'M0,0 L{X},{Y}','none','stroke="#54c9bd" stroke-width="9"')+circle(X,Y,7,'#9bf5c9')
    v+=circle(0,0,r,'#3caaa7')+circle(-5,-7,r*.75,'#7ce5c0')+circle(8,7,r*.25,'#378c99')
    s+=group('particle'+str(j),v,f'translate({x} {y})')
s+=text(67,674,'ART STUDY  /  01',14,'#b9a9d2',extra='letter-spacing="3"')
save('01-cell',s)

s=bg()+text(65,67,'02  /  MỘT CÁNH CỔNG NHỎ',18,extra='letter-spacing="3"')+text(65,113,'Đúng tín hiệu. Mở đúng cửa.',34,extra='font-weight="bold"')
s+=path('M0,463 L1280,314 L1280,720 L0,720Z','#f9ce80')
s+=path('M0,445 L1280,296 L1280,380 L0,529Z','#ad397a')
lip=''
for x in range(-30,1320,26):
    y=445-x*.1164
    lip+=path(f'M{x},{y+13} q-8,16 0,31 m8,-31 q-8,16 0,31','none','stroke="#ff9eb3" stroke-width="7" stroke-linecap="round"')
    lip+=circle(x+3,y,12,'#f96c9e')+circle(x,y-4,4,'#ffb1c5')+circle(x+3,y+70,12,'#ed628e')
s+=group('lipid-bilayer',lip)
gate=ellipse(0,0,90,90,'#532778')+path('M-28,-83 C-96,-94 -103,-4 -69,71 L-27,78 Q-54,0 -28,-83','#53c8aa')+path('M28,-83 C96,-94 103,-4 69,71 L27,78 Q54,0 28,-83','url(#mint)')
gate+=path('M-58,-59 Q-79,-8 -53,45','none','stroke="#aff6ce" stroke-width="7" stroke-linecap="round"')
s+=group('gate',gate,'translate(765 394) rotate(-7)')
arm=path('M585,375 L546,299 L604,233 L677,249','none','stroke="#228cb8" stroke-width="29" stroke-linejoin="round" stroke-linecap="round"')
for x,y in [(585,375),(546,299),(604,233),(677,249)]: arm+=circle(x,y,19,'#58d7e1')+circle(x-4,y-5,7,'#a8f5eb')
arm+=path('M676,248 L703,221 L735,235 M677,249 L693,279 L727,274','none','stroke="#59dce4" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"')
s+=group('protein',arm)
s+=circle(752,248,21,'#fff1a1')+circle(747,242,8,'white')
for x,y in [(387,259),(293,332),(981,180),(1048,265),(413,571),(1035,535)]:
    s+=group('molecule'+str(x),circle(-9,0,12,'#a888df')+circle(9,0,12,'#a888df')+circle(0,-13,12,'#cfb2f6'),f'translate({x} {y}) rotate(25)')
s+=text(70,213,'BÊN NGOÀI',15,'#ae9ccc',extra='letter-spacing="3"')+text(70,610,'BÊN TRONG',15,'#9d5966',extra='letter-spacing="3"')
s+=text(67,674,'ART STUDY  /  02 · CƠ CHẾ CÁCH ĐIỆU',14,'#9d5966',extra='letter-spacing="2"')
save('02-membrane',s)

s='<rect width="1280" height="720" fill="#fff1cf"/>'+circle(985,281,280,'#d4ead7')+circle(1150,90,145,'#c3e3d3')
s+=text(65,67,'03  /  CHUYỆN CỦA CON NGƯỜI',18,'#5b5073',extra='letter-spacing="3"')+text(65,113,'Tò mò là điểm bắt đầu.',34,'#373452',extra='font-weight="bold"')
s+='<rect x="65" y="197" width="430" height="322" rx="24" fill="#d1e4d5"/><rect x="82" y="213" width="396" height="289" rx="16" fill="#f8ffe6"/>'
for k in range(20):
    x=115+k*17; y=345; off=math.sin(k*.42)*67
    s+=path(f'M{x},{y+off} L{x},{y-off}','none','stroke="#8bcfc2" stroke-width="7"')
for phase,c in [(0,'#388fa0'),(math.pi,'#7e60b7')]:
    pts=[f'{115+i*3.4},{345+math.sin(i*.084+phase)*67}' for i in range(96)]
    s+=path('M'+' L'.join(pts),'none',f'stroke="{c}" stroke-width="9" stroke-linecap="round"')
s+=ellipse(851,655,208,24,'#e2cba9')
person=path('M-96,153 Q-150,182 -159,335 L155,335 Q144,191 86,151Z','#5c5795')
person+=path('M-86,149 L-24,169 L10,283 L40,169 L85,151 L117,335 L-119,335Z','#fffdf0')
person+=path('M-26,115 L-25,169 Q10,197 40,166 L40,113Z','#d2778e')
person+=path('M-28,160 L-66,150 L-85,205 L-46,218 L-57,249 L0,315Z','#d2e7df')+path('M39,161 L74,148 L92,204 L58,218 L67,247 L15,312Z','#e2eee0')
person+=path('M-121,180 Q-151,187 -179,238 L-265,195','none','stroke="#fffdf0" stroke-width="48" stroke-linecap="round"')
person+=path('M-266,196 L-286,178 M-269,198 L-303,193','none','stroke="#ed9ca6" stroke-width="22" stroke-linecap="round"')
person+=path('M105,185 Q147,217 131,271 L60,291','none','stroke="#f5f7e9" stroke-width="48" stroke-linecap="round"')
person+=group('head',ellipse(-1,18,88,104,'#3d365a')+ellipse(-73,51,18,23,'#df889c')+ellipse(77,51,18,23,'#e997a5')+path('M-69,-2 Q-66,-65 10,-64 Q77,-59 73,18 L66,77 Q49,123 9,129 Q-45,121 -63,75Z','#efa5ab')+path('M-76,23 Q-116,-46 -52,-81 Q-9,-125 43,-85 Q105,-80 88,-7 Q57,2 40,-34 Q-5,9 -53,-5 L-64,37Z','#393451')+path('M-66,-53 Q-15,-94 33,-68','none','stroke="#65547a" stroke-width="12" stroke-linecap="round"')+ellipse(-28,43,17,20,'#fff7dc')+ellipse(37,43,17,20,'#fff7dc')+ellipse(-33,44,8,12,'#393451')+ellipse(32,44,8,12,'#393451')+path('M-47,14 Q-30,4 -12,14 M24,9 Q40,0 55,12','none','stroke="#59405e" stroke-width="7" stroke-linecap="round"')+path('M8,42 L0,66 L15,66','none','stroke="#d67d90" stroke-width="6" stroke-linecap="round"')+path('M-13,86 Q9,106 32,84','#9c4c71')+path('M-9,87 L28,86 Q13,97 -9,87','#fff7df'))
person+='<rect x="-1" y="248" width="98" height="107" rx="9" fill="#3b7c8c" transform="rotate(-12 48 300)"/>'+path('M124,277 L74,296','none','stroke="#efa5ab" stroke-width="24" stroke-linecap="round"')
s+=group('scientist',person,'translate(885 298)')
s+=text(67,674,'ART STUDY  /  03',14,'#897c8c',extra='letter-spacing="3"')
save('03-scientist',s)
sheet=Image.new('RGB',(1280,2160))
for i,n in enumerate(['01-cell','02-membrane','03-scientist']):
    with Image.open(OUT/f'{n}.png') as im: sheet.paste(im,(0,i*720))
sheet.save(OUT/'preview.jpg',quality=95)
print('Created 3 layered SVGs, 3 PNGs and preview.jpg')
