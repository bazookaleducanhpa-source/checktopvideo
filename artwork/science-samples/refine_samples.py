"""Second art pass; preserves the first drawings for comparison."""
from pathlib import Path
import math, random
import xml.etree.ElementTree as ET
import resvg_py
from PIL import Image

ROOT=Path(__file__).parent
OUT=ROOT/'v2'
OUT.mkdir(exist_ok=True)
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
random.seed(73)
def el(s): return ET.fromstring(f'<g xmlns="{NS}">{s}</g>')
def add(node,s,index=None):
    g=el(s)
    if index is None: node.append(g)
    else: node.insert(index,g)
    return g
def find(root,id): return next(e for e in root.iter() if e.get('id')==id)
def p(d,c,extra=''): return f'<path d="{d}" fill="{c}" {extra}/>'
def c(x,y,r,col,extra=''): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" {extra}/>'

for name in ['01-cell','02-membrane','03-scientist']:
    root=ET.fromstring((ROOT/f'{name}.svg').read_text(encoding='utf-8'))
    defs=root.find(f'{{{NS}}}defs')
    add(defs,'''<linearGradient id="skin" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffd0b1"/><stop offset="1" stop-color="#db829f"/></linearGradient>
    <linearGradient id="interior" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffe6a3"/><stop offset="1" stop-color="#f0ab79"/></linearGradient>
    <linearGradient id="glass"><stop stop-color="#53dbc9" stop-opacity=".1"/><stop offset="1" stop-color="#53dbc9" stop-opacity=".5"/></linearGradient>
    <filter id="blur"><feGaussianBlur stdDeviation="9"/></filter>
    <radialGradient id="signal"><stop stop-color="#fffbd9"/><stop offset=".2" stop-color="#ffd96b" stop-opacity=".5"/><stop offset="1" stop-color="#ffd96b" stop-opacity="0"/></radialGradient>''')
    if name=='01-cell':
        # Large, low-contrast structures behind the focal character establish depth.
        backdrop=''
        for x,y,r in [(-60,335,175),(1190,665,176),(1125,53,110)]:
            backdrop+=c(x,y,r,'#312650')+c(x,y,r*.87,'#39315e')+c(x+20,y+10,r*.35,'#4a3c70')
            for a in range(0,360,40):
                X,Y=x+r*.68*math.cos(math.radians(a)),y+r*.68*math.sin(math.radians(a))
                backdrop+=c(X,Y,9,'#51436e')
        add(root,backdrop,2)
        cell=find(root,'cell')
        # A tapered shadow crescent adds volume without making all edges glow.
        add(cell,p('M175,-72 C200,-26 180,12 190,42 C168,111 132,112 101,114 C54,169 -15,177 -61,139 C-115,156 -166,119 -177,75 C-123,111 -95,80 -65,102 C-6,136 45,114 79,86 C119,93 141,36 144,5Z','#cf626e','opacity=".35"'),2)
        ribbons=''
        for i in range(4):
            ribbons+=p(f'M-137,{-55+i*12} C-112,{-76+i*12} -83,{-48+i*12} -99,{-28+i*12}','none','stroke="#ed8c60" stroke-width="6" stroke-linecap="round"')
        add(cell,ribbons,4)
        nuc=find(root,'nucleus')
        add(nuc,p('M-2,52 C17,30 16,81 39,64 S64,31 77,50 M7,23 Q28,5 49,26','none','stroke="#d29ce8" stroke-width="4" stroke-linecap="round" opacity=".65"'))
        # Controlled perimeter beads read as membrane structure at close scale.
        for x,y in [(-165,-91),(-137,-146),(-91,-161),(-37,-183),(25,-179),(73,-154),(142,-122),(187,-74),(190,19),(166,91),(107,126),(49,163),(-13,172),(-81,148),(-153,118),(-190,46),(-204,-12)]:
            add(cell,c(x,y,3.5,'#ffd6bb','opacity=".7"'))
        for j in range(3):
            particle=find(root,'particle'+str(j))
            add(particle,p('M-20,-25 Q-3,-37 15,-24','none','stroke="#d3ffe3" stroke-width="5" stroke-linecap="round"'))
            for k in range(7):
                a=k*2.4
                add(particle,c(math.cos(a)*18,math.sin(a)*18,2.5,'#329f9b'))
        # Dotted flow behind particles provides direction without text clutter.
        add(root,p('M1137,348 C1059,351 956,359 858,400','none','stroke="#77b7c5" stroke-width="2" stroke-dasharray="3 12" opacity=".6"'))
    elif name=='02-membrane':
        for node in root:
            if node.get('fill')=='#f9ce80': node.set('fill','url(#interior)')
        lipid=find(root,'lipid-bilayer')
        # Opposing lipid tails complete both leaflets of the membrane.
        tails=''
        for x in range(-30,1320,26):
            y=445-x*.1164
            tails+=p(f'M{x},{y+57} q6,-9 0,-19 m8,19 q6,-9 0,-19','none','stroke="#ef9ab4" stroke-width="6" stroke-linecap="round"')
        add(lipid,tails,0)
        gate=find(root,'gate')
        add(gate,p('M-24,-78 Q-44,-8 -26,75 L26,75 Q42,-8 24,-78Z','#281b52'),1)
        add(gate,p('M-58,57 Q-4,91 58,57','none','stroke="#267d97" stroke-width="10" stroke-linecap="round"'))
        for y in [-43,-11,21]:
            add(gate,p(f'M-82,{y} L-64,{y+4} M62,{y+4} L80,{y}','none','stroke="#93f1d0" stroke-width="4" stroke-linecap="round" opacity=".7"'))
        add(root,c(752,248,73,'url(#signal)'),list(root).index(find(root,'protein')))
        add(root,p('M780,277 C811,317 806,341 778,366','none','stroke="#fff0b3" stroke-width="3" stroke-dasharray="4 9"')+p('M767,353 L777,373 L792,356','none','stroke="#fff0b3" stroke-width="3" stroke-linejoin="round"'))
        for i in range(35):
            x=random.randint(40,1220); y=random.randint(540,635)
            add(root,c(x,y,random.randint(2,5),'#c67e88','opacity=".25"'))
        # Foreground molecules are deliberately clipped and soft.
        add(root,'<g filter="url(#blur)" opacity=".4">'+c(-12,280,48,'#9e64c9')+c(1255,598,58,'#b1659b')+'</g>')
    else:
        # Furnish the lab with purposeful, subdued objects behind the scientist.
        add(root,'''<g id="lab-background" opacity=".7">
        <rect x="1073" y="221" width="157" height="11" rx="5" fill="#8abaaa"/>
        <path d="M1110,173 V196 L1094,216 H1151 L1135,196 V173Z" fill="#9cd3be"/>
        <path d="M1108,202 H1137 L1145,213 H1100Z" fill="#51aaa5"/>
        <rect x="1170" y="163" width="13" height="54" rx="5" fill="#eab88a"/><rect x="1190" y="150" width="13" height="67" rx="5" fill="#a69bba"/>
        <path d="M1090,556 H1240 V635 H1090Z" fill="#c2d9c6"/>
        <path d="M1080,548 H1250" stroke="#8fb9aa" stroke-width="12" stroke-linecap="round"/>
        </g>''',4)
        person=find(root,'scientist')
        # Replace stroke-only hands with shaped palms, thumbs and finger folds.
        for node in list(person):
            d=node.get('d','')
            if d.startswith('M-266,196') or d.startswith('M124,277'): person.remove(node)
        add(person,p('M-257,188 C-269,181 -274,163 -283,167 C-288,171 -280,180 -280,183 L-308,175 Q-320,175 -314,183 L-299,191 L-318,186 Q-329,188 -318,196 L-298,206 Q-274,215 -260,204Z','url(#skin)')+p('M-303,191 L-283,198 M-298,184 L-280,191','none','stroke="#ca8191" stroke-width="2.5" stroke-linecap="round"'))
        add(person,p('M122,268 Q133,274 126,285 L95,301 Q80,308 70,301 Q64,297 72,292 L88,285 L74,286 Q66,283 73,278 L96,273Z','url(#skin)')+p('M85,293 L108,283','none','stroke="#cb7f93" stroke-width="2.5" stroke-linecap="round"'))
        head=find(root,'head')
        for node in head:
            if node.get('fill')=='#efa5ab': node.set('fill','url(#skin)')
        add(head,p('M64,28 Q76,73 46,104 Q22,124 -3,121 Q49,141 66,77Z','#c77695','opacity=".3"'),4)
        add(head,c(-36,39,3,'#fff')+c(29,39,3,'#fff')+p('M-60,53 Q-57,67 -45,65 M57,53 Q60,65 66,62','none','stroke="#ef8f9a" stroke-width="7" stroke-linecap="round" opacity=".65"'))
        add(person,'''<g id="coat-details"><path d="M-105,239 L-111,302 M104,213 L116,245" fill="none" stroke="#c0d6d1" stroke-width="4" stroke-linecap="round"/>
        <rect x="-82" y="242" width="48" height="34" rx="5" fill="#b9d9d1"/><rect x="-75" y="248" width="34" height="21" rx="3" fill="#f9f7dd"/>
        <circle cx="-64" cy="256" r="5" fill="#8d79aa"/><path d="M-54,254 H-45 M-54,260 H-45" stroke="#8d79aa" stroke-width="2"/>
        <circle cx="4" cy="319" r="4" fill="#98beb7"/></g>''')
        # Board labels introduce a designed hierarchy without a large empty rectangle.
        add(root,'''<g font-family="Arial"><text x="113" y="254" fill="#588c86" font-size="13" letter-spacing="3">DẤU VẾT CỦA SỰ SỐNG</text>
        <path d="M114,439 H440" stroke="#c0dfcd" stroke-width="2"/>
        <text x="113" y="473" fill="#547a7c" font-size="15">DNA</text><circle cx="184" cy="467" r="3" fill="#8eaf9e"/>
        <text x="201" y="473" fill="#80998e" font-size="13">Thông tin trong từng tế bào</text></g>''')
    svg=ET.tostring(root,encoding='unicode')
    (OUT/f'{name}.svg').write_text(svg,encoding='utf-8')
    (OUT/f'{name}.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg))

sheet=Image.new('RGB',(1280,2160))
for i,name in enumerate(['01-cell','02-membrane','03-scientist']):
    with Image.open(OUT/f'{name}.png') as im: sheet.paste(im,(0,720*i))
sheet.save(OUT/'preview.jpg',quality=95)
print('Saved v2: three SVGs, three PNGs, preview.jpg; v1 preserved.')
