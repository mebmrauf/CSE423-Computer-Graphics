# Vector Display vs. Raster Display

## Vector Display Architecture

```
     --------------------------
|--->|     Host Computer      |<---------|
|    --------------------------          |
|                                |-------|
|                                |
|    --------------------------  |   ------------------------
|    |     1. MOVE 10, 10     |  |-->|                      |----|
|    |     2. LINE 10, 100    |----->|  Display Controller  |    |
|    |     3. LINE 100, 10    |      ------------------------    |
|--->|     4. LINE 10, 10     |                                  |
     |     5. GOTO 1          |     ------------------------     |
     |                        |     |    -------------     |     |
     --------------------------     |    |   |\       |    |<----|
                                    |    |   | \      |    |
                                    |    |   |  \     |    |
                                    |    |   |   \    |    |
                                    |    |   |    \   |    |
                                    |    |   |     \  |    |
                                    |    |   -------  |    |
                                    |    --------------    |
                                    ------------------------
```

## Raster Display Architecture

```
     --------------------------
|--->|     Host Computer      |<---------|
|    --------------------------          |
|                                |-------|
|                                |
|    --------------------------  |   ------------------------
|    |     10000000000000     |  |-->|                      |----|
|    |     10000000000000     |----->|   Video Controller   |    |
|    |     10100000000000     |      ------------------------    |
|--->|     10010000000000     |                                  |
     |     11111000000000     |     ------------------------     |
     |                        |     |    -------------     |     |
     --------------------------     |    |   |\       |    |<----|
                                    |    |   | \      |    |
                                    |    |   |  \     |    |
                                    |    |   |   \    |    |
                                    |    |   |    \   |    |
                                    |    |   |     \  |    |
                                    |    |   -------  |    |
                                    |    --------------    |
                                    ------------------------
```

## Feature Comparison

| Feature         | Vector Display                                      | Raster Display                                     |
|---------------|------------------------------------------------|------------------------------------------------|
| **Working**    | Drawing lines directly using an electron beam  | Uses a grid of pixels to form images.          |
| **Use Cases**  | Calligraphic, Stroke, Random-scan, Technical drawings, CAD. | TV screens, modern monitors, bitmap, pixmap, laser printers. |
| **Pros**       | High resolution, scalable, sharp lines without pixelation. | More realistic images, rich color support, better for detailed textures. |
| **Cons**       | Limited to line drawings, not ideal for complex images. | Can have pixelation (jagged edges), resolution dependent. |
| **Key Differences** | Shape-based, resolution-independent, best for scalable designs like fonts and logos. | Pixel-based, fixed resolution, more common in displays, better for detailed and realistic images. |

## Key Terms in Raster Displays

- **Raster:** A rectangular grid of points or dots.
- **Pixel (Pel):** The smallest part of a digital image, each representing a single color.
- **Pixel Grid:** A structured grid where each pixel holds color data (e.g., RGB values).
- **Scan Line:** A horizontal row of pixels in a raster display.
- **Bitmap:** A collection of pixels forming an image. Formats include .bmp, .png, .jpg.
- **Frame Buffer:** A memory space that stores the pixel data to be displayed.
- **Resolution** defines the number of pixels in the display (e.g., 1024×1024 pixels).
- **Bit Depth (Bit Planes)** determines color accuracy.

## Formulas

```
Colors Available Based on Bit Depth:
Colors Available = 2^Bit Depth
Example:
8-bit color: 2^8 = 256  colors
```

```
Memory Required for Frame Buffer:
Memory Required = Resolution (Width ✕ Height) ✕ Bytes (Bit Depth ÷ 8) 
Example:
For a 1920 × 1080 resolution image with 24-bit color (3 bytes per pixel):
Memory Required = 1920 ✕ 1080 ✕ 3 = 6220800 bytes ≈ 5.93 MB
Higher Bit Depth = More Colors, but also more memory usage.
```

# Rendering Pipeline
The Rendering Pipeline is the process of converting 3D models into 2D images for display. It consists of several key stages:

- Vertex Processing & Clipping
     - Transforms 3D object coordinates into screen coordinates using model and view transformations.
     - Removes objects or parts of objects outside the camera's field of view (clipping).
- Rasterization
     - Converts 3D shapes into a 2D pixel grid, determining which pixels correspond to which objects.
- Fragment Processing
     - Applies visual effects such as shading, textures, and lighting to individual pixels (fragments).
- Image Composition & Output Merging
     - Combines multiple layers and objects into a final rendered image, ready for display.

## Steps
```
Raw Vertices & Primitives ===>>> Vertex Processor (Programmable) == Transformed Vertices & Primitives ===>>> Rasterizer == Fragments ===>>> Fragment Processor (Porgrammable) == Processed Fragments ===>>> Output Merging == Pixels ===>>> Display
```
