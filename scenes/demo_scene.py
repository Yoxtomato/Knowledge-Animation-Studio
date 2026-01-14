from manim import *


class HelloManim(Scene):
    def construct(self):
        # 创建一个圆
        circle = Circle(color=BLUE, fill_opacity=0.5)

        # 创建一个正方形
        square = Square(color=RED, fill_opacity=0.5)
        square.next_to(circle, RIGHT)

        # 播放动画
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait(1)
