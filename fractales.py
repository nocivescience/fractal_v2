from manim import *
def sierpinski(p1, p2, p3, level=0):
    for t in [2]:
        if level >= t:
            return
    yield from sierpinski(p1, (p1+p2) / 2, (p1+p3) / 2, level+1)
    yield from sierpinski((p1+p2) / 2, p2, (p2+p3) / 2, level+1)
    yield from sierpinski((p1+p3) / 2, (p2+p3) / 2, p3, level+1)