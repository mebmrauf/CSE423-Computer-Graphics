# Curves

## Curve Representation

```jsx
Explicit: y = f(x)
y = mx + b			y = x^2
(–) Must be a single valued function
(–) Vertical lines, say x = d? No way to represent using single valued function

Implicit: f(x,y) = 0
(+) y can be multiple valued function of x
x^2 + y^2 - r^2 = 0
y > 0 : out of the curve
y = 0 : on the curve
y < 0 : inside the curve
(–) Continuity hard to detect

Parametric: (x, y) = (x(t), y(t))
(x, y) = (cost, sint)
(+) Easy to specify, modify and control
(–) Extra hidden variable t, the parameter, non intuitive

Subdivision Representation:
- Used to create smooth curves by repeatedly splitting and adjusting points on a shape.
- Split each lines into smaller parts
- Add new points betweeen the existing ones
- Move the points to smooth out the shape
```

![Screenshot 2025-05-17 at 12.11.11 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.11_AM.png)

## Lagrange

![Screenshot 2025-05-17 at 12.11.21 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.21_AM.png)

![Screenshot 2025-05-17 at 12.15.35 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.15.35_AM.png)

![Screenshot 2025-05-17 at 12.11.34 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.34_AM.png)

![Screenshot 2025-05-17 at 12.11.40 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.40_AM.png)

![Screenshot 2025-05-17 at 12.11.47 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.47_AM.png)

![Screenshot 2025-05-17 at 12.11.54 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.11.54_AM.png)

### Lagrange Polynomial Problems

- y=f(x), no multiple values
- Higher order functions tend to oscillate
- No local control (change any (xi, yi) changes the whole curve)
- Computationally expensive due to high degree.

## Piecewise Linear Polynomial

To overcome the problems with Lagrange polynomial

- Divide given points into overlap sequences of 4 points
- Construct **3rd degree polynomial** that passes through these points, p0, p1 , p2 , p3 then p3, p4 , p5 , p6 etc.
- Then glue the curves so that they appear **sufficiently smooth** at joint points.

### Why Cubic Curves?

- Lower-degree polynomials offer too little flexibility in controlling the shape of the curve.
- Higher-degree polynomials can introduce unwanted wiggles and also require more computation.
- No lower-degree representation allows a curve segment to be defined by two given endpoints with given derivative at each endpoints.
- No lower-degree curves are non planar in 3D.

## Parametric Continuity, C(n)

We say a curve is C(n) continuous, if all its derivatives up to and including n are continuous

```jsx
C(0) - position
C(1) - position and velocity/tangent(1st derivative)
C(2) - position, velocity/tangent and accelaration(2nd derivative)

If true:
C(0) - no gaps
C(1) - no corners
C(2) - looks smooth
```

- **Positional discontinuity** means the curve is broken - there’s a gap or jump between two segments, so they don’t connect at the same point.
- **Tangential discontinuity** in curves means the segments meet at a point, but their directions (tangents) are different.

![Screenshot 2025-05-17 at 12.43.07 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.43.07_AM.png)

![Screenshot 2025-05-17 at 12.43.29 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.43.29_AM.png)

## BÉZIER CURVE

![Screenshot 2025-05-17 at 12.48.15 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.48.15_AM.png)

![Screenshot 2025-05-17 at 12.48.42 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.48.42_AM.png)

![Screenshot 2025-05-17 at 12.48.54 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.48.54_AM.png)

![Screenshot 2025-05-17 at 12.49.03 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.49.03_AM.png)

![Screenshot 2025-05-17 at 12.49.27 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.49.27_AM.png)

![Screenshot 2025-05-17 at 12.50.03 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.50.03_AM.png)

![Screenshot 2025-05-17 at 12.50.27 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.50.27_AM.png)

![Screenshot 2025-05-17 at 12.50.35 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.50.35_AM.png)

![Screenshot 2025-05-17 at 12.50.45 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.50.45_AM.png)

## Practice Problems

![Screenshot 2025-05-17 at 12.54.52 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.54.52_AM.png)

- **C(1) continuity** requires that both the function and its first derivative are continuous at the given point.
- **G(1) continuity** requires that the function is continuous and the left and right derivatives at the point have the same direction (but not necessarily the same magnitude)
    
    ```jsx
    a. At t = 2π
    The function is defined as:
    
    For t ≤ 2π: (x(t), y(t)) = (t, sin t)
    For t > 2π: (x(t), y(t)) = (t, 1 - cos t)
    
    First, let's check continuity (C(0)):
    
    Left limit: (x(2π), y(2π)) = (2π, sin(2π)) = (2π, 0)
    Right limit: (x(2π), y(2π)) = (2π, 1 - cos(2π)) = (2π, 1 - 1) = (2π, 0)
    
    The function values match, so the function is continuous at t = 2π.
    Now, let's check the first derivatives (for C(1)):
    
    Left derivative: (x'(t), y'(t)) = (1, cos t), so at t = 2π: (1, cos(2π)) = (1, 1)
    Right derivative: (x'(t), y'(t)) = (1, sin t), so at t = 2π: (1, sin(2π)) = (1, 0)
    
    The derivatives don't match, so the function is not C(1) continuous at t = 2π.
    For G(1) continuity, we need to check if the left and right derivatives point in the same direction:
    
    Left derivative at t = 2π: (1, 1)
    Right derivative at t = 2π: (1, 0)
    
    These vectors don't point in the same direction, so the function is not G(1) continuous at t = 2π.
    ```
    
    ```jsx
    b. At t = π/4
    The function is defined as:
    
    For t ≤ π/4: (x(t), y(t)) = (t, sin t)
    For t > π/4: (x(t), y(t)) = (t, 1 - cos t)
    
    Let's check continuity:
    
    Left limit: (x(π/4), y(π/4)) = (π/4, sin(π/4)) = (π/4, 1/√2) ≈ (π/4, 0.7071)
    Right limit: (x(π/4), y(π/4)) = (π/4, 1 - cos(π/4)) = (π/4, 1 - 1/√2) ≈ (π/4, 0.2929)
    
    The function values don't match, so the function is not continuous at t = π/4, which means it's neither C(1) nor G(1) continuous.
    ```
    
    ```jsx
    c. At t = 1
    The function is defined as:
    
    For t < 1: (x(t), y(t)) = (6t, t³)
    For t ≥ 1: (x(t), y(t)) = (t⁴ + 5, t²)
    
    Let's check continuity:
    
    Left limit: (x(1), y(1)) = (6·1, 1³) = (6, 1)
    Right limit: (x(1), y(1)) = (1⁴ + 5, 1²) = (6, 1)
    
    The function values match, so the function is continuous at t = 1.
    Now, let's check the first derivatives:
    
    Left derivative: (x'(t), y'(t)) = (6, 3t²), so at t = 1: (6, 3)
    Right derivative: (x'(t), y'(t)) = (4t³, 2t), so at t = 1: (4, 2)
    
    The derivatives don't match, so the function is not C(1) continuous at t = 1.
    For G(1) continuity, we need to check if the left and right derivatives point in the same direction:
    
    Left derivative at t = 1: (6, 3)
    Right derivative at t = 1: (4, 2)
    
    These vectors are proportional (right = 2/3 · left), so they point in the same direction. Therefore, the function is G(1) continuous at t = 1.
    ```
    
    ```jsx
    d. At t = 1
    The function is defined as:
    
    For t ≤ 1: (x(t), y(t)) = (t, t²)
    For t > 1: (x(t), y(t)) = (t, t² + (t-1)³)
    
    Let's check continuity:
    
    Left limit: (x(1), y(1)) = (1, 1²) = (1, 1)
    Right limit: (x(1), y(1)) = (1, 1² + (1-1)³) = (1, 1 + 0) = (1, 1)
    
    The function values match, so the function is continuous at t = 1.
    Now, let's check the first derivatives:
    
    Left derivative: (x'(t), y'(t)) = (1, 2t), so at t = 1: (1, 2)
    Right derivative: (x'(t), y'(t)) = (1, 2t + 3(t-1)²), so at t = 1: (1, 2 + 0) = (1, 2)
    
    The derivatives match, so the function is C(1) continuous at t = 1.
    Since the function is C(1) continuous, it is also G(1) continuous at t = 1.
    ```
    
- Find the explicit representation of a quadratic curve going through the following 3 points using the Lagrange Polynomial:
P0 = (0, 0), P1 = (1, 2), P2 = (2, 0)
    
    ```jsx
    For the points P₀ = (0, 0), P₁ = (1, 2), P₂ = (2, 0), we'll use the Lagrange interpolation formula:
    L(x) = y₀L₀(x) + y₁L₁(x) + y₂L₂(x), where:
    L₀(x) = [(x-x₁)(x-x₂)]/[(x₀-x₁)(x₀-x₂)]
    L₁(x) = [(x-x₀)(x-x₂)]/[(x₁-x₀)(x₁-x₂)]
    L₂(x) = [(x-x₀)(x-x₁)]/[(x₂-x₀)(x₂-x₁)]
    Substituting our points:
    
    L₀(x) = [(x-1)(x-2)]/[(0-1)(0-2)] = [(x-1)(x-2)]/[(-1)(-2)] = [(x-1)(x-2)]/[2]
    L₁(x) = [(x-0)(x-2)]/[(1-0)(1-2)] = [x(x-2)]/[1(-1)] = [x(x-2)]/[-1]
    L₂(x) = [(x-0)(x-1)]/[(2-0)(2-1)] = [x(x-1)]/[2(1)] = [x(x-1)]/[2]
    
    Now, L(x) = 0·L₀(x) + 2·L₁(x) + 0·L₂(x)
    L(x) = 2·L₁(x) = 2·[x(x-2)]/[-1] = -2x(x-2) = -2x² + 4x
    Therefore, the quadratic curve is y = -2x² + 4x or y = 4x - 2x²
    ```
    
- Derive the Basis Matrix for the cubic Bézier curve.
    
    ![Screenshot 2025-05-17 at 12.49.03 AM.png](FL04%20-%20Curves/Screenshot_2025-05-17_at_12.49.03_AM%201.png)
    
- Given four control points P0 = (1,1), P1 = (2,3), P2 = (4,3), and P3 = (5,1), find the point on the cubic Bézier curve at t = 0.5.
    
    ```jsx
    Given P₀ = (1,1), P₁ = (2,3), P₂ = (4,3), P₃ = (5,1), and t = 0.5.
    Using the formula:
    P(t) = (1-t)³P₀ + 3(1-t)²tP₁ + 3(1-t)t²P₂ + t³P₃
    Let's calculate:
    
    (1-0.5)³ = 0.5³ = 0.125
    3(1-0.5)²(0.5) = 3(0.5²)(0.5) = 3(0.25)(0.5) = 0.375
    3(1-0.5)(0.5)² = 3(0.5)(0.5²) = 3(0.5)(0.25) = 0.375
    (0.5)³ = 0.125
    
    Now:
    P(0.5) = 0.125·(1,1) + 0.375·(2,3) + 0.375·(4,3) + 0.125·(5,1)
    = (0.125, 0.125) + (0.75, 1.125) + (1.5, 1.125) + (0.625, 0.125)
    = (3, 2.5)
    Therefore, the point on the cubic Bézier curve at t = 0.5 is (3, 2.5).
    ```
    
- Given the four control points in 3D:
P0 = (0,0,0), P1 = (3,6,0), P2 = (6,6,6), P3 = (9,0,6)
Find the point on the cubic Bézier curve at t = 0.5.
    
    ```jsx
    Given P₀ = (0,0,0), P₁ = (3,6,0), P₂ = (6,6,6), P₃ = (9,0,6), and t = 0.5.
    Using the same approach as in problem 3:
    P(0.5) = 0.125·(0,0,0) + 0.375·(3,6,0) + 0.375·(6,6,6) + 0.125·(9,0,6)
    = (0,0,0) + (1.125,2.25,0) + (2.25,2.25,2.25) + (1.125,0,0.75)
    = (4.5, 4.5, 3)
    Therefore, the point on the cubic Bézier curve at t = 0.5 is (4.5, 4.5, 3).
    ```
    
- Given the four control points in 2D:
P0 = (0,0), P1 = (2,2), P2 = (4,-2), P3 = (6,0)
Find the point on the cubic Bézier curve at t = 0.75.
    
    ```jsx
    Given P₀ = (0,0), P₁ = (2,2), P₂ = (4,-2), P₃ = (6,0), and t = 0.75.
    Let's calculate:
    
    (1-0.75)³ = 0.25³ = 0.015625
    3(1-0.75)²(0.75) = 3(0.25²)(0.75) = 3(0.0625)(0.75) = 0.140625
    3(1-0.75)(0.75)² = 3(0.25)(0.75²) = 3(0.25)(0.5625) = 0.421875
    (0.75)³ = 0.421875
    
    Now:
    P(0.75) = 0.015625·(0,0) + 0.140625·(2,2) + 0.421875·(4,-2) + 0.421875·(6,0)
    = (0,0) + (0.28125,0.28125) + (1.6875,-0.84375) + (2.53125,0)
    = (4.5, -0.5625)
    Therefore, the point on the cubic Bézier curve at t = 0.75 is (4.5, -0.5625).
    ```
    
- Given the first three control points of a cubic Bézier curve:
P0 = (2, 1), P1 = (3, 4), P2 = (5, 6)
and the point on the curve at t = 0.5:
f(0.5) = (4, 5)
Find the fourth control point, P3 = (x3, y3).
    
    ```jsx
    Given P₀ = (2,1), P₁ = (3,4), P₂ = (5,6), f(0.5) = (4,5), and we need to find P₃ = (x₃,y₃).
    Using the formula for a point on a cubic Bézier curve at t = 0.5:
    f(0.5) = (1-0.5)³P₀ + 3(1-0.5)²(0.5)P₁ + 3(1-0.5)(0.5)²P₂ + (0.5)³P₃
    f(0.5) = 0.125P₀ + 0.375P₁ + 0.375P₂ + 0.125P₃
    Substituting the known values:
    (4,5) = 0.125(2,1) + 0.375(3,4) + 0.375(5,6) + 0.125(x₃,y₃)
    (4,5) = (0.25,0.125) + (1.125,1.5) + (1.875,2.25) + 0.125(x₃,y₃)
    (4,5) = (3.25,3.875) + 0.125(x₃,y₃)
    Solving for P₃:
    0.125(x₃,y₃) = (4,5) - (3.25,3.875)
    0.125(x₃,y₃) = (0.75,1.125)
    (x₃,y₃) = (6,9)
    Therefore, the fourth control point is P₃ = (6,9).
    ```
    
- You are going to draw 3 cubic Bézier curves joined together to form a single smooth composite curve. You have already decided upon the control points for the first and last Bézier curves:
First Bézier curve (Curve A):
A0 = (0, 0), A1 = (1, 2), A2 = (2, 2), A3 = (3, 0)
Third Bézier curve (Curve C):
C0 = (6, 0), C1 = (7, −2), C2 = (8, −2), C3 = (9, 0)
You want to insert a Bézier curve (Curve B) between them such that the entire 3-curve segment is C(1) continuous.
Find the 4 control points- B0, B1, B2, B3 of the middle Bézier curve (Curve B).
    
    ```jsx
    Given Information
    - Curve A: A₀ = (0, 0), A₁ = (1, 2), A₂ = (2, 2), A₃ = (3, 0)
    - Curve C: C₀ = (6, 0), C₁ = (7, -2), C₂ = (8, -2), C₃ = (9, 0)
    - Need to find control points for curve B: B₀, B₁, B₂, B₃
    
    For C(1) continuity, we need:
    1. **Value continuity** (C(0)): The endpoint of one curve must equal the starting point of the next
    2. **Derivative continuity**: The tangent direction and magnitude at the join points must be equal
    
    Step 1: Establish B₀ and B₃
    
    For value continuity:
    - B₀ must equal A₃: B₀ = (3, 0)
    - B₃ must equal C₀: B₃ = (6, 0)
    
    Step 2: Determine B₁ based on A₂ and A₃
    
    For derivative continuity at the A-B junction:
    - The derivative at t=1 for curve A is: 3(A₃ - A₂)
    - The derivative at t=0 for curve B is: 3(B₁ - B₀)
    
    These must be equal, so:
    3(A₃ - A₂) = 3(B₁ - B₀)
    A₃ - A₂ = B₁ - B₀
    B₁ = B₀ + (A₃ - A₂)
    B₁ = (3, 0) + ((3, 0) - (2, 2))
    B₁ = (3, 0) + (1, -2)
    B₁ = (4, -2)
    
    Step 3: Determine B₂ based on C₀ and C₁
    
    For derivative continuity at the B-C junction:
    - The derivative at t=1 for curve B is: 3(B₃ - B₂)
    - The derivative at t=0 for curve C is: 3(C₁ - C₀)
    
    These must be equal, so:
    3(B₃ - B₂) = 3(C₁ - C₀)
    B₃ - B₂ = C₁ - C₀
    B₂ = B₃ - (C₁ - C₀)
    B₂ = (6, 0) - ((7, -2) - (6, 0))
    B₂ = (6, 0) - (1, -2)
    B₂ = (5, 2)
    
    Final Control Points for Curve B
    
    B₀ = (3, 0)
    B₁ = (4, -2)
    B₂ = (5, 2)
    B₃ = (6, 0)
    ```