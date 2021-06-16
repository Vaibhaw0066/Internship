###One line segment from (x1,y1) to (x2,y2)
###Another line segment from (x3,y3) to (x4,y4)
___
The set of points on the first line segment is
```math
A = { (x1+(x2−x1)u,y1+(y2−y1)u)   ∈ R^2 ∣u ∈ [0,1]}
```
the set of points on the second line segment is
```math
B = { (x3+(x4−x3)t, y3+(y4−y3)t)  ∈ R^2 ∣t ∈ [0,1]}
```
we want to find,  <h5 >*A∩B*</h5> <br> 
which means finding u∈[0,1], t∈[0,1] such that  <br>
```math
( x1+(x2−x1)u, y1+(y2−y1)u) = (x3+(x4−x3)t, y3+(y4−y3)t )
```
split into components

```
x1 + (x2−x1)u = x3 + (x4−x3)t
```
```
y1 + (y2−y1)u = y3 + (y4−y3)t
```

####solve for u by eliminating t
```
(x1−x3) + (x2−x1) u (x4−x3) = (y1−y3) + (y2−y1)u(y4−y3)
```
```
(y4−y3)(x1−x3)−(x4−x3)(y1−y3)(x4−x3)(y2−y1)−(y4−y3)(x2−x1) = u

```

Finally,
####x = -1 * ((x1 - x2) * (u1 * v2 - u2 * v1) - (u2 - u1) * (x2 * y1 - x1 * y2)) / ((v1 - v2) * (x1 - x2) - (u2 - u1) * (y2 - y1))
####y = y = -1 * (u1 * v2 * y1 - u1 * v2 * y2 - u2 * v1 * y1 + u2 * v1 * y2 - v1 * x1 * y2 + v1 * x2 * y1 + v2 * x1 * y2 - v2 * x2 * y1) / (-1 * u1 * y1 + u1 * y2 + u2 * y1 - u2 * y2 + v1 * x1 - v1 * x2 - v2 * x1 + v2 * x2)