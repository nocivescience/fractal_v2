from manim import *
import itertools as it
class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":8,
        "angle":90*DEGREES,
        "border_proportion":1.25,
        "colors":[RED_A,RED_C,RED_E,BLUE_A,
                  BLUE_C,BLUE_E,YELLOW_A,YELLOW_C,
                  YELLOW_E,PURPLE_A,PURPLE_C,PURPLE_E]
    }
    def construct(self):
        self.color = it.cycle(self.CONFIG['colors'])
        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, color = next(self.color))
        path.add(first_line)

        self.camera.frame.animate.set(height=first_line.get_height() * self.CONFIG['border_proportion'])
        self.camera.frame.animate.move_to(first_line)
        self.play(Create(first_line))
        self.add_foreground_mobject(path)

        self.target_path = self.get_all_paths(path,self.CONFIG['iterations'])
        for i in range(self.CONFIG['iterations']):
            self.duplicate_path(path,i)
        self.wait()

    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * self.CONFIG['border_proportion']
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Transform(path,new_path),
            self.camera.frame.animate.move_to(set_paths),
            self.camera.frame.animate.set(height=height),
            run_time=1, rate_func=smooth
            )
        self.add_foreground_mobject(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        self.CONFIG['angle'], 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1