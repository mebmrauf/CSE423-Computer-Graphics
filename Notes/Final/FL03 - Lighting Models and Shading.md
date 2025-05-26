# Lighting Models and Shading

![Screenshot 2025-05-16 at 8.23.46 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_8.23.46_PM.png)

## Ambient Light

- No identifiable source or direction
- Product of multiple reflections of light from the many surfaces present in the environment
- Computationally inexpensive
    
    ![Screenshot 2025-05-16 at 8.24.40 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_8.24.40_PM.png)
    

## Diffuse Reflection

- Result of irregular reflection of light
- Light is scattered in all direction. Not all are visible
- Does Not depend on the position of viewpoint
- Light reflected equally in all direction.
- Magnitude of reflection depends in incident angle.
    
    ![Screenshot 2025-05-16 at 8.35.56 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_8.35.56_PM.png)
    
    ![Screenshot 2025-05-16 at 11.31.38 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.31.38_PM.png)
    
    ![Screenshot 2025-05-16 at 11.31.53 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.31.53_PM.png)
    

## Specular Reflection

- Reflection is only at mirror angle. An ideal mirror is a purely specular reflector.
- View dependent reflection. That is, reflected light’s intensity varies with viewer’s position.
- Intensity of reflected light is stronger near mirror angle and strongest at mirror angle.
- An Ideal specular reflection follows Snell’s Law →
    - The incoming ray and reflected ray lie in a plane with the surface normal
    - The angle that the reflected ray forms with the surface normal equals the angle formed by the incoming ray and the surface normal

![Screenshot 2025-05-16 at 11.32.39 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.32.39_PM.png)

![Screenshot 2025-05-16 at 11.33.33 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.33.33_PM.png)

![Screenshot 2025-05-16 at 11.34.15 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.34.15_PM.png)

![Screenshot 2025-05-16 at 11.34.36 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.34.36_PM.png)

### Blinn and Torrence Variation

- Calculation of R is computationally expensive. So in phong model the term R.V is sometimes replaced by N.H , where H is a unit vector that bisect the angle between L and V.
- Angle between N and H measures the fall off of intensity.
- Though calculation of N.H is is computationally inexpensive relative to R.V, but N.H is not always equal to R.V. In that case calculation of specular component will be approximate.

![Screenshot 2025-05-16 at 11.35.07 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.35.07_PM.png)

## **Comparison of Ambient, Diffuse, and Specular Reflection**

| **Aspect** | **Ambient Reflection** | **Diffuse Reflection** | **Specular Reflection** |
| --- | --- | --- | --- |
| **Source & Direction** | Has no specific source or direction — it’s the result of light bouncing around the environment. | Comes from light hitting a rough surface and scattering in all directions. | Comes from light hitting a smooth surface and reflecting mainly in one direction (mirror-like). |
| **Surface Dependency** | Doesn’t depend on the surface shape or angle. | Depends on the surface's angle relative to the light source (normal vector). | Depends on the angle of the surface **and** the viewer’s position. |
| **Viewpoint Dependency** | Always looks the same, no matter where the viewer is. | Looks the same from any angle — not affected by viewer position. | Changes based on where the viewer is — produces highlights that move with the viewer. |
| **Visual Effect** | Adds a general brightness to make sure objects aren’t completely dark. | Gives the surface a matte or dull look — shows the shape of the object. | Creates shiny highlights — makes the surface look glossy or polished. |
| **Reflection Pattern** | Light is scattered evenly across the scene. | Light is scattered randomly due to a rough surface. | Light is reflected sharply in a single direction, near the mirror angle. |
| **Computation Cost** | Very simple and fast to calculate — often constant. | Slightly more complex — needs normal and light direction. | Most complex — needs surface normal, light direction, viewer direction, and shininess. |

![Screenshot 2025-05-16 at 11.35.17 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.35.17_PM.png)

![Screenshot 2025-05-16 at 11.35.45 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.35.45_PM.png)

![Screenshot 2025-05-16 at 11.36.08 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.36.08_PM.png)

![Screenshot 2025-05-16 at 11.36.48 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.36.48_PM.png)

![Screenshot 2025-05-16 at 11.37.05 PM.png](FL03%20-%20Lighting%20Models%20and%20Shading/Screenshot_2025-05-16_at_11.37.05_PM.png)

## Shading

![Lighting.pptx-images-42.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-42.jpg)

![Lighting.pptx-images-43.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-43.jpg)

![Lighting.pptx-images-44.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-44.jpg)

![Lighting.pptx-images-45.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-45.jpg)

![Lighting.pptx-images-46.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-46.jpg)

![Lighting.pptx-images-47.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-47.jpg)

![Lighting.pptx-images-48.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-48.jpg)

![Lighting.pptx-images-49.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-49.jpg)

![Lighting.pptx-images-50.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-50.jpg)

![Lighting.pptx-images-51.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-51.jpg)

![Lighting.pptx-images-52.jpg](FL03%20-%20Lighting%20Models%20and%20Shading/Lighting.pptx-images-52.jpg)


## Problem Solving

### Problem 01

**In a 3D modeling software, Rachel is applying color to a rectangular panel. The rectangle is defined by the vertices A(-400, 500), B(400, 500), C(400, 300), and D(-400, 300). Let point P be the centroid of the rectangle. The color at vertex A is specified using the RGB color model with values (0.90, 0.72, 0.18), and the color at vertex C is (0.7, 0.6, 0.8). Using Gouraud shading, compute the interpolated color at point P.**

```jsx
The centroid of rectangle ABCD is:
P = ((x₁ + x₂ + x₃ + x₄)/4, (y₁ + y₂ + y₃ + y₄)/4)
P = ((-400 + 400 + 400 + (-400))/4, (500 + 500 + 300 + 300)/4)
P = (0, 400)

In Gouraud shading, we need to determine what colors are at vertices.
Since only A and C are specified,
we're interpolating between the two diagonal vertices A and C.

The interpolation at the centroid would be:
Color at P = (Color at A + Color at C) / 2

Calculate interpolated RGB at P
R = (0.90 + 0.7) / 2 = 0.80
G = (0.72 + 0.6) / 2 = 0.66
B = (0.18 + 0.8) / 2 = 0.49

The interpolated color at point P is (0.80, 0.66, 0.49).
```

### Problem 02

**Matt Murdock is on a mission and hides behind his glossy red sports car at night. An enemy is nearby, and the only light source is an orange streetlamp. To spot the enemy without revealing his position, Matt considers using one of three small mirrors with shininess values of 1, 20, and 50 H also notices that parts of his red car appear to have orange highlights under the street lamp. Which mirror should Matt use to best locate the enemy? Justify your choice using Phong's reflection model In addition, state the reason why the red car displays orange highlights under the orange street lamp.**

**Best Mirror Choice**

Matt should use the mirror with shininess = 20. It provides the optimal balance - sharp enough for clear enemy detection but not so focused that it misses the target if positioning isn't perfect.

**Why Red Car Shows Orange Highlights**

The car's glossy surface creates specular reflections that directly mirror the orange streetlight color, while the diffuse reflections maintain the car's red paint color. In Phong's model, specular highlights take on the light source color regardless of the object's base color.

## Problem 03

**Matt Murdock is now designing the lighting for a 3D simulation inside a small room, with the xy plane acting as the floor. A perfect sphere with a radius of 1 unit and shininess 5 is placed in the room with its center at (4, 5.5). To give an 80s feel, he decides to use only grayscale light sources He placed a backlight at (0, 8, 8) with source intensity 0.9, diffuse coefficient 0.5, and speculo coefficient 0.6. Matt is also trying to place a floor light at (4, 2,3) with source intensity 0.8. diffuse coefficient 0.4, and specular coefficient 0.7. All sources have a sphere of influence of 5 units. The ambient light intensity and coefficient are both 0.4. Can you help Matt by calculating the total reflected light intensity at the very topmost point of the sphere, if he places the camera at the point (6, 3, 7)? Use the Phong Reflection Model to calcutate this intensity.**

**[Hint. Calculate the attenuation factor first.]**

```jsx
Step01 : Identify key points

Sphere center: (4, 5, 5)
Sphere radius: 1 unit
Topmost point of sphere: (4, 5, 6) [center + radius in z-direction]
Camera position: (6, 3, 7)
Backlight position: (0, 8, 8)
Floor light position: (4, 2, 3)


Step02 : Calculate distances and check sphere of influence

Backlight to topmost point:
Distance = √[(4-0)² + (5-8)² + (6-8)²] = √[16 + 9 + 4] = √29 ≈ 5.39 units
Since 5.39 > 5 units (sphere of influence), the backlight doesn't affect this point.

Floor light to topmost point:
Distance = √[(4-4)² + (5-2)² + (6-3)²] = √[0 + 9 + 9] = √18 ≈ 4.24 units
Since 4.24 < 5 units, the floor light affects this point.


Step03 : Calculate attenuation factor for floor light

Attenuation = max(0, 1 - (distance/sphere_of_influence)²)
Attenuation = max(0, 1 - (4.24/5)²) = max(0, 1 - 0.719) = 0.281


Step04 : Calculate vectors for floor light

Light vector (L): From topmost point to floor light
L = (4-4, 2-5, 3-6) = (0, -3, -3)
|L| = √(0 + 9 + 9) = √18 ≈ 4.24
L̂ = (0, -3/4.24, -3/4.24) = (0, -0.707, -0.707)

Normal vector (N): At topmost point of sphere
N̂ = (0, 0, 1) [pointing upward]

View vector (V): From topmost point to camera
V = (6-4, 3-5, 7-6) = (2, -2, 1)
|V| = √(4 + 4 + 1) = 3
V̂ = (2/3, -2/3, 1/3)

Reflection vector (R): R = 2(N̂·L̂)N̂ - L̂
N̂·L̂ = (0)(0) + (0)(-0.707) + (1)(-0.707) = -0.707
R = 2(-0.707)(0, 0, 1) - (0, -0.707, -0.707)
R = (0, 0, -1.414) - (0, -0.707, -0.707) = (0, 0.707, -0.707)


Step05 : Calculate Phong components

Ambient component:
Ia = ambient_intensity × ambient_coefficient = 0.4 × 0.4 = 0.16

Diffuse component:
Id = light_intensity × diffuse_coef × max(0, N̂·L̂)
Id = 0.8 × 0.4 × max(0, -0.707) = 0.8 × 0.4 × 0 = 0
(Since N̂·L̂ < 0, the light is hitting the surface from below)

Specular component:
Is = light_intensity × specular_coef × max(0, R̂·V̂)ⁿ
R̂·V̂ = (0)(2/3) + (0.707)(-2/3) + (-0.707)(1/3) = 0 - 0.471 - 0.236 = -0.707
Is = 0.8 × 0.7 × max(0, -0.707)⁵= 0
(Since R̂·V̂ < 0, there's no specular reflection toward the camera)


Step 6: Total reflected light intensity
Total intensity = Ia + attenuation × (Id + Is) = 0.16 + (0.281 × 0) = 0.16

Answer: The total reflected light intensity at the topmost point of the sphere is 0.16 units.
```