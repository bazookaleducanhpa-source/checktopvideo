"""Nine distinct animated compositions; 36 seconds, 30 fps, original vector art."""
import math, copy, io, json, sys, subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import xml.etree.ElementTree as ET
import resvg_py, imageio_ffmpeg
from PIL import Image, ImageDraw
import animate as base

OUT=Path(__file__).parent/'sequence-v3'
OUT.mkdir(exist_ok=True)
FPS=30; COUNT=1080
P=base.path; C=base.circle; E=base.ease
def G(s,tr=''): return f'<g transform="{tr}">{s}</g>'
def R(x,y,w,h,col,r=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{col}"/>'
def T(x,y,s,size=24,col='#f8eacb'): return f'<text x="{x}" y="{y}" font-family="Arial" font-size="{size}" fill="{col}">{s}</text>'
DEFS='''<defs><radialGradient id="deep"><stop stop-color="#492467"/><stop offset="1" stop-color="#10142e"/></radialGradient>
<linearGradient id="aqua" x2=".5" y2="1"><stop stop-color="#c0fff0"/><stop offset="1" stop-color="#2ca9bc"/></linearGradient>
<linearGradient id="pink" x2=".4" y2="1"><stop stop-color="#f998b7"/><stop offset="1" stop-color="#8c3f93"/></linearGradient>
<radialGradient id="light"><stop stop-color="#ffe99c" stop-opacity=".8"/><stop offset="1" stop-color="#ffd87a" stop-opacity="0"/></radialGradient>
<linearGradient id="warm" x2=".5" y2="1"><stop stop-color="#fff0b6"/><stop offset="1" stop-color="#e8bc97"/></linearGradient></defs>'''
def signal(x,y,r=16): return C(x,y,r*3,'url(#light)')+C(x,y,r,'#ffe5a0')+C(x-r*.28,y-r*.3,r*.23,'#fffbea')
def particles(t,col='#7d6cad',n=35):
    return ''.join(C((i*193+t*(8+i%4*5))%1400-60,100+(i*113)%520+8*math.sin(t+i),2+i%5,col,'opacity=".3"') for i in range(n))
def doc(s): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">{DEFS}{s}</svg>'
def core(root):
    return ''.join(ET.tostring(e,encoding='unicode') for e in root)
SCIENTIST=base.load('03-scientist')
def lab(u,ending=False):
    root=copy.deepcopy(SCIENTIST)
    actor=base.group(root,'scientist')
    actor.set('transform',f'translate({960 if ending else 855} {295+3*math.sin(u*2)}) scale({.85 if ending else 1})')
    base.group(actor,'head').set('transform',f'rotate({-3+3*E(u,.4,2)} 0 110)')
    s=core(root)
    s+=R(50,580,1180,30,'#8db8aa',9)+R(83,610,28,110,'#739d98')+R(1160,610,28,110,'#739d98')
    s+=G(P('M0,0 L44,0 L44,76 L71,126 Q76,140 62,140 L-18,140 Q-32,140 -27,126 L0,76Z','#bbe1d6')+P('M-12,111 L56,111 L68,133 L-24,133Z','url(#aqua)')+R(-4,-9,52,14,'#689f9d',5),'translate(536 428)')
    if not ending:
        s+=signal(560,508,9+2*math.sin(u*2))
        s+=T(70,80,'Một giọt nhỏ chứa điều gì?',34,'#3b385b')
    else:
        # Different composition and a completed observation replace the original board.
        s+=R(65,197,430,322,'#203751',24)+R(90,222,380,265,'#13293f',14)
        for i in range(6):
            x=136+i*57; h=30+95*E(u,i*.15,.9+i*.15)
            s+=R(x,440-h,31,h,['#65d3bd','#9f92d1','#f4d48a'][i%3],6)
        s+=T(115,259,'QUAN SÁT • KHÁM PHÁ',17,'#b2e7d5')
        s+=T(70,80,'Đổi góc nhìn. Mở một thế giới.',34,'#3b385b')
    return s

def droplet(u):
    s=R(0,0,1280,720,'#17213b')+particles(u)
    s+=P('M0,574 Q650,523 1280,574 L1280,720 L0,720Z','#364b66')
    s+='<ellipse cx="640" cy="560" rx="305" ry="65" fill="#64a7ae"/><ellipse cx="640" cy="547" rx="305" ry="55" fill="#b3ded3"/><ellipse cx="640" cy="544" rx="270" ry="42" fill="#408da4"/>'
    s+=G(R(-31,-180,62,190,'#b5c7d2',10)+P('M-31,0 L-12,51 L12,51 L31,0Z','#e0ecdf')+R(-22,-167,15,145,'#eaf7ed',6),'translate(640 181)')
    v=E(u,.25,2.15); y=265+245*v
    if u<2.15:
        s+=G(P('M0,-47 C-12,-17 -33,1 -28,21 C-23,56 27,58 31,22 C34,2 12,-22 0,-47Z','url(#aqua)')+P('M-14,9 Q-21,27 -7,33','none','stroke="#ebfff0" stroke-width="6" stroke-linecap="round"'),f'translate(640 {y}) scale({1+.1*v} {1+.25*v})')
    ripple=E(u,2,3.6)
    if u>2:
        for i in range(3): s+=f'<ellipse cx="640" cy="545" rx="{25+ripple*(210+i*25)}" ry="{7+ripple*(20+i*4)}" fill="none" stroke="#a2f2d6" stroke-width="3" opacity="{max(0,1-ripple*.8-i*.15)}"/>'
    s+=signal(640,545,9)
    return s

def cellshot(u):
    root=base.macro(u)
    cell=base.group(root,'cell')
    # Camera travels across a population, then settles on the expressive protagonist.
    cell.set('transform',f'translate({470+55*E(u,0,3)} {380+10*math.sin(u)}) rotate({-12+3*u}) scale({.85+.25*E(u,.4,3.8)})')
    return core(root)+signal(970-140*E(u,0,3.8),290+45*math.sin(u*.5),16)

def gate(u):
    root=base.micro(9+u*3.6)
    return G(core(root),f'translate({-40*E(u,0,3.8)} {-25*E(u,0,3.8)}) scale({1+.06*E(u,0,3.8)})')

def tunnel(u):
    s=R(0,0,1280,720,'#162a43')
    # Curving organelle walls, receding hoops and directional streaks create a new view.
    for i in range(11):
        z=((i/11+u*.12)%1); rx=60+z*z*820; ry=30+z*z*460
        s+=f'<ellipse cx="760" cy="325" rx="{rx}" ry="{ry}" fill="none" stroke="{["#29376a","#424279","#346f83"][i%3]}" stroke-width="{5+z*45}" opacity="{.2+.7*z}"/>'
    for i in range(24):
        a=i*2.4; r=((i*73+u*150)%750)
        x=760+math.cos(a)*r; y=325+math.sin(a)*r*.6
        s+=P(f'M{x},{y} l{math.cos(a)*35},{math.sin(a)*21}','none','stroke="#77bdb6" stroke-width="3" opacity=".35"')
    s+=P('M-100,590 C290,270 425,618 835,400 S1190,353 1380,100','none','stroke="#87639c" stroke-width="90"')
    s+=P('M-100,573 C290,253 425,601 835,383 S1190,336 1380,83','none','stroke="#be86bc" stroke-width="12"')
    for i in range(9):
        x=(i*164+u*210)%1540-130; y=370+80*math.sin(x*.005)
        s+=signal(x,y,12 if i%3 else 20)
    return s

def dna(u):
    s=R(0,0,1280,720,'#fff0c5')+particles(u,'#c4a8be',22)
    s+=C(1110,90,260,'#f9dfb6')
    # Rotation illusion: phase-driven rung depth, with near segments drawn last.
    phase=u*.8
    for i in range(54):
        x=i*26-60-u*16; mid=350+45*math.sin(x*.003)
        a=i*.24+phase; off=100*math.sin(a)
        col='#8ebfbd' if math.cos(a)<0 else '#61b6b0'
        s+=P(f'M{x},{mid-off} L{x},{mid+off}','none',f'stroke="{col}" stroke-width="9" stroke-linecap="round"')
    for ph,col in [(0,'#2b86a4'),(math.pi,'#7552a1')]:
        pts=[]
        for i in range(250):
            x=i*5.6-60-u*16; y=350+45*math.sin(x*.003)+100*math.sin(i*5.6/26*.24+phase+ph)
            pts.append(f'{x},{y}')
        s+=P('M'+' L'.join(pts),'none',f'stroke="{col}" stroke-width="17" stroke-linecap="round"')
    x=390+360*E(u,.2,3.5); y=230-24*math.sin(u)
    s+=G(P('M-70,-28 Q-37,-68 3,-41 Q43,-62 72,-19 L56,32 Q24,12 -3,43 Q-49,50 -70,14Z','#ed8f83')+P('M-39,-19 Q-12,-35 17,-18','none','stroke="#ffcb9e" stroke-width="10" stroke-linecap="round"')+signal(2,2,15),f'translate({x} {y}) rotate({-10+5*math.sin(u)})')
    return s

def network(u):
    s=R(0,0,1280,720,'#202344')+particles(u)
    nodes=[(120,360),(390,190),(390,500),(690,290),(690,555),(1000,170),(1100,430)]
    edges=[(0,1),(0,2),(1,3),(2,3),(2,4),(3,5),(3,6),(4,6)]
    for j,(a,b) in enumerate(edges):
        x,y=nodes[a]; X,Y=nodes[b]
        s+=P(f'M{x},{y} C{x+110},{y} {X-110},{Y} {X},{Y}','none','stroke="#51567e" stroke-width="11"')
        v=max(0,min(1,(u-j*.18)/1.25))
        if 0<v<1:
            px=(1-v)**3*x+3*(1-v)**2*v*(x+110)+3*(1-v)*v*v*(X-110)+v**3*X
            py=(1-v)**3*y+3*(1-v)**2*v*y+3*(1-v)*v*v*Y+v**3*Y
            s+=signal(px,py,11)
    for i,(x,y) in enumerate(nodes):
        active=E(u,i*.28,.7+i*.28)
        s+=C(x,y,57+3*math.sin(u*2+i),'#524c88')+C(x,y,44,'#65caba' if active>.5 else '#7772a7')+C(x-10,y-12,12,'#b5eee1','opacity=".7"')
        if active>0: s+=C(x,y,60+active*25,'none',f'stroke="#91dcc4" stroke-width="2" opacity="{(1-active)*.8}"')
    return s

def tissue(u):
    s=R(0,0,1280,720,'#38204c')
    cells=''
    for row in range(5):
        for col in range(9):
            x=col*156+(row%2)*78-50; y=row*140+70
            activation=E(u,.18*col+.2*row,.18*col+.2*row+.6)
            color='#eead72' if activation>.5 else '#8460b0'
            scale=1+.05*math.sin(u*3-col*.6-row)
            d='M-64,-38 Q-72,-65 -20,-65 L40,-60 Q76,-47 70,-5 L58,42 Q48,65 2,62 L-48,55 Q-72,40 -64,-38Z'
            shape=P(d,'#4a315e','stroke="#b48ac1" stroke-width="5"')+P(d,color,'transform="scale(.86)"')+C(5,7,22,'#674078')+C(-1,0,9,'#b58fc6')
            cells+=G(shape,f'translate({x} {y}) scale({scale})')
    s+=G(cells,f'translate({-30*u} {-15*u}) rotate(-5 640 360)')
    s+=P(f'M{-50+u*340},0 l-140,720','none','stroke="#ffe19a" stroke-width="5" opacity=".5"')
    return s

SCENES=[lab,droplet,cellshot,gate,tunnel,dna,network,tissue,lambda u:lab(u,True)]
CAPTIONS=['Bắt đầu từ một câu hỏi.','Tiến gần hơn — vào một giọt mẫu.','Một thế giới ở tỷ lệ khác.','Tiếp cận. Tương tác. Đi qua.','Theo dòng chuyển động bên trong.','Đổi góc nhìn: cấu trúc xoắn.','Một điểm chạm, nhiều kết nối.','Từ một tế bào đến cả vùng mô.','Trở lại con người — với một góc nhìn mới.']
def svg_at(n):
    t=n/FPS; idx=min(8,int(t/4)); u=t-idx*4
    s=SCENES[idx](u)
    # Several visual grammars: match cut, object occlusion, hard cut, sweeping wipe.
    if idx in [0,1] and u>3.55:
        v=E(u,3.55,4)
        x,y=(560,508) if idx==0 else (640,545)
        s+=C(x,y,v*1500,'#17213b' if idx==0 else '#151333')
    if idx in [4,6] and u>3.7:
        v=E(u,3.7,4)
        x=1600-v*2000
        s+=P(f'M{x},-100 H1800 V850 H{x-320}Z','#fff0c5' if idx==4 else '#38204c')
    # Short bottom caption replaces the repetitive large title card layout.
    s+=R(0,646,1280,74,'#11162b')+T(48,690,CAPTIONS[idx],23)
    s+=T(1130,690,f'{idx+1:02d} / 09',15,'#9eaec1')
    return doc(s)
def render(n):
    return resvg_py.svg_to_bytes(svg_string=svg_at(n),skip_system_fonts=True,font_files=['C:/Windows/Fonts/arial.ttf','C:/Windows/Fonts/arialbd.ttf'])
def boards():
    sheet=Image.new('RGB',(1280,3*270),'#11162b'); draw=ImageDraw.Draw(sheet)
    for i in range(9):
        n=i*120+60; data=render(n)
        (OUT/f'shot-{i+1:02d}.svg').write_text(svg_at(n),encoding='utf-8')
        (OUT/f'shot-{i+1:02d}.png').write_bytes(data)
        im=Image.open(io.BytesIO(data)).convert('RGB'); im.thumbnail((426,240))
        x,y=i%3*426,i//3*270;sheet.paste(im,(x,y));draw.text((x+10,y+246),f'SHOT {i+1:02d} | {i*4:02d}-{i*4+4:02d}s',fill='white')
    sheet.save(OUT/'storyboard.jpg',quality=95)
def main():
    if '--boards' in sys.argv: boards();return
    ff=imageio_ffmpeg.get_ffmpeg_exe()
    video=OUT/'nine-scenes-36s.mp4'
    proc=subprocess.Popen([ff,'-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','png','-r','30','-i','-','-an','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-movflags','+faststart',str(video)],stdin=subprocess.PIPE)
    with ProcessPoolExecutor(max_workers=4) as pool:
        for start in range(0,COUNT,30):
            for data in pool.map(render,range(start,start+30)):proc.stdin.write(data)
            print(f'{start+30}/{COUNT}',flush=True)
    proc.stdin.close(); assert proc.wait()==0
    reader=imageio_ffmpeg.read_frames(str(video)); meta=next(reader);count=sum(1 for _ in reader)
    assert count==COUNT and meta['size']==(1280,720)
    for i in range(3):
        subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-ss',str(i*12),'-i',str(video),'-t','12','-an','-c:v','libx264','-crf','19','-pix_fmt','yuv420p',str(OUT/f'part-{i+1}.mp4')],check=True)
    subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-i',str(video),'-vf','fps=8,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse','-loop','0',str(OUT/'preview.gif')],check=True)
    (OUT/'validation.json').write_text(json.dumps({'decoded_frames':count,'fps':meta['fps'],'size':meta['size'],'duration':36,'scenes':9,'audio':False,'visual_review':'Nine representative frames plus selected boundary frames; not continuous playback'},indent=2))
    print('Complete: MP4, three 12-second clips, GIF and validation',flush=True)
if __name__=='__main__':main()
