# Eight Way Symmetry

```
   y = -x      x = 0       y = x
      \          |          /
       \         |         /
        \        |        /
         \   2   |       / 
          \      |      /
           \     |  1  /
         3  \    |    /
             \   |   /   0
              \  |  /
               \ | /
                \|/
y = 0 -----------+----------- y = 0
                /|\
           4   / | \
              /  |  \
             /   |   \ 
            /    |    \   7
           /     |     \
          /   5  |   6  \
         /       |       \
        /        |        \
       /         |         \
      /          |          \
   y = x       x = 0      y = -x
```

### Steps
```
- Find the zone
```
```
- If zone is 0, apply Midpoint Line Algorithm
```
```
- Else, convert it to zone 0
- Apply Midpoint Line Algorithm
- Find the pixels in zone 0
- Convert pixels back to original zone
- Draw the line
```

### Quadrants

- <p>dx = x<sub>2</sub>-x<sub>1</sub></p>
- <p>dy = y<sub>2</sub>-y<sub>1</sub></p>

```
Q1 --> dy > 0, dx > 0
Q2 --> dy > 0, dx < 0
Q3 --> dy < 0, dx < 0
Q4 --> dy < 0, dx > 0
```

### Zone
```
|dx| > |dy| --> near to X axis
|dy| > |dx| --> near to Y axis
```

#### Example
```
Q. dx = 3, dy = 4

dx > 0, dy > 0
Selected quadrant Q1

|dy| > |dx| --> near to y axis
Selected zone 1

```

### Reflection

```
- (x,y) --> (x = 0) -->(-x,y)
- (x,y) --> (y = 0) -->(x,-y)
- (x,y) --> (y = x) -->(y,x)
- (x,y) -->(y = -x)-->(-y,-x)
```

### Convert to Zone 0
```
Zone 1 --> 0
x = y, y = x
```

```
Zone 2 --> 0
- (2 --> 1) --> x = -x, y = y
- (1 --> 0) --> x = y, y = -x
```

```
Zone 3 --> 0
x = -x, y = y
```

```
Zone 4 --> 0
x = -x, y = -y
```

```
Zone 5 --> 0
x = -y, y = -x
```

```
Zone 6 --> 0
x = -y, y = x
```

```
Zone 7 --> 0
x = x, y = -y
```

### Convert pixels back to original zone
```
Zone 0 --> 1
x = y, y = x
```

```
Zone 0 --> 2
x = -y, y = x
```

```
Zone 0 --> 3
x = -x, y = y
```

```
Zone 0 --> 4
x = -x, y = -y
```

```
Zone 0 --> 5
x = -y, y = -x
```

```
Zone 0 --> 6
x = y, y = -x
```

```
Zone 0 --> 7
x = x, y = -y
```
