# Vector Display vs. Raster Display

## Vector Display Architecture

```
     --------------------------
|--> |     Host Computer      |
|    --------------------------
|    --------------------------
|    |     1. MOVE 10, 10     |
|    |     2. LINE 10, 100    |
|--> |     3. LINE 100, 10    |
     |     4. LINE 10, 10     |
     |     5. GOTO 1          |
     --------------------------
```

## Feature Comparison

| Feature         | Vector Display                                      | Raster Display                                     |
|---------------|------------------------------------------------|------------------------------------------------|
| **Working**    | Drawing lines directly using an electron beam  | Uses a grid of pixels to form images.          |
| **Use Cases**  | Calligraphic, Stroke, Random-scan, Technical drawings, CAD. | TV screens, modern monitors, bitmap, pixmap, laser printers. |
| **Pros**       | High resolution, scalable, sharp lines without pixelation. | More realistic images, rich color support, better for detailed textures. |
| **Cons**       | Limited to line drawings, not ideal for complex images. | Can have pixelation (jagged edges), resolution dependent. |
| **Key Differences** | Shape-based, resolution-independent, best for scalable designs like fonts and logos. | Pixel-based, fixed resolution, more common in displays, better for detailed and realistic images. |
