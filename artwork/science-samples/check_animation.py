from pathlib import Path
import subprocess, json
import imageio_ffmpeg

out=Path(__file__).parent/'animation'
video=out/'cell-journey-30s.mp4'
ff=imageio_ffmpeg.get_ffmpeg_exe()
reader=imageio_ffmpeg.read_frames(str(video),pix_fmt='rgb24')
meta=next(reader)
count=0
same=0
previous=None
for frame in reader:
    if frame==previous: same+=1
    previous=frame
    count+=1
assert count==900, count
assert meta['size']==(1280,720), meta
assert abs(meta['fps']-30)<.01, meta
assert same==0, same
report={'decoded_frames':count,'fps':meta['fps'],'size':meta['size'],'identical_adjacent_frames':same,'bytes':video.stat().st_size,'audio':False,'visual_inspection':'Selected source frames; not continuous playback.'}
(out/'validation.json').write_text(json.dumps(report,indent=2))
subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-i',str(video),'-vf','fps=8,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse','-loop','0',str(out/'preview.gif')],check=True)
print(json.dumps(report))
