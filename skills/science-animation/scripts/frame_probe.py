"""Extract consecutive decoded frames for drawing/motion study; no FPS resampling.

Requires Pillow and imageio-ffmpeg. Times are CFR estimates, not source PTS.
Use --start-frame for precise decoded-frame indexing. Existing output is refused.
"""
import argparse
import json
import subprocess
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('video', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--start', type=float, default=0)
    ap.add_argument('--start-frame', type=int)
    ap.add_argument('--count', type=int, default=24)
    args = ap.parse_args()
    if not args.video.is_file() or args.count < 1 or args.count > 240 or args.start < 0:
        ap.error('Existing video, nonnegative start and count in 1..240 required')
    reader = imageio_ffmpeg.read_frames(str(args.video))
    meta = next(reader)
    reader.close()
    fps = meta['fps']
    first = args.start_frame if args.start_frame is not None else round(args.start * fps)
    if first < 0:
        ap.error('start-frame must be nonnegative')
    args.output.mkdir(parents=True, exist_ok=False)
    subprocess.run([
        imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-loglevel', 'error',
        '-i', str(args.video), '-vf',
        f'select=between(n\\,{first}\\,{first + args.count - 1}),scale=640:-2',
        '-fps_mode', 'passthrough', '-frames:v', str(args.count),
        str(args.output / 'frame-%04d.png'),
    ], check=True)
    files = sorted(args.output.glob('frame-*.png'))
    if len(files) != args.count:
        raise RuntimeError(f'Requested {args.count} frames; decoded {len(files)}')
    rows = []
    for i, path in enumerate(files):
        rows.append({'file': path.name, 'decoded_frame_zero_based': first+i,
                     'estimated_time_seconds_CFR': (first+i)/fps})
    for page in range((len(files)+11)//12):
        sheet = Image.new('RGB', (1280, 3*204), '#101322')
        draw = ImageDraw.Draw(sheet)
        for k, path in enumerate(files[page*12:(page+1)*12]):
            index = page*12+k
            x, y = (k % 4)*320, (k//4)*204
            with Image.open(path) as im:
                im.thumbnail((320, 180))
                sheet.paste(im, (x, y))
            draw.text((x+5, y+183), f'n={first+index} ~{(first+index)/fps:.3f}s', fill='white')
        sheet.save(args.output / f'sheet-{page+1:02d}.jpg', quality=94)
    manifest = {'source': str(args.video.resolve()), 'reported_fps': fps,
                'note': 'Consecutive decoded frames. Times assume CFR; audio not inspected.',
                'frames': rows}
    (args.output/'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps({'output': str(args.output), 'count': len(files), 'fps': fps, 'first': first}))


if __name__ == '__main__':
    main()
