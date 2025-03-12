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

### Potential Entering
N_i.D < 0 => PE
=> Angle > 90°

### Potential Leaving
N_i.D > 0 => PL
=> Angle < 90°

## Cyrus-Beck algo
- Calculate t values of intersection points with each 4 boundaries
- Classify intersection points whether PE/PL
- Select the PE with highest t and the PL with the lowest t
- Using parametric line eqn. find the clipped points
