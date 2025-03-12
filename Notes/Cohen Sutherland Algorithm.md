# Cohen Sutherland Algorithm 
A point (x,y) is not clipped if:
<p>x<sub>min</sub>≤ x ≤ x<sub>max</sub> AND y<sub>min</sub>≤ y ≤ y<sub>max</sub></p>

## Line Clipping
<p>use 4 bit outcode --> a<sub>3</sub>a<sub>2</sub>a<sub>1</sub>a<sub>0</sub></p>
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

### Calculate Outcode(2D)
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

### Calculate Outcode(3D)
```
A = Above, B = Below, R = Right, L = Left, N = Near, F = Far
ABRLNF = ?

if y > y_max: A = 1
else: A = 0

if y < y_min: B = 1
else: B = 0

if x > x_max: R = 1
else: R = 0

if x < x_min: L = 1
else: L = 0

if z > z_max: N = 1
else: N = 0

if z < z_min: F = 1
else: F = 0
```

### Trivial Conditions

#### Acceptance
```
If outcode1 = outcode2 = 0000; lines are completely inside
```
#### Rejection
```
If outcode1 != 0 AND outcode2 != 0; lines are completely outside
```

### Boundary Intersection Formulas

#### ABOVE/TOP boundary intersection:
```
y = y_max
x = x_1 + 1/m (y_max - y_1)
```

#### BOTTOM/BELOW boundary intersection:
```
y = y_min
x = x_1 + 1/m (y_min - y_1)
```

#### RIGHT boundary intersection:
```
x = x_max
y = y_1 + m (x_max - x_1)
```
#### LEFT boundary intersection:
```
x = x_min
y = y_1 + m (x_min - x_1)
```

## Algorithm
```
cohen-Sutherland(x1, y1, x2, y2):
oc1 = calculate_outcode(x1, y1), 
oc2 = calculate_outcode(x2, y2);

while(true) {

if (oc1 == oc2 == 0000) {
	//line is completely inside, no need to clip
	output (x1, y1), (x2, y2)
	break
}

else if (oc1 != 0000 AND oc2 != 0000) {
	//line is completely outside and clipped
	break
}

else{

	if(oc1 != 0000){
		(x1, y1) = find intersection point of line
                           and the boundary corresponding
			   to non-zero bit of oc1
		oc1 = calculate_outcode(x1, y1)
	}

	else{
		(x2, y2) = find intersection point of line
			   and the boundary corresponding
			   to non-zero bit of oc2
		oc2 = calculate_outcode(x2, y2)
	}

	continue
}
```
