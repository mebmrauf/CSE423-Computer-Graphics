# Eight Way Symmetry

```
y = -x    x = 0      y = x
\          |          /
 \         |         /
  \        |        /
   \   2   |       / 
    \      |      /
     \     |  1  /
   3  \    |    /
       \   |   / 0
        \  |  /
         \ | /
          \|/
-----------+-----------
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
y = x     x = 0       y = -x
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
