# Cyrus Beck Algorithm

```

             P_1(x_1, y_1)
                   ⦿
                  /
                 /
                /
               /
              /
             /
            ⦿ P(t)
           /
          /
         /
        /
       /
      /
     ⦿
P_0(x_0, y_0)

```

## Parametric Equation
<p>P(t) = P<sub>0</sub> + t(P<sub>1</sub> - P<sub>0</sub>)</p>
<p>P(t) = (x<sub>0</sub>, y<sub>0</sub>) + t(x<sub>1</sub> - x<sub>0</sub>, y<sub>1</sub> - y<sub>0</sub>)</p>
<p>P(t) = (x<sub>0</sub> + t(x<sub>1</sub> - x<sub>0</sub>), y<sub>0</sub> + t(y<sub>1</sub> - y<sub>0</sub>))</p>

If `0 ≤ t ≤ 1`, all the intersection points will be inside the line.

## Normal Vectors to Boundary
```
           |           |
           |   N-top   |
           |   =(0,1)  |
           |           |
-----------|-----------|-----------
           |           |
   N-left  |           |   N-right
   =(-1,0) |           |   =(1,0)
           |           |
-----------|-----------|-----------`
           |           |
           |  N-bottom |
           |  =(0,-1)  |
           |           |
```

## Angle
```
N_i = Left(-1,0) ; Right(1,0) ; Top(0,1) ; Bottom(0,-1)
```

### Potential Entering
```
N_i.D < 0 (+ve) => PE
=> Angle > 90°
```

### Potential Leaving
```
N_i.D > 0 (-ve) => PL
=> Angle < 90°
```

## Boundary(t)
<p>t<sub>left</sub> = -(x<sub>0</sub> - x<sub>min</sub>)/(x<sub>1</sub> - x<sub>0</sub>)</p>

## Cyrus-Beck algo
- Calculate t values of intersection points with each 4 boundaries
- Classify intersection points whether PE/PL
- Select the PE with highest t and the PL with the lowest t
- Using parametric line eqn. find the clipped points

## Advantages and Drawbacks

### Advantage
- Works with polygons too (not only with clip rectangles)
- Works in 3D scenario (polyhedrons)

### Drawbacks
- Does not work with concave polygon clip region
