# Midpoint Line Drawing Algorithm (MPL)

The decision function for the midpoint determines the next pixel position:

- If `d(-ve)`, choose the lower pixel `(E)`
- If `d(+ve)`, choose the upper pixel `(NE)`

### Derivation:

<p>dy = y<sub>2</sub> - y<sub>1</sub>; dx = x<sub>2</sub> - x<sub>1</sub></p>

```
y = mx + c
y = (dy / dx) * x + c
y = (2dy / 2dx) * x + c
2xdy - 2ydx + 2cdx = 0
Ax + By + C = 0

Here,
A = 2dy, B = -2dx, C = 2cdx
```

### Initial Midpoint Calculation:
- Midpoint → `d = 2dy - dx`

### Next Midpoint Calculation Based on Pixel Choice:

```
ΔNE → 2dy - 2dx ; ΔE → 2dy

NE → d = d + 2dy - 2dx = d + ΔNE
E → d = d + 2dy = d + ΔE
```

### Next Pixel/Point Based on Selected Pixel:
- NE → `x + 1, y + 1`
- E → `x + 1, y`

### Example: 
Given points (0,2) and (70,52), first three steps:

| Pixel | x | y | d   | NE/E | Updated d | Next Pixel |
|--------|----|----|-----|------|------------|-------------|
| (0,2)  | 0  | 2  | 30  | NE   | -10       | (1,3)       |
| (1,3)  | 1  | 3  | -10 | E    | 90        | (2,3)       |
| (2,3)  | 2  | 3  | 90  | NE   | 50        | (3,4)       |

### Calculations:

<p>dy = y<sub>2</sub> - y<sub>1</sub>; dx = x<sub>2</sub> - x<sub>1</sub></p>
<p>(x<sub>1</sub>, y<sub>1</sub>), (x<sub>2</sub>, y<sub>2</sub>) = (0,2), (70,52)</p>

```
dy = 52 - 2 = 50
dx = 70 - 0 = 70
ΔNE = (2 * 50) - (2 * 70) = -40
ΔE = 2 * 50 = 100
```

#### Pixel (0,2):
```
d = 2dy - dx = (2 * 50) - 70 = 30

Since d > 0(+ve), choose NE:
d = d + 2dy - 2dx = 30 + (2 * 50) - (2 * 70) = -10

Next Pixel: (1,3)
```
#### Pixel (1,3):
```
d = -10 (from previous step)

Since d < 0(-ve), choose E:
d = d + ΔE = -10 + 100 = 90

Next Pixel: (2,3)
```
#### Pixel (2,3):
```
d = 90 (from previous step)

Since d > 0(+ve), choose NE:
d = d + ΔNE = 90 - 40 = 50

Next Pixel: (3,4)
```

### Drawbacks

Range of m, `0 < m < 1`

That means `dx` and `dy` both are positive; `dx, dy > 0`

```
Example:
If the points are (2,9) and (8,4), midpoint could not be able to handle it.
m = (4-9)/(8-2) = -5/6 < 0
```
