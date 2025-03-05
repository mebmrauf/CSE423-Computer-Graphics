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
        Raw Vertices
        & Primitives
              |
              |
------------------------------------
|  Vertex Processor(Programmable)  |
------------------------------------
              |
              |
     Transformed Vertices
        & Primitives
              |
              |
------------------------------------
|         Rasterizer               |
------------------------------------
              |
              |
          Fragments
              |
              |
------------------------------------
| Fragment Processor(Porgrammable) |
------------------------------------
              |
              |
     Processed Fragments
              |
              |
------------------------------------
|        Output Merging            |
------------------------------------
              |
              |
            Pixels
              |
              |
------------------------------------
|           Display                |
------------------------------------
```

# Modeling vs. Rendering

## Process Comparison

| Process    | Description                                           | Example                                      |
|------------|------------------------------------------------------|----------------------------------------------|
| **Modeling**  | Creating objects, applying materials, positioning them. | Designing a 3D house in Blender.            |
| **Rendering** | Generating the final 2D image from the 3D scene.   | Taking a picture of the 3D house.           |

# Antialiasing

Antialiasing is a technique used to reduce jagged edges (aliasing) in digital graphics, making images appear smoother and more visually appealing.

## What is Aliasing?
Aliasing occurs when a continuous object, like a diagonal line or curve, is represented using discrete pixels. This results in a **staircasing effect (jagged edges)** due to the "all-or-nothing" approach of pixel coloring, each pixel is either filled completely or left blank.

## Antialiasing Techniques

- Increasing Resolution
     - More pixels per unit area reduce jagged lines.
     - Costly in terms of memory and processing power.
     - Improves smoothness but does not fully eliminate aliasing.
- Area Sampling (Supersampling)
     - Instead of treating each pixel as a single point, it is considered a small area.
     - The color of a pixel is determined based on how much of it is covered by the object.
     - **Unweighted Area Sampling** a pixel’s intensity is proportional to the fraction of its area covered by the object.
     - **Weighted Area Sampling** uses a weighting function to give more importance to the center of the pixel for smoother transitions.
- Example
     - **Without Antialiasing** A diagonal line appears jagged, with visible staircasing.
     - **With Antialiasing** The edges of the line are blended with nearby pixels, creating.
