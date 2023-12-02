'''
A simple CLI command wrapper for FFmpeg written in Python to apply dithering algorithms and color palettes to images and videos. It can be used to turn almost any type of media (supported by FFmpeg) into the style of '37C3: Unlocked'.

Copyright (c) 2023 n0ctua https://github.com/n0ctu/
GNU GPLv3
'''

import subprocess
import argparse
import os
import sys

def is_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert a video/image to a dithered version in the stlye of '37C3: Unlocked' using FFmpeg.")
    parser.add_argument('-i', '--input', default='input.mp4', help='Input file')
    parser.add_argument('-p', '--final_palette', default='palette/palette-bw-alpha.png', help='Final color palette')
    parser.add_argument('-pi', '--intermediate_palette', default='', help='Intermediate color palette')
    parser.add_argument('-fps', '--framerate', type=int, default=24, help='Frame rate')
    parser.add_argument('-s', '--size', type=int, default=-1, help='Width of the output GIF, aspect ratio is preserved')
    parser.add_argument('-b', '--brightness', type=float, default=0, help='Brightness, -1 to 1, with 0 being the default value')
    parser.add_argument('-c', '--contrast', type=float, default=1, help='Contrast, 0 to 2, with 1 being the default value')
    parser.add_argument('-d', '--dither', default='bayer', help='Dither algorithm: bayer, heckbert, floyd_steinberg, sierra2, sierra2_4a')
    parser.add_argument('-bs', '--bayer_scale', type=float, default=0.5, help='Bayer scale: 0 to 2')
    parser.add_argument('-loop', '--loop', type=int, default=0, help='Loop')
    parser.add_argument('-o', '--output', default='output.gif', help='Output filename')

    args = parser.parse_args()

    if not is_ffmpeg_installed():
        print("Error: FFmpeg is not installed on this system or missing from PATH.", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.input):
        print(f"Error: The input file '{args.input}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if os.path.exists(args.output):
        print(f"Error: The output file '{args.output}' already exists.", file=sys.stderr)
        sys.exit(1)

    ffmpeg_command = [
        'ffmpeg', '-i', args.input,
    ]

    if args.intermediate_palette:
        ffmpeg_command.extend(['-i', args.intermediate_palette])

    ffmpeg_command.extend(['-i', args.final_palette])

    filter_complex = f"[0:v]fps={args.framerate},scale={args.size}:-1:flags=neighbor,eq=brightness={args.brightness}:contrast={args.contrast} [x];"
    
    if args.intermediate_palette:
        filter_complex += " [x][1:v]paletteuse=dither=none [y]; [y][2:v]"
    else:
        filter_complex += " [x][1:v]"

    filter_complex += f"paletteuse=dither={args.dither}:bayer_scale={args.bayer_scale}:diff_mode=rectangle"

    ffmpeg_command.extend(['-filter_complex', filter_complex, '-loop', str(args.loop), args.output])

    subprocess.run(ffmpeg_command)

if __name__ == "__main__":
    main()
