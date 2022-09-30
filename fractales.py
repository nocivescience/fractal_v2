from importlib.resources import path
from manim import *
class RecursionScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        line_1=Line()
        line_2=line_1.copy()
        line_2.rotate(PI/2)
        line_2.move_to(line_1.get_end(),line_2.get_start())
        line_1.add(line_2)
        # self.play(*[
        #     Create(line) for line in [
        #         line_1,
        #         line_2
        #     ]
        # ])
        self.play(Create(line_1))
        self.wait()