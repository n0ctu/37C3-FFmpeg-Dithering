# 37C3-FFmpeg-Dithering

A simple CLI command wrapper for FFmpeg written in Python to apply dithering algorithms and color palettes to images and videos. It can be used to turn almost any type of media (supported by FFmpeg) into the style of '37C3: Unlocked'.

https://events.ccc.de/2023/11/27/37c3-hat-die-haare-schoen/

## Prerequisites

- Clone this repository (you'll need the 'palette' folder and the 'dither-this.py' file)
- Python 3 installed and added to PATH
- FFmpeg installed and added to PATH

## Usage

Simply call the 'dither-this.py' file from the command line or run it without any arguments. When running the script without any arguments, it will look for a file called 'input.mp4' and process it with the default values.

![Demo](/demo/demo.gif "Demo")

By passing the '-h' or '--help' flag you can list all available options.

```
n0c@box:~$ dither-this.py --help

usage: dither-this.py [-h] [-i INPUT] [-p FINAL_PALETTE] [-pi INTERMEDIATE_PALETTE] [-fps FRAMERATE] [-s SIZE] [-b BRIGHTNESS] [-c CONTRAST] [-d DITHER] [-bs BAYER_SCALE]
                      [-loop LOOP] [-o OUTPUT]

Convert a video/image to a dithered version in the stlye of '37C3: Unlocked' using FFmpeg.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file
  -p FINAL_PALETTE, --final_palette FINAL_PALETTE
                        Final color palette
  -pi INTERMEDIATE_PALETTE, --intermediate_palette INTERMEDIATE_PALETTE
                        Intermediate color palette
  -fps FRAMERATE, --framerate FRAMERATE
                        Frame rate
  -s SIZE, --size SIZE  Width of the output GIF, aspect ratio is preserved
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        Brightness, -1 to 1, with 0 being the default value
  -c CONTRAST, --contrast CONTRAST
                        Contrast, 0 to 2, with 1 being the default value
  -d DITHER, --dither DITHER
                        Dither algorithm: bayer, heckbert, floyd_steinberg, sierra2, sierra2_4a
  -bs BAYER_SCALE, --bayer_scale BAYER_SCALE
                        Bayer scale: 0 to 2
  -loop LOOP, --loop LOOP
                        Loop
  -o OUTPUT, --output OUTPUT
                        Output filename
```

## Examples (Image to Image)

Default values with resizing to 256px width:

```
n0c@box:~$ dither-this.py -i lenna.jpg -s 256 -o lenna-default.jpg
```

![Lenna Default](/demo/lenna-default.jpg "Lenna Default")

Alternative dithering algorithm:

```
n0c@box:~$ dither-this.py -i lenna.jpg -s 256 -d floyd_steinberg -o lenna-floyd_steinberg.jpg
```

![Lenna Floyd Steinberg](/demo/lenna-floyd_steinberg.jpg "Lenna Floyd Steinberg")

Alternative dithering algorithm with brightness/contrast fix:

```
n0c@box:~$ dither-this.py -i lenna.jpg -s 256 -d floyd_steinberg -b -0.3 -c 1.3 -o lenna-floyd_steinberg-fix.jpg
```

![Lenna Floyd Steinberg Fix](/demo/lenna-floyd_steinberg-fix.jpg "Lenna Floyd Steinberg Fix")


## Examples (Video / GIF)

Video to GIF:

```
n0c@box:~$ dither-this.py -i input.mp4 -s 256 -o dither-video.gif
```

![Luxeria Logo Default](/demo/luxeria-default.gif "Luxeria Logo Default")

Using the 'floyd_steinberg' dithering algorithm:

```
n0c@box:~$ dither-this.py -i input.mp4 -d floyd_steinberg -o output.gif
```

![Luxeria Logo Floyd Steinberg](/demo/luxeria-floyd_steinberg.gif "Luxeria Logo Floyd Steinberg")

Reducing the color palette before applying the dithering algorithm (intermediate palette):

```
n0c@box:~$ dither-this.py -i input.mp4 -pi palette/palette-5-shades-of-gray-alpha.png -o output.gif
```

![Luxeria Logo Floyd Steinberg Intermediate Palette](/demo/luxeria-floyd_steinberg-intermediate.gif "Luxeria Logo Floyd Steinberg Intermediate Palette")

Using a different color palette for the final output:

```
n0c@box:~$ dither-this.py -i input.mp4 -p palette/palette-5-shades-of-gray-alpha.png -o output.gif
```

## License

GNU GPLv3

Well, it's just a wrapper for a great piece of software doing the hard work (FFmpeg) and an experiment for the lulz. Do whatever you want with this python snippet, don't blame me and share any improvements and results you make!