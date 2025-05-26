# Projection

Converting points from n dimension to m dimension, where m < n.

```
P(x, y, z) ——Projection—— P(x', y')
```

## Types

- Planar
    - Perspective
    - Parallel
        - Orthographic
        - Oblique
            - Cabinet
            - Cavalier

## Perspective vs Parallel Projection

### 1. Perspective Projection

**Definition**: A projection where lines of sight (projectors) converge at a single point called COP (the viewer’s eye or camera).

COP - Center of Projection

#### Characteristics:

- **Mimics human vision** – things look smaller as they get farther away.
- **Has a vanishing point** – parallel lines appear to converge.
- **Depth is realistic** – good for rendering real-world scenes (e.g., video games, 3D animation).
- **Non-uniform scale** – objects farther away are scaled down more.

#### Example Use:

- Video Games
- Animation
- Virtual Reality(VR)

---

### 2. Parallel Projection

**Definition**: A projection where the lines of sight (projectors) are parallel to each other and perpendicular (orthographic) or angled (oblique) to the projection plane.

#### Characteristics:

- **No perspective distortion** – objects stay the same size regardless of depth.
- **No vanishing point** – parallel lines remain parallel.
- **More technical/diagrammatic** – ideal for architectural planning and design.
- **Uniform scale** – good for precise measurements.

#### Types:

- **Orthographic Projection** – projectors are perpendicular to the projection plane. the DOP is equal to the normal vector of the plane.
- **Oblique Projection** – projectors are at an angle to the projection plane. the DOP is not equal to the normal vector of the plane.

#### Example Use:

- Engineering and architectural drawings
- CAD software
- Blueprints and schematics

---

### Quick Comparison Table

| Feature | Perspective Projection | Parallel Projection |
| --- | --- | --- |
| Projector lines | Converging | Parallel |
| Depth perception | Realistic | Flattened |
| Scale | Non-uniform | Uniform |
| Vanishing point | Yes | No |
| Application | Visual realism | Technical accuracy |

---

## Parallel Projection

![Screenshot 2025-04-17 at 11.58.56 AM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_11.58.56_AM.png)

![Screenshot 2025-04-17 at 11.59.14 AM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_11.59.14_AM.png)

![Screenshot 2025-04-17 at 11.59.31 AM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_11.59.31_AM.png)

Matrix Representation

![Screenshot 2025-04-17 at 12.05.22 PM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_12.05.22_PM.png)

![Screenshot 2025-04-17 at 12.08.35 PM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_12.08.35_PM.png)

![Screenshot 2025-04-17 at 12.09.49 PM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_12.09.49_PM.png)

![Screenshot 2025-04-17 at 12.14.03 PM.png](FL01%20-%20Projection/Screenshot_2025-04-17_at_12.14.03_PM.png)

![Screenshot_2025-05-16_at_12.02.17_PM.png](FL01%20-%20Projection/Screenshot_2025-05-16_at_12.02.17_PM.png)

## Perspective Projection

### Simple Purpose

![Screenshot 2025-04-18 at 5.07.16 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.07.16_PM.png)

![Screenshot 2025-04-18 at 5.07.30 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.07.30_PM.png)

![Screenshot 2025-04-18 at 5.07.45 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.07.45_PM.png)

![Screenshot 2025-04-18 at 5.08.10 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.08.10_PM.png)

When COP at origin

![Screenshot 2025-04-18 at 5.15.53 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.15.53_PM.png)

![Screenshot 2025-04-18 at 5.16.08 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.16.08_PM.png)

When Projection Plane(PP) at origin

![Screenshot 2025-04-18 at 5.16.23 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.16.23_PM.png)

![Screenshot 2025-04-18 at 5.16.40 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.16.40_PM.png)

### General Purpose

![Screenshot 2025-04-18 at 7.24.30 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_7.24.30_PM.png)

![Screenshot 2025-04-18 at 5.42.56 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.42.56_PM.png)

![Screenshot 2025-04-18 at 5.43.22 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_5.43.22_PM.png)

![Screenshot 2025-04-18 at 7.26.03 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_7.26.03_PM.png)

![Screenshot 2025-04-18 at 7.26.25 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_7.26.25_PM.png)

![Screenshot 2025-04-18 at 7.26.35 PM.png](FL01%20-%20Projection/Screenshot_2025-04-18_at_7.26.35_PM.png)


```
- Project a point, P' = M * P
- Find COP, M * COP = 0
```

## Problem Solving

**Note: There may be errors in the solution. Please double-check it.**

### Problem 01

A designer is creating a technical drawing of a mechanical part. In the drawing, the front face of the object is shown in true shape and size, while the depth is represented along lines receding at 45° to the horizontal, and the depth dimensions are kept at full scale. Identify which type of parallel projection is being used, and justify your answer with two characteristics of this projection type. What would change in the drawing if the depth axis were scaled to half its actual length?

**Projection Type :** This is Cavalier Projection, a type of oblique parallel projection.

**Two Characteristics that Justify this**

- True shape and size of front face - The front face appears without any distortion or foreshortening, maintaining its actual proportions.

- Full-scale depth dimensions - The receding lines maintain 100% of their true length along the 45° depth axis.

**If depth axis were scaled to half length**

The projection would become Cabinet Projection instead of Cavalier Projection. The drawing would appear more natural and less distorted because the excessive depth that makes Cavalier projections look stretched would be reduced, creating a more visually pleasing representation of the mechanical part.

## Problem 02

While studying late at night for the CSE423 final, you realize it is gently raining outside through your glass window. The window is standing at z =-250. You look through the window down at a flower shop across the street, where a flower, for its unique colour, catches your attention. If a line segment is drawn starting from one side of the shop, (100, 100, -350), and ending at the other side (500, 80, -350), the flower's position, P, falls on this line segment's 80% of the way. From where you are standing, the x and y coordinates of your eye are (60, 200). The z distance between you and the glass window is 1/5th of the z distance between the window and the flower. Find the flower's projected coordinate, P', on the window.

```jsx
Step 1: Identify the projection parameters
Eye position: (60, 200, -230)
Window (projection plane): z = -250
Flower position: (420, 84, -350)

qₓ = copₓ = 60
qᵧ = copᵧ = 200
qᵤ = copᵤ - zₚ = -230 - (-250) = 20
zₚ = -250 (projection plane z-coordinate)


Step 2: Build the projection matrix
[1   0   (-qₓ/qᵤ)     (zₚ·qₓ/qᵤ)  ]   [1   0   -3    -750 ]
[0   1   (-qᵧ/qᵤ)     (zₚ·qᵧ/qᵤ)  ] = [0   1   -10   -2500]
[0   0   (-zₚ/qᵤ)     (zₚ+zₚ²/qᵤ)] = [0   0   12.5  -3125]
[0   0   (-1/qᵤ)      (1+zₚ/qᵤ)   ]   [0   0   -0.05 -11.5]

Where:
-qₓ/qᵤ = -60/20 = -3
-qᵧ/qᵤ = -200/20 = -10
-zₚ/qᵤ = -(-250)/20 = 12.5
-1/qᵤ = -1/20 = -0.05
zₚ·qₓ/qᵤ = (-250)(60)/20 = -750
zₚ·qᵧ/qᵤ = (-250)(200)/20 = -2500
zₚ + zₚ²/qᵤ = -250 + (-250)²/20 = -250 + 3125 = 2875
1 + zₚ/qᵤ = 1 + (-250)/20 = 1 - 12.5 = -11.5


Step 3: Apply matrix to flower coordinates
Multiply the matrix by [420, 84, -350, 1]ᵀ

x'·w = 1(420) + 0(84) + (-3)(-350) + (-750)(1) = 420 + 1050 - 750 = 720
y'·w = 0(420) + 1(84) + (-10)(-350) + (-2500)(1) = 84 + 3500 - 2500 = 1084
z'·w = 0(420) + 0(84) + (12.5)(-350) + (2875)(1) = -4375 + 2875 = -1500
w = 0(420) + 0(84) + (-0.05)(-350) + (-11.5)(1) = 17.5 - 11.5 = 6

Step 4: Normalize by w
x' = x'·w / w = 720 / 6 = 120
y' = y'·w / w = 1084 / 6 = 180.67
z' = z'·w / w = -1500 / 6 = -250

Answer:
The flower's projected coordinates P' on the window are (120, 180.67, -250).
```