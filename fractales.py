import numpy as np
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve
p = 6 # 2^3 squares on a side
n = 2 # two dimensional cube, i.e. square
hc = HilbertCurve(p, n)

N = (2**p)**n
points = hc.points_from_distances(range(N))
for i in range(1, N):
    x0, y0 = points[i-1]
    x1, y1 = points[i]
    plt.plot([x0, x1], [y0, y1])
plt.gca().set_aspect('equal')    
plt.show()

