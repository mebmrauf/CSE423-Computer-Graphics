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
### **1. Pixel Calculation**
\[\text{Total Pixels} = \text{Width} \times \text{Height}\]

### **2. Aspect Ratio**
\[\text{Aspect Ratio} = \frac{\text{Width}}{\text{Height}}\]

### **3. Frame Rate (FPS)**
\[\text{Frame Time (ms)} = \frac{1}{\text{FPS}} \times 1000\]

### **4. Pixel Processing Speed**
\[\text{Pixels per Second} = \text{Total Pixels per Frame} \times \text{FPS}\]

### **5. Image Size Calculation**
\[\text{Image Size (bytes)} = \text{Width} \times \text{Height} \times \text{Bit Depth} \div 8\]

---

## **11. Antialiasing**
Reduces jagged edges (aliasing) in graphics.

### **Techniques:**
1. **Increase Resolution**: More pixels reduce jagged lines (costly).
2. **Area Sampling**: Smoothens edges by averaging pixel colors.

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