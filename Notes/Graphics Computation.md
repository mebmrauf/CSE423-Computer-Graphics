# Graphics Computation

## Formulas

- **Pixel Calculation**

```
The total number of pixels in an image is given by:
Total Pixels = Width ✕ Height

Example:
For a 1920 × 1080 Full HD image:
Total Pixels = 1920 × 1080 = 2,073,600 pixels
```

- **Aspect Ratio**

```
Aspect Ratio is the ratio of an image's width to its height:
​Aspect Ratio = Width / Height

Example:
For a 1920 x 1080 image:
Aspect Ratio = 1920 / 1080 = 16 : 9
```

- **Frame Rate(FPS)**

```
Frame rate (Frames Per Second) determines how many images (frames) are displayed per second:
Frame Time (ms) = (1 / FPS) ✕ 1000 

Example:
For 60 FPS:
Frame Time = (1/60) × 1000 = 16.67 ms per frame
This means each frame must be rendered in 16.67 milliseconds to maintain 60 FPS.
```

- **Pixel Processing Speed**

```
The number of pixels processed per second can be calculated as:
Pixels per Second = Total Pixels per Frame ✕ FPS = Width ✕ Height ✕ FPS

If a GPU can process N pixels per millisecond, the total pixels it can render per frame is:
Pixels per Second = N ✕ Frame Time 

Example:
For a 1920 × 1080 image at 60 FPS:
Pixels per Second = 2,073,600 × 60 = 124,416,000 pixels per second

If a GPU can process 100,000 pixels per millisecond:
Pixels per Frame = 100,000 × 16.67 = 1,667,000 pixels per frame
```

- **Colors Available Based on Bit Depth**

```
Colors Available = 2^Bit Depth

Example:
8-bit color: 2^8 = 256  colors
```

- **Image Size(File Size Calculation)/Memory Required for Frame Buffer**

```
The size of an image file depends on its resolution, bit depth, and compression.
Image Size (bytes)/Memory Required = Total Pixels per Frame ✕ Bytes (Bit Depth ÷ 8)
                                   = Width ✕ Height ✕ Bytes (Bit Depth ÷ 8)

Example:
For a 1920 x 1080 image with 24-bit (3 bytes per pixel) color depth:
Image Size = 1920 × 1080 × 3 = 6,220,800 bytes ≈ 5.93 MB
Higher Bit Depth = More Colors, but also more memory usage.
If compressed (e.g., JPEG), the file size is smaller.
```

- **Pixel Density(DPI/PPI)**

```
Pixel density measures how many pixels are packed into a given physical area,
commonly expressed as DPI (Dots Per Inch) or PPI (Pixels Per Inch).

PPI/DPI = Diagonal Resolution (pixels) / Diagonal Screen Size (inches) 
= √(Width^2 + Height^2) / Diagonal Screen Size (inches)

Example:
For a 1920 × 1080 display with a 15.6-inch diagonal screen:
PPI/DPI = 2202.91 / 15.06 PPI = 141 PPI
```

- **Scaling Factor**

```
Scaling is used to adjust the size of UI elements and text on high-DPI displays.
Scaling Factor = Target PPI / Base PPI

Screen Scaling
When scaling is applied, the effective resolution (how content is displayed) changes.
Effective Resolution = Native Resolution / Scaling Factor
```

## Antialiasing

#### I<sub>x,y</sub> = I<sub>max</sub>.dA.Weight

```
dA = area overlap for pixel at (x,y)
Weight = 1 for unweighted area sampling
```
