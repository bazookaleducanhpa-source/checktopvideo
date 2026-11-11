"""Deterministic 30-second motion study, using editable SVG scene layers."""
from pathlib import Path
import copy, math, io, subprocess, json
from concurrent.futures import ProcessPoolExecutor
import xml.etree.ElementTree as ET
import resvg_py, imageio_ffmpeg
from PIL import Image, ImageDraw

ROOT=Path(__file__).parent
OUT=ROOT/'animation'
OUT.mkdir(exist_ok=True)
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
FPS=30
def node(s): return ET.fromstring(f'<g xmlns="{NS}">{s}</g>')
def group(root,id): return next(e for e in root.iter() if e.get('id')==id)
def ease(t,a,b):
    u=max(0,min(1,(t-a)/(b-a))); return u*u*(3-2*u)
def mix(a,b,u): return a+(b-a)*u
def circle(x,y,r,c,extra=''): return f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r}" fill="{c}" {extra}/>'
def path(d,c,extra=''): return f'<path d="{d}" fill="{c}" {extra}/>'

def load(name):
    root=ET.fromstring((ROOT/'v2'/f'{name}.svg').read_text(encoding='utf-8'))
    for e in list(root):
        if e.tag.endswith('text'): root.remove(e)
    return root
CELL=load('01-cell'); MEM=load('02-membrane')
MEM.remove(group(MEM,'protein'))
# Remove the old fixed signal, fixed path and directional annotation.
for e in list(MEM):
    if e.tag.endswith('circle') and e.get('cx') in ['752','747']: MEM.remove(e)
    elif e.tag.endswith('g'):
        serialized=ET.tostring(e,encoding='unicode')
        if 'url(#signal)' in serialized or 'M780,277' in serialized: MEM.remove(e)

def macro(t):
    root=copy.deepcopy(CELL)
    cell=group(root,'cell')
    bob=math.sin(t*1.4)*5
    zoom=1+0.06*ease(t,0,6)
    cell.set('transform',f'translate(555 {410+bob}) rotate({-8+1.5*math.sin(t*.8)}) scale({1.12*zoom})')
    # Small membrane deformation; face and nucleus retain their own geometry.
    for e in list(cell)[:3]:
        if e.tag.endswith('path'):
            old=e.get('transform','')
            e.set('transform',f'{old} scale({1+.009*math.sin(t*2)} {1-.007*math.sin(t*2)})')
    face=group(cell,'face')
    blink=min(abs(t-b) for b in [2.4,5.7,27.3,29.1])
    if blink<.13:
        for e in face:
            if e.tag.endswith('ellipse') or e.tag.endswith('circle'):
                e.set('transform',f'translate(0 -61) scale(1 {max(.08,blink/.13)}) translate(0 61)')
    nucleus=group(cell,'nucleus')
    nucleus.set('transform',f'translate({2*math.sin(t*1.4-.4)} {2*math.cos(t*1.2)})')
    for j,(x,y) in enumerate([(959,275),(1030,467),(839,560)]):
        group(root,'particle'+str(j)).set('transform',f'translate({x+10*math.sin(t*.7+j)} {y+12*math.cos(t*.6+j)}) rotate({t*5+j*10})')
    # A selected membrane location foreshadows the scale change.
    a=ease(t,4,5)*(1-ease(t,7,8))
    root.append(node(circle(748,397,30+3*math.sin(t*4),'none',f'stroke="#b9ffe6" stroke-width="3" opacity="{a}"')+circle(748,397,43,'none',f'stroke="#b9ffe6" stroke-width="1" opacity="{a*.4}"')))
    return root

def micro(t):
    root=copy.deepcopy(MEM)
    # A two-link chain with invariant bone lengths; root is locked to the membrane.
    u=ease(t,13,16)
    tx=mix(691,721,u); ty=mix(249,277,u)
    back=ease(t,21,23)
    tx=mix(tx,691,back); ty=mix(ty,249,back)
    bx,by=585,375; l1,l2=110,105
    dx,dy=tx-bx,ty-by
    dist=math.hypot(dx,dy)
    angle=math.atan2(dy,dx)-math.acos(max(-1,min(1,(l1*l1+dist*dist-l2*l2)/(2*l1*dist))))
    ex,ey=bx+l1*math.cos(angle),by+l1*math.sin(angle)
    arm=path(f'M{bx},{by} L{ex},{ey} L{tx},{ty}','none','stroke="#228cb8" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"')
    for x,y in [(bx,by),(ex,ey),(tx,ty)]: arm+=circle(x,y,18,'#58d7e1')+circle(x-4,y-5,6,'#a8f5eb')
    opening=1-ease(t,11.7,12.2)+ease(t,17,17.5)
    gap=9+13*min(1,opening)
    arm+=path(f'M{tx},{ty} l24,{-gap} l20,5 M{tx},{ty} l24,{gap} l20,-5','none','stroke="#59dce4" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"')
    root.append(node(f'<g id="animated-protein">{arm}</g>'))
    # Gate leaves separate before the cargo crosses, then close after release.
    opened=ease(t,15.6,17)*(1-ease(t,20.5,22))
    gate=group(root,'gate')
    paths=[e for e in gate if e.tag.endswith('path')]
    for e in paths:
        d=e.get('d','')
        if d.startswith('M-28') or d.startswith('M-58'): e.set('transform',f'translate({-10*opened} 0)')
        if d.startswith('M28'): e.set('transform',f'translate({10*opened} 0)')
    # At contact, the cargo and gripper share a position; release is continuous.
    arrival=ease(t,9,12)
    sx=mix(1080,tx+46,arrival); sy=mix(191,ty,arrival)
    if t>=12: sx,sy=tx+46,ty
    if t>=17:
        v=ease(t,17,20.5); sx=mix(767,816,v); sy=mix(277,547,v)
    if t>=20.5:
        v=ease(t,20.5,24); sx=mix(816,1010,v); sy=mix(547,595,v)
    root.append(node(circle(sx,sy,65,'url(#signal)')+circle(sx,sy,19,'#ffe79b')+circle(sx-5,sy-6,6,'#fffde5')))
    for e in root.iter():
        id=e.get('id','')
        if id.startswith('molecule'):
            old=e.get('transform',''); seed=int(id[8:])
            e.set('transform',f'translate({5*math.sin(t*.6+seed)} {6*math.cos(t*.8+seed)}) {old}')
    return root

def render(n):
    t=n/FPS
    # Circular reveal expands from the selected membrane location.
    if t<7: root=macro(t)
    elif t<9:
        root=macro(t)
        rad=1550*ease(t,7,9)
        root.append(node(f'<defs><clipPath id="reveal"><circle cx="748" cy="397" r="{rad}"/></clipPath></defs>'))
        other=micro(t)
        overlay=ET.Element(f'{{{NS}}}g',{'clip-path':'url(#reveal)'})
        for e in list(other):
            if not e.tag.endswith('defs'): overlay.append(e)
        root.append(overlay)
    elif t<24: root=micro(t)
    elif t<26:
        root=macro(t)
        rad=1550*(1-ease(t,24,26))
        root.append(node(f'<defs><clipPath id="reveal"><circle cx="748" cy="397" r="{rad}"/></clipPath></defs>'))
        overlay=ET.Element(f'{{{NS}}}g',{'clip-path':'url(#reveal)'})
        for e in list(micro(t)):
            if not e.tag.endswith('defs'): overlay.append(e)
        root.append(overlay)
    else: root=macro(t)
    if t<7: title='Một thế giới đang chuyển động'; sub='TỪ TẾ BÀO ĐẾN MÀNG TẾ BÀO'
    elif t<12: title='Một tín hiệu đang đến gần'; sub='01 / TIẾP CẬN'
    elif t<17: title='Tiếp nhận và đưa tới cổng'; sub='02 / TƯƠNG TÁC'
    elif t<22: title='Cổng mở. Hạt đi qua.'; sub='03 / VẬN CHUYỂN'
    elif t<26: title='Hoàn thành một hành trình nhỏ'; sub='04 / ỔN ĐỊNH'
    else: title='Những chuyển động nhỏ. Một thế giới sống.'; sub='SCIENCE ANIMATION / MOTION STUDY'
    root.append(node(f'<g font-family="Arial"><text x="64" y="64" fill="#bbaacb" font-size="15" letter-spacing="3">{sub}</text><text x="64" y="111" fill="#fff3d8" font-size="32" font-weight="bold">{title}</text><rect x="48" y="662" width="1184" height="3" rx="1" fill="#615578" opacity=".4"/><rect x="48" y="662" width="{1184*t/30}" height="3" rx="1" fill="#b8e7d3"/><text x="64" y="695" fill="#aaa4bc" font-size="12">MINH HỌA CÁCH ĐIỆU · BẢN THỬ CHUYỂN ĐỘNG</text></g>'))
    return resvg_py.svg_to_bytes(svg_string=ET.tostring(root,encoding='unicode'), skip_system_fonts=True, font_files=['C:/Windows/Fonts/arial.ttf','C:/Windows/Fonts/arialbd.ttf'])

def main():
    ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
    cmd=[ffmpeg,'-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','png','-r',str(FPS),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart',str(OUT/'cell-journey-30s.mp4')]
    process=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    selected=[0,180,240,300,360,450,510,555,600,660,750,899]
    thumbs=[]
    with ProcessPoolExecutor(max_workers=4) as pool:
        for start in range(0,900,30):
            for n,data in zip(range(start,start+30),pool.map(render,range(start,start+30))):
                process.stdin.write(data)
                if n in selected:
                    (OUT/f'frame-{n:04d}.png').write_bytes(data)
                    im=Image.open(io.BytesIO(data)).convert('RGB'); im.thumbnail((426,240))
                    thumbs.append((n,im))
            print(f'Rendered {start+30}/900',flush=True)
    process.stdin.close()
    if process.wait()!=0: raise RuntimeError('Encoding failed')
    sheet=Image.new('RGB',(1278,4*265),'#151333'); d=ImageDraw.Draw(sheet)
    for i,(n,im) in enumerate(thumbs):
        x,y=i%3*426,i//3*265;sheet.paste(im,(x,y));d.text((x+8,y+244),f'{n/FPS:.2f}s / frame {n}',fill='white')
    sheet.save(OUT/'contact-sheet.jpg',quality=94)
    (OUT/'manifest.json').write_text(json.dumps({'duration_seconds':30,'fps':30,'frames':900,'resolution':[1280,720],'audio':False,'source':'../v2/*.svg','sampled_frames':selected},indent=2))
    print('Complete',flush=True)

if __name__=='__main__': main()
