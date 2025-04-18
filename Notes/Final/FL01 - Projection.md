# FL01 - Projection

---

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

### 🔍 **1. Perspective Projection**

**Definition**: A projection where lines of sight (projectors) converge at a single point called COP (the viewer’s eye or camera).

COP - Center of Projection

### ✅ Characteristics:

- **Mimics human vision** – things look smaller as they get farther away.
- **Has a vanishing point** – parallel lines appear to converge.
- **Depth is realistic** – good for rendering real-world scenes (e.g., video games, 3D animation).
- **Non-uniform scale** – objects farther away are scaled down more.

### ✏️ Example Use:

- Architectural visualization
- 3D simulations
- Photography and cinematography

---

### 🔧 **2. Parallel Projection**

**Definition**: A projection where the lines of sight (projectors) are parallel to each other and perpendicular (orthographic) or angled (oblique) to the projection plane.

### ✅ Characteristics:

- **No perspective distortion** – objects stay the same size regardless of depth.
- **No vanishing point** – parallel lines remain parallel.
- **More technical/diagrammatic** – ideal for engineering or CAD.
- **Uniform scale** – good for precise measurements.

### Types:

- **Orthographic Projection** – projectors are perpendicular to the projection plane (used in blueprints).
- **Oblique Projection** – projectors are at an angle to the projection plane (used in some technical illustrations).

### ✏️ Example Use:

- Engineering and architectural drawings
- CAD software
- Blueprints and schematics

---

### 🆚 **Quick Comparison Table**

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
