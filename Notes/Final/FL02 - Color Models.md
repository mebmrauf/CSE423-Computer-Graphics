# Color Models
A color model is a specification of a coordinate system and a subspace within that system where each color is represented by a single point.

### Achromatic or Monochrome

- Basically it’s Black and White color
- Different intensities of grey
- RGB values are equal (R = G = B)
- Lack of hue (pure color), saturation (intensity of a color) and brightness
- Only measured using the quantity of light

Range of visible light : 380nm (blue)  - 780nm (red)

### Color Gamut
The color gamut describes a range of colors within the spectrum of colors, or a color space, that can be reproduced on an output device. Depending on how wide the gamut is, every screen will display different quantities of color. 

## RGB

`RGB = Red, Green, Blue`

**Additive Color** - begins with black and ends with white.

RGB color model applies additive model.

Used for active displays such as television and computer screens.

![Screenshot 2025-05-16 at 5.03.12 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.03.12_PM.png)

`Origin (0, 0, 0) is black and diagonal opposite (1, 1, 1) is white. The line joining black to white represents a gray scale and has R=G=B.`

## CMY

`CMY = Cyan, Magenta, Yellow`

```jsx
Cyan = Green + Blue = (0, 1, 1)
Magenta = Red + Blue = (1, 0, 1)
Yellow = Red + Green = (1, 1, 0)
```

**Subtractive Color** - begins with white and ends with black.

CMY color model applies subtractive model.

Color printers or copiers requires CMY data.

![Screenshot 2025-05-16 at 5.03.28 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.03.28_PM.png)

```jsx
C = 1 - R
M = 1 - G
Y = 1 - B
```

`Combining CMY color produces a “Muddy-Black” color. So CMYK color model is used, where K = True Black.`

## RGB to CMY

![Screenshot 2025-05-16 at 5.04.02 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.04.02_PM.png)

## HSV

`HSV = Hue, Saturation, Value`

### Application

- Widely used in computer graphics for intuitive color selection in tools like color pickers and gradient design.
- It aids in image processing tasks such as color-based filtering, segmentation, and thresholding.
- In shading, lighting, and special effects, HSV simplifies dynamic adjustments and smooth color transitions.
- It's critical for color grading in video editing and data visualization, mapping values to colors effectively.
- Additionally, HSV is essential in gaming, AR/VR, and AI applications, where it supports object highlighting, procedural content generation, and feature extraction.

![Screenshot 2025-05-16 at 5.04.32 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.04.32_PM.png)

Hue → color wheel/dominant color

- More than **400 hues** can be seen by the human eye.

Saturation → percentage/purity of the color

- A pure color has 100% saturation, the white and grey have 0% saturation.
- About 20 saturation levels are visible per hue.

Value → brightness or intensity of a color

- Helps in generating shading or lighting effects in graphics.

## RGB to HSV

- Divide r, g, b by 255 (if the scale is 0-255, otherwise skip)
- Compute cmax, cmin, difference
    
    ```jsx
    RGB = (r, g, b)
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    difference = cmax - cmin
    ```
    
- Hue calculation :
    
    ```jsx
    if cmax = 0, then h = 0
    if cmax = r then h = (g – b) / diff
    if cmax = g then h = 2 + (b – r) / diff
    if cmax = b then h = 4 + (r – g) / diff
    
    h = h * 60
    if h<0 → h = h + 360
    ```
    
- Saturation computation :
    
    ```jsx
    if cmax = 0, then s = 0
    if cmax != 0 then s = diff / cmax
    ```
    
- *Value Computation:*
    
    ```jsx
    v = cmax
    ```
    

![Screenshot 2025-05-16 at 5.05.03 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.05.03_PM.png)

## HSV to RGB

`H = Hue, S = Saturation, V = Value`

- Chromatic Component (C )
It represents the difference between the maximum and minimum RGB components
`C = V × S`
- Intermediate Value (X)
`X = C × ( 1 − abs((H/60 mod 2 ) − 1 ))`
- Adjustment (m)
It shifts the RGB values to match the value V (the maximum component)
`m = V − C`
- Assign RGB Values Based on Hue (H)
    
    ![Screenshot 2025-05-16 at 5.05.53 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.05.53_PM.png)
    
    ### **Way to Remember**
    
    ![Screenshot 2025-05-16 at 5.04.50 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.04.50_PM.png)
    
    ```jsx
    RGB = Red(R), Green(G), Blue(B)
    - Find nearest RGB color (forward)
        - nearest color = C
    - Find next nearest color (forward / backward)
        - next nearest color = X
    - Another color = 0
    
    `0 <= H < 60`
    
    - R = C, G = X, B = 0
    
    `60 <= H < 120`
    
    - R = X, G = C, B = 0
    
    `120 <= H < 180`
    
    - R = 0, G = C, B = X
    
    `180 <= H < 240`
    
    - R = 0, G = X, B = C
    
    `240 <= H < 300`
    
    - R = X, G = 0, B = C
    
    `300 <= H < 360`
    
    - R = C, G = 0, B = X
    
    © Azmari Sultana
    ```
    
- Adjustment
    
    Adjust the RGB values to match the original value (V)
    
    `R’=(R+m), G’=(G+m), B’=(B+m)`
    

![Screenshot 2025-05-16 at 5.06.03 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.06.03_PM.png)

## HLS

`HLS = Hue, Lightness, Saturation`

```jsx
Hue: Angle on the color wheel (e.g., 0° = red, 120° = green, 240° = blue)
Lightness: 0=black,1=white,0.5=pure color
Saturation: 0=gray,1=fully vivid color
```

**Application →** Image editing, color pickers, and design tools. Useful for adjusting brightness without altering color hue.

![Screenshot 2025-05-16 at 5.06.16 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.06.16_PM.png)

![Screenshot 2025-05-16 at 5.06.29 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.06.29_PM.png)

## RGB to HLS

- Normalise
- Compute cmax, cmin, difference
    
    ```jsx
    RGB = (r, g, b)
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    difference = cmax - cmin
    ```
    
- `L = (cmax + cmin) / 2`
- Hue calculation
    
    ```jsx
    if diff = 0, then H = 0
    if cmax = r then H = (g – b) / diff
    if cmax = g then H = 2 + (b – r) / diff
    if cmax = b then H = 4 + (r – g) / diff
    
    H = H * 60
    if H < 0 → H = H + 360
    ```
    
- Saturation computation :
    
    ```jsx
    if diff = 0, then S = 0
    if L <= 0.5 → S = diff / (cmax + cmin)
    if L > 0.5 → S = diff / [2- (cmax + cmin)]
    ```
    

![Screenshot 2025-05-16 at 5.06.46 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.06.46_PM.png)

## Problem Solving

**Note: There could be errors in the solution. Please double-check it.**

### Problem 01

**Rachel, a game developer, is customizing magical glow effects in a fantasy game using a shader editor that supports both HSL and HSV color models. She notices that while the same Hue value gives similar colors in both, adjusting Saturation and Lightness/Value produces different results. Create a labeled diagram that visually represents the HSL color model. Describe the key differences between HSL and HSV in how they define and control color. Additionally, identify whether the HSL and HSV color models use the same formula for calculating Hue.**

**HSL Color Diagram**

![Screenshot 2025-05-16 at 5.06.16 PM.png](FL02%20-%20Color%20Models/Screenshot_2025-05-16_at_5.06.16_PM.png)

**Saturation Differences**

In HSV, saturation represents how pure or vivid a color appears - 100% saturation gives you the most intense, pure color possible, while 0% gives you gray.

In HSL, saturation works differently: it measures how far the color deviates from gray at that particular lightness level. This means a color can appear quite vivid in HSL even at moderate saturation values, depending on the lightness setting.

**Brightness Control Differences**

HSV's "Value" represents the overall brightness or intensity of the color. At 100% value, you get the brightest possible version of that hue and saturation. At 0% value, everything becomes black regardless of hue or saturation.

HSL's "Lightness" works more intuitively for many applications. At 50% lightness, you get the "pure" color. At 100% lightness, everything becomes white, and at 0% lightness, everything becomes black.

**Hue Calculation**

Yes, both HSL and HSV use identical formulas for calculating Hue. The hue component is derived the same way in both models - it's based on which RGB component is dominant and the relationships between the RGB values. This is why the same hue value produces visually similar colors in both models. The hue represents the color's position on the color wheel (0-360 degrees), and this fundamental measurement remains consistent across both systems. Only difference is in HSV, if cmax = 0, hue = 0 and in HSL, if difference(cmax - cmin) = 0, hue = 0.

### Problem 02

**HSV = (45°, 0.8. 0.9), convert it to RGB.**

**HSV to RGB conversion**

```jsx
H = 45°, S = 0.8, V = 0.9

C = V × S = 0.9 × 0.8 = 0.72

X = C × (1 - |((H/60) mod 2) - 1|)
=> 0.72 × (1 - |0.75 - 1|)
=> 0.72 × 0.75 = 0.54

m = V - C = 0.9 - 0.72 = 0.18

Since H = 45° is in the range 0° <= H < 60°:

R = C + m = 0.72 + 0.18 = 0.90
G = X + m = 0.54 + 0.18 = 0.72
B = 0 + m = 0.18

RGB = (0.90, 0.72, 0.18)
```

### Problem 03

**CMY = (0.3, 0.4, 0.2), convert it to RGB.**

**CMY to RGB conversion**

```jsx
R = 1 - C, G = 1 - M, B = 1 - Y

R = 1 - 0.3 = 0.7
G = 1 - 0.4 = 0.6
B = 1 - 0.2 = 0.8

RGB = (0.7, 0.6, 0.8)
```