# CSE423: DDA, Midpoint Algorithm

## Digital Differential Algorithm (DDA)
The line equation: `y = mx + c`

`If -1 < m < 1:`

<p>X<sub>k+1</sub> = X<sub>k</sub> + 1
Y<sub>k+1</sub> = Y<sub>k</sub> + 1</p>

`else:`

<p>Y<sub>k+1</sub> = Y<sub>k</sub> + 1
X<sub>k+1</sub> = X<sub>k</sub> + 1/m</p>

Then, round off to the nearest pixel.

## Midpoint Algorithm

The decision function for the midpoint determines the next pixel position:

- If \( d(-ve) \), choose the lower pixel (E, upper side)
- If \( d(+ve) \), choose the upper pixel (NE, lower side)

### Derivation:
```
y = mx + c
```
Substituting slope definition:
```
y = (y₂ - y₁) / (x₂ - x₁) * x + c
```
Multiplying by 2dx:
```
2x dy - 2y dx + 2c dx = 0
```
Rewriting in standard form:
```
Ax + By + C = 0
```
Where:
```
A = 2dy, B = -2dx, C = 2c dx
```

### Initial Midpoint Calculation:
```
d = 2dy - dx
```
### Next Midpoint Calculation Based on Pixel Choice:
- NE → `d = d + 2dy - 2dx`
- E → `d = d + 2dy`

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
```
dy = y₂ - y₁ = 52 - 2 = 50
dx = x₂ - x₁ = 70 - 0 = 70
```
#### Pixel (0,2):
```
d = 2dy - dx = (2 * 50) - 70 = 30
```
Since \( d > 0 \), choose NE:
```
d = d + 2dy - 2dx = 30 + (2 * 50) - (2 * 70) = -10
Next Pixel: (1,3)
```
#### Pixel (1,3):
```
d = -10 (from previous step)
```
Since \( d < 0 \), choose E:
```
d = d + 2dy = -10 + (2 * 50) = 90
Next Pixel: (2,3)
```
#### Pixel (2,3):
```
d = 90 (from previous step)
```
Since \( d > 0 \), choose NE:
```
d = d + 2dy - 2dx = 90 + (2 * 50) - (2 * 70) = 50
Next Pixel: (3,4)
```
