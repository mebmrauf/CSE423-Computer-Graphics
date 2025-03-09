# Some issues are there, I'm fixing them...

# DDA, Midpoint Algorithm

## Digital Differential Algorithm (DDA)
The line equation: `y = mx + c`

- If `-1 < m < 1`:

    <b><p>X<sub>k+1</sub> = X<sub>k</sub> ± 1</p></b>
    <b><p>Y<sub>k+1</sub> = Y<sub>k</sub> ± m</p></b>

- else:

  <b><p>Y<sub>k+1</sub> = Y<sub>k</sub> ± 1</p></b>
  <b><p>X<sub>k+1</sub> = X<sub>k</sub> ± 1/m</p></b>

- Then, round off to the nearest pixel.

```
- check `m` is within the range or not

- if yes, check `x` is increasing or decreasing
- if `x` increase, use positive(+) sign
- else, use negative(-) sign

- else, check `y` is increasing or decreasing
- if `y` increase, use positive(+) sign
- else, use negative(-) sign
```

#### Example 01

Points : (2,2) & (7,5)

`m = 0.6 ; -1 < m < 1 ; x is increasing`

| x | y | y(round)| pixel |
|----|----|---------|------|
| 2 | 2.0 | 2 | (2,2) |
| 3 | 2.6 | 3 | (3,3) |
| 4 | 3.2 | 3 | (4,3) |
| 5 | 3.8 | 4 | (5,4) |
| 6 | 4.4 | 4 | (6,4) |
| 7 | 5.0 | 5 | (7,5) |

#### Example 02

Points : (2,2) & (5,7)

`m = 1.7 ; m > 1 ; y is increasing`

| y | x | x(round)| pixel |
|----|----|---------|------|
| 2 | 2.00 | 2 | (2,2) |
| 3 | 2.58 | 3 | (3,3) |
| 4 | 3.16 | 3 | (3,4) |
| 5 | 3.74 | 4 | (4,5) |
| 6 | 4.32 | 4 | (4,6) |
| 7 | 4.90 | 5 | (5,7) |

#### Example 03

Points : (2,3) & (-1, -4)

`m = 2.3 ; m > 1 ; y is decreasing`

| y | x | x(round)| pixel |
|----|----|---------|------|
| 3 | 2.00 | 2 | (2,3) |
| 2 | 1.57 | 2 | (2,2) |
| 1 | 1.14 | 1 | (1,1) |
| 0 | 0.71 | 1 | (1,0) |
| -1 | 0.28 | 0 | (0,-1) |
| -2 | 0.15 | 0 | (0, -2) |
| -3 | -0.58 | -1 | (-1,-3) |
| -4 | -1.01 | -1 | (-1,-4) |

Calculation:
```
m > 1 ; y is decreasing

1/m = 0.43
prev y = 3
prev x = 2.00

current y = 3 - 1 = 2
current x = 2 - 0.43 = 2.57
```

#### Example 04

Points : (2,3) & (-1, 4)

`m = 2.3 ; -1 < m < 1 ; x is decreasing`

| x | y | y(round)| pixel |
|----|----|---------|------|
| 2 | 3.00 | 3 | (2,3) |
| 1 | 3.33 | 3 | (1,3) |
| 0 | 3.66 | 4 | (0,4) |
| -1 | 3.99 | 4 | (-1,4) |

Calculation:
```
-1 < m < 1 ; x is decreasing

m = -0.33
prev x = 2
prev y = 3

current x = 2 - 1 = 1
current y = 3 - (-0.33) = 3 + 0.33 = 3.33
```

#### Example 05

Points : (2,3) & (4, -4)

`m = -3.5 ; m < -1 ; y is decreasing`

| y | x | x(round)| pixel |
|----|----|---------|------|
| 3 | 2.00 | 2 | (2,3) |
| 2 | 2.29 | 2 | (2,2) |
| 1 | 2.58 | 3 | (3,1) |
| 0 | 2.87 | 3 | (3,0) |
| -1 | 3.16 | 3 | (3,-1) |
| -2 | 3.45 | 3 | (3, -2) |
| -3 | 3.74 | 4 | (4,-3) |
| -4 | 4.03 | 4 | (4,-4) |

### Drawbacks

Two big issues:
- Accumulation of round-off errors can make the pixelated line drift away from what was intended (Low Accuracy)
- The rounding operations and floating point arithmetic involved are time consuming (Time Consuming)


## Midpoint Algorithm

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
