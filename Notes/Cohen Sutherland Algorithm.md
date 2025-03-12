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
If (outcode1 AND outcode2) != 0000; lines are completely outside
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
cohenSutherland(x1, y1, x2, y2):
oc1 = calculate_outcode(x1, y1), 
oc2 = calculate_outcode(x2, y2);

while(true) {

if (oc1 == oc2 == 0000) {
	//line is completely inside, no need to clip
	output (x1, y1), (x2, y2)
	break
}

else if ((oc1 AND oc2) != 0000) {
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

## Examples
````
Determine whether the following line are accepted/rejected/partial using Cohen Sutherland line clipping algorithm. 
a) Given (-250,-200) to (250,200) be the clip region.
(i) (-100, -220) to (300, -210).
(ii) (-250, 200) to (250, -200).
b) Given (0,0) to (300,200) be the clip region.
(i) (50, -125) to (-100, 225).
(ii) (-250, 200) to (250, -200).

If they are partially accepted/rejected find the line segment within the clipping window. 
````

### a(i)
```
x_min = -250 ; y_min = -200
x_max = 250 ; y_max = 200

(x_1, y_1) = (-100, -220) to (x_2, y_2) = (300, -210)

outcode1/oc1 calculation:
x_1 > x_min ; so, L = 0
x_1 < x_max ; so, R = 0
y_1 < y_min ; so, B = 1
y_1 < y_max ; so, A = 0

oc1 = 0100

outcode2/oc2 calculation:
x_2 > x_min ; so, L = 0
x_2 > x_max ; so, R = 1
y_2 < y_min ; so, B = 1
y_2 < y_max ; so, A = 0

oc2 = 0110

oc1 AND oc2
0100
0100
----
0100

(0c1 AND oc2) != 0000
Since the line is completely out of the window, line clipped.
```

### a(ii)
```
x_min = -250 ; y_min = -200
x_max = 250 ; y_max = 200

(x_1, y_1) = (-250, 200) to (x_2, y_2) = (250, -200)

outcode1/oc1 calculation:
x_1 = x_min ; so, L = 0
x_1 < x_max ; so, R = 0
y_1 > y_min ; so, B = 0
y_1 = y_max ; so, A = 0

oc1 = 0000

outcode2/oc2 calculation:
x_2 > x_min ; so, L = 0
x_2 = x_max ; so, R = 0
y_2 = y_min ; so, B = 0
y_2 < y_max ; so, A = 0

oc2 = 0000

oc1 = oc2 = 0000

The line is completely inside the window.
```

## Pros and Cons

### Pros
Works well for two cases
- Very large clip region
- Very small clip region
Because of many trivial accept and many trivial reject

### Cons
- Only rectangular clipping region
- Unnecessary clipping is done
- Different clipping order  may take less iterations  to finish 
