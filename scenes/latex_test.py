from manim import *


class LatexTest(Scene):
    def construct(self):
        title = Text("Final Test", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
