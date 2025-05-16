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
