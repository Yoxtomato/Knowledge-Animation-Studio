from manim import *


class Celebration(Scene):
    def construct(self):
        # 1. 准备文字
        text_1 = Text("Environment", font_size=48, color=BLUE)
        text_2 = Text("Configured!", font_size=60, color=YELLOW)
        text_2.next_to(text_1, DOWN)

        # 2. 准备几何装饰
        circle = Circle(radius=3, color=WHITE)
        squares = VGroup(*[
            Square(side_length=0.5).move_to(circle.point_at_angle(angle))
            for angle in np.linspace(0, TAU, 12, endpoint=False)
        ])
        squares.set_color_by_gradient(BLUE, YELLOW, RED)

        # --- 动画开始 ---

        # 3. 进场
        self.play(DrawBorderThenFill(circle), run_time=1)
        self.play(SpinInFromNothing(squares), run_time=1)
        self.wait(0.5)

        # 4. 文字变换
        self.play(Write(text_1))
        self.play(
            text_1.animate.shift(UP * 0.5),
            FadeIn(text_2, shift=UP)
        )

        # 5. 庆祝动作：方块旋转 + 颜色循环
        self.play(
            Rotate(squares, angle=PI),
            Flash(text_2, color=YELLOW, line_length=0.5),
            run_time=2
        )

        # 6. 谢幕
        self.wait(1)
        self.play(
            ShrinkToCenter(squares),
            FadeOut(circle),
            FadeOut(text_1),
            FadeOut(text_2)
        )
