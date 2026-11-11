from pathlib import Path
import json
import imageio_ffmpeg
from PIL import Image,ImageDraw

out=Path(__file__).parent/'sequence-v3'
selected=sorted([n for b in range(120,1080,120) for n in [b-3,b+3]])
reader=imageio_ffmpeg.read_frames(str(out/'nine-scenes-36s.mp4'),pix_fmt='rgb24')
meta=next(reader)
sheet=Image.new('RGB',(1280,4*205),'#12152d');draw=ImageDraw.Draw(sheet)
count=0
for n,data in enumerate(reader):
    count+=1
    if n in selected:
        i=selected.index(n);im=Image.frombytes('RGB',meta['size'],data);im.thumbnail((320,180))
        x,y=i%4*320,i//4*205;sheet.paste(im,(x,y));draw.text((x+8,y+185),f'{n/30:.2f}s',fill='white')
sheet.save(out/'transition-review.jpg',quality=94)
assert count==1080
for part in range(1,4):
    r=imageio_ffmpeg.read_frames(str(out/f'part-{part}.mp4'));next(r)
    assert sum(1 for _ in r)==360
report=json.loads((out/'validation.json').read_text())
report.update({'clip_frames':[360,360,360],'transition_frames_checked':selected,'purpose':'Original visual/motion study; not a verified biological pathway'})
(out/'validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report))
