# Cohen Sutherland Algorithm 
A point (x,y) is not clipped if:
<p>x<sub>min</sub>≤ x ≤ x<sub>max</sub> AND y<sub>min</sub>≤ y ≤ y<sub>max</sub></p>

## Line Clipping
<p>use 4 bit outcode - a<sub>3</sub>a<sub>2</sub>a<sub>1</sub>a<sub>0</sub></p>
where,
<p>a<sub>3</sub> = Above; a<sub>2</sub> = Below; a<sub>1</sub> = Right; a<sub>0</sub> = Left | ABRL</p>

```
ABRL = 0000 (Window)
           |           |
           |   Above   |
   1001    |   1000    |   1010
           |           |
-----------|-----------|-----------
           |           |
    Left   |  Window   |   Right
    0001   |   0000    |   0010
           |           |
-----------|-----------|-----------`
           |           |
   0101    |   0100    |   0110
           |   Below   |
           |           |
```

### Calculate Outcode
```
ABRL = ?

if y > y_max: A = 1
else: A = 0

if y < y_min: B = 1
else: B = 0

if x > x_max: R = 1
else: R = 0

if x < x_min: L = 1
else: L = 0
```

```
For example, given (x_min, y_min), (x_max, y_max) = (-250, -200), (250, 200)
Now, find the outcode (x, y) = (-100, -220)

y < y_max = -220 < 200 : A = 0
y < y_min = -220 < -200 : B = 1
x < x_max = -100 < 250 : R = 0
x > x_min = -100 > -250 : L = 0

So, the outcode, ABRL = 0100
```
