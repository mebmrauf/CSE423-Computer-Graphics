# **Introduction to Computer Graphics**

## **1. What is Computer Graphics?**
Computer graphics involves creating, storing, and manipulating images and models using computers. It is used in various fields, including engineering, medicine, gaming, and entertainment.

### **Key Points:**
- Coined by **William Fetter** in 1960.
- Used in fields like **mathematics, biology, physics, and arts**.
- Involves both **2D and 3D representations**.

### **Example:**
- Creating a 3D model of a car in **Computer-Aided Design (CAD)**.
- Animating a character in a video game.

---

## **2. Differences Between Related Fields**
| Field | Description | Example |
|--------|----------------|-----------|
| **Computer Graphics** | Creating images from scratch using a computer. | Animated movies, video games. |
| **Computer Vision** | Understanding and extracting information from images. | Face recognition, autonomous driving. |
| **Digital Image Processing** | Manipulating images to enhance or analyze them. | Applying filters, noise reduction. |

---

## **3. Applications of Computer Graphics**
Computer graphics are widely used in different industries:

### **Entertainment**
- **Film & Animation:** Special effects in movies (e.g., Marvel movies).
- **Video Games:** 3D rendering for immersive gaming experiences.

### **Design & Engineering**
- **CAD:** Engineers use it for designing buildings and cars.
- **Product Design:** Visualizing prototypes before manufacturing.

### **Medical Field**
- **Medical Visualization:** MRI and CT scan analysis.
- **Surgical Simulations:** Helps doctors practice complex surgeries.

### **Scientific Research**
- **Data Visualization:** Representing large datasets graphically.
- **Astrophysics:** Simulating black holes, planetary movements.

### **Advertising & Marketing**
- **Graphic Design:** Creating advertisements, logos.
- **3D Product Visualization:** Showing realistic product models online.

---

## **4. Input Methods in Computer Graphics**
Devices used to interact with graphics:

- **Keyboard & Mouse**: Standard input for navigation.
- **Graphics Tablets**: Used for digital drawings.
- **Touchscreens**: Interactive displays (e.g., smartphones).
- **3D Scanners**: Convert real-world objects into digital models.
- **Body Tracking Devices**: Used in gaming (e.g., Xbox Kinect).

---

## **5. Output Devices in Computer Graphics**
Devices used to display graphics:

- **Monitors & Screens**: Standard output devices.
- **Printers**: Convert digital images to physical form.
- **Projectors**: Large-scale display (e.g., classrooms, cinemas).
- **VR/AR Headsets**: Immersive environments.

---

## **6. Graphics Display Hardware**
### **Vector vs. Raster Displays**
| Feature | Vector Display | Raster Display |
|---------|---------------|---------------|
| **Working** | Draws lines directly using an electron beam. | Uses a grid of pixels to form images. |
| **Use Cases** | Technical drawings, CAD. | TV screens, modern monitors. |
| **Pros** | High resolution, scalable. | More realistic images, color support. |
| **Cons** | Limited to line drawings. | Can have pixelation (jagged edges). |

---

## **7. Raster Displays and Frame Buffers**
- **Raster Display:** Stores images as a grid of pixels (bitmaps).
- **Frame Buffer:** Memory storing pixel color data.
- **Bit Depth:** Number of bits per pixel (e.g., 24-bit → 16 million colors).

### **Example:**
A **1920×1080 resolution** image has:
- **2,073,600 pixels**
- If 60 FPS (frames per second), **124 million pixels processed per second**.

---

## **8. Rendering Pipeline**
The process of converting 3D models into 2D images.

### **Steps:**
1. **Vertex Processing & Clipping:** Converts 3D object coordinates to 2D.
2. **Rasterization:** Converts shapes into pixel data.
3. **Fragment Processing:** Adds shading, textures, lighting.
4. **Image Composition:** Combines layers to form the final image.

---

## **9. Modeling vs. Rendering**
| Process | Description | Example |
|---------|------------|---------|
| **Modeling** | Creating objects, applying materials, positioning them. | Designing a 3D house in Blender. |
| **Rendering** | Generating the final 2D image from the 3D scene. | Taking a picture of the 3D house. |

---

## **10. Graphics Computation: Key Concepts**
Here are the formulas for the key concepts related to **Pixel Calculation, Aspect Ratio, Frame Rate (FPS), Pixel Processing Speed, and Image Size** in computer graphics:  

---

## **1. Pixel Calculation (Total Pixels in an Image)**
The total number of pixels in an image is given by:  

\[
\text{Total Pixels} = \text{Width} \times \text{Height}
\]

### **Example:**
For a **1920 × 1080** Full HD image:  

\[
\text{Total Pixels} = 1920 \times 1080 = 2,073,600 \text{ pixels}
\]

---

## **2. Aspect Ratio**
Aspect Ratio is the ratio of an image's width to its height:  

\[
\text{Aspect Ratio} = \frac{\text{Width}}{\text{Height}}
\]

### **Example:**
For a **1920 × 1080** image:  

\[
\text{Aspect Ratio} = \frac{1920}{1080} = 16:9
\]

---

## **3. Frame Rate (FPS)**
Frame rate (Frames Per Second) determines how many images (frames) are displayed per second:  

\[
\text{Frame Time (ms)} = \frac{1}{\text{FPS}} \times 1000
\]

### **Example:**
For **60 FPS**:  

\[
\text{Frame Time} = \frac{1}{60} \times 1000 = 16.67 \text{ ms per frame}
\]

This means each frame must be rendered in **16.67 milliseconds** to maintain 60 FPS.

---

## **4. Pixel Processing Speed**
The number of pixels processed per second can be calculated as:  

\[
\text{Pixels per Second} = \text{Total Pixels per Frame} \times \text{FPS}
\]

If a GPU can process **N pixels per millisecond**, the total pixels it can render per frame is:  

\[
\text{Pixels per Frame} = N \times \text{Frame Time}
\]

### **Example:**
For a **1920 × 1080** image at **60 FPS**:

\[
\text{Pixels per Second} = 2,073,600 \times 60 = 124,416,000 \text{ pixels per second}
\]

If a GPU can process **100,000 pixels per millisecond**:

\[
\text{Pixels per Frame} = 100,000 \times 16.67 = 1,667,000 \text{ pixels per frame}
\]

---

## **5. Image Size (File Size Calculation)**
The size of an image file depends on its resolution, bit depth, and compression.

\[
\text{Image Size (bytes)} = \text{Width} \times \text{Height} \times \text{Bit Depth} \div 8
\]

\[
\text{Image Size (KB)} = \frac{\text{Image Size (bytes)}}{1024}
\]

\[
\text{Image Size (MB)} = \frac{\text{Image Size (KB)}}{1024}
\]

### **Example:**
For a **1920 × 1080** image with **24-bit (3 bytes per pixel) color depth**:

\[
\text{Image Size} = 1920 \times 1080 \times 3 = 6,220,800 \text{ bytes} \approx 5.93 \text{ MB}
\]

If compressed (e.g., JPEG), the file size is smaller.

---

### **Scaling and Pixel Density (DPI/PPI) - Formulas and Explanation**  

---

## **1. Pixel Density (DPI/PPI)**
Pixel density measures how many pixels are packed into a given physical area, commonly expressed as **DPI (Dots Per Inch)** or **PPI (Pixels Per Inch)**.

\[
\text{PPI} = \frac{\text{Diagonal Resolution (pixels)}}{\text{Diagonal Screen Size (inches)}}
\]

where  
- **Diagonal Resolution** = \( \sqrt{(\text{Width}^2 + \text{Height}^2)} \) in pixels  
- **Diagonal Screen Size** is the physical size of the screen in inches.

### **Example:**  
For a **1920 × 1080** display with a **15.6-inch diagonal** screen:  
1. Calculate **diagonal resolution**:

\[
\text{Diagonal Resolution} = \sqrt{(1920^2 + 1080^2)}
\]

\[
= \sqrt{3686400 + 1166400} = \sqrt{4852800} \approx 2202.91 \text{ pixels}
\]

2. Calculate **PPI**:

\[
\text{PPI} = \frac{2202.91}{15.6} \approx 141 \text{ PPI}
\]

Thus, this screen has **141 pixels per inch**.

---

## **2. Scaling Factor**
Scaling is used to adjust the size of UI elements and text on high-DPI displays.

\[
\text{Scaling Factor} = \frac{\text{Target PPI}}{\text{Base PPI}}
\]

### **Example:**  
If the base PPI is **96 PPI** (standard for many displays) and the target display has **192 PPI**:

\[
\text{Scaling Factor} = \frac{192}{96} = 2.0 \text{ (200% scaling)}
\]

At **200% scaling**, elements appear twice as large to maintain readability.

---

## **3. Screen Scaling**
When scaling is applied, the **effective resolution** (how content is displayed) changes.

\[
\text{Effective Resolution} = \frac{\text{Native Resolution}}{\text{Scaling Factor}}
\]

### **Example:**  
For a **3840 × 2160 (4K)** display at **150% scaling**:

\[
\text{Effective Resolution} = \frac{3840}{1.5} \times \frac{2160}{1.5} = 2560 \times 1440
\]

Thus, UI elements will appear as if they are on a **2560 × 1440** screen.

---

## **11. Antialiasing**
Reduces jagged edges (aliasing) in graphics.

### **Techniques:**
1. **Increase Resolution**: More pixels reduce jagged lines (costly).
2. **Area Sampling**: Smoothens edges by averaging pixel colors.

### **Example:**
- **Without Antialiasing:** Jagged edges on diagonal lines.
- **With Antialiasing:** Smooth edges with blended colors.

---

# **Summary**
1. **Computer Graphics** creates and manipulates images.
2. It differs from **Computer Vision** (image analysis) and **Image Processing** (enhancement).
3. **Applications** include entertainment, medicine, research, and advertising.
4. **Input methods** (mouse, touchscreen) and **output devices** (monitors, VR headsets) enable interaction.
5. **Vector vs. Raster Displays:** Vector is scalable, raster is pixel-based.
6. **Rendering Pipeline** converts 3D models into final images.
7. **Graphics Computation** involves FPS, pixel processing, and resolution.
8. **Antialiasing** smoothens jagged edges for better visuals.

These notes provide a structured and detailed explanation of the topics. Let me know if you need further clarifications!