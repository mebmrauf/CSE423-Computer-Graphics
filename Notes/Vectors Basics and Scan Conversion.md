# Vectors
- Points specify location in space (or in the plane). 
- Vectors have magnitude and direction (like velocity). The difference between two points is a vector. For example, (p,q) - p and q are two points; vector, v = q - p.
- Points ≠ Vectors

### Magnitude of a Vector
<p>|a|= √(x<sup>2</sup>+y<sup>2</sup>)</p>

### Unit Vector
```
â = a / |a|
```

### Vector Addition
```
(a + b) + c = a + (b + c)
```

### Vector Subtraction
```
b – a = b + (-a)
a - b ≠ b - a
```

## Dot Product / Scalar Multiplication 
```
a.b = |a||b|Cosθ

|b|^2 = b·b
a.1 = a
a.0 = 0
a.(-1) = -a

if  b and c are two vectors,
Cosθ = bc
if b.c = 0, b and c are perpendiicular
```
```
Properties:
Symmetry: a·b = b·a
Linearity: (a+c)·b = a·b + c·b
Homogeneity: (sa)·b = s(a·b)
```
## Cross Product / Vector Multiplication
```
bxc = |b||c|Sinθâ
```
```
Properties
Antisymmetry: axb = - bΧa
Linearity: (a+c) x b = axb + cxb
Homogeneity: (sa) x b = s(axb)
```
<b>Cross Product</b>
```
  a x b
|i  j   k|
|ax ay az|
|bx by bz|
```
```
Geometric Interpretation of Cross Product
- aXb is perpendicular to both a and b 
- |aXb| = area of the parallelogram defined by a and b
```

# Scan Conversion

<p>dy = y<sub>2</sub> - y<sub>1</sub>; dx = x<sub>2</sub> - x<sub>1</sub></p>

```
y = mx + c
y = dy/dx + c

Example:
Given points, (2,2) & (7,5)
Find the pixels

m = (5-2)/(7-2) = 3/5
c = 2 - (3/5)*3 = 4/5

y(3) = 3*3/5 + 4/5 = 13/5 ≈ 3 ; pixel (3,3)
y(4) = 4*3/5 + 4/5 = 16/5 ≈ 3 ; pixel (4,3)
y(5) = 5*3/5 + 4/5 = 19/5 ≈ 4 ; pixel (5,4)
y(6) = 6*3/5 + 4/5 = 22/5 ≈ 4 ; pixel (6,4)
```

## Drawbacks

Too slow because,
- The equation y = mx + b requires the multiplication of m by x
- Rounding off the resulting y coordinates
