# Cohen Sutherland Algorithm 
A point (x,y) is not clipped if:
<p>x<sub>min</sub>≤ x ≤ x<sub>max</sub> AND y<sub>min</sub>≤ y ≤ y<sub>max</sub></p>

## Line Clipping
use 4 bit outcode
<p>a<sub>3</sub>a<sub>2</sub>a<sub>1</sub>a<sub>0</sub> = ABRL</p>
where,
<p>a<sub>3</sub> = Above</p>
<p>a<sub>2</sub> = Below</p>
<p>a<sub>1</sub> = Right</p>
<p>a<sub>0</sub> = Left</p>
