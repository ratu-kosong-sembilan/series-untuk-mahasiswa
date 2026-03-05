from manim import *
import numpy as np

OUTPUT_DIR = r"D:\Data Ratu\WEB PROJECT FOR BUSSINESS\Series Untuk Mahasiswa\02-MODUL-KONTEN\Output animasi"

config.media_dir = OUTPUT_DIR
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = "#F7F8FB"

RED_MAIN = "#E11D48"
BLUE_MAIN = "#2563EB"
GREEN_MAIN = "#10B981"
YELLOW_MAIN = "#F59E0B"
TEXT_MAIN = "#0F172A"
AXIS_COLOR = "#94A3B8"
GRID_COLOR = "#CBD5E1"
LINE_THIN = 2


def engineer_logo():
    head = Circle(radius=0.18, color=TEXT_MAIN, stroke_width=LINE_THIN).set_fill("#F8CBA6", 1)
    body = Rectangle(width=0.5, height=0.45, color=TEXT_MAIN, stroke_width=LINE_THIN).set_fill("#E2E8F0", 1)
    helmet = Arc(radius=0.22, start_angle=PI, angle=PI, color=YELLOW_MAIN, stroke_width=3)
    helmet_brim = Line(LEFT * 0.22, RIGHT * 0.22, color=YELLOW_MAIN, stroke_width=3).shift(DOWN * 0.08)
    head_group = VGroup(head, helmet, helmet_brim).arrange(DOWN, buff=0.0)
    head_group[0].shift(DOWN * 0.05)
    body.shift(DOWN * 0.45)
    icon = VGroup(head_group, body)
    label = Text("Guru Ratu", font_size=22, color=TEXT_MAIN)
    group = VGroup(icon, label).arrange(RIGHT, buff=0.2)
    group.scale(0.8)
    group.to_corner(UL).shift(RIGHT * 0.3 + DOWN * 0.2)
    return group


class RotatingPhasor(Scene):
    def construct(self):
        logo = engineer_logo()
        title = Text("Phasor Berputar -> Gelombang Sinus", color=TEXT_MAIN, font_size=40)
        title.to_edge(UP)
        self.play(FadeIn(title), FadeIn(logo), run_time=1)

        center_left = LEFT * 4
        radius = 1.6
        circle = Circle(radius=radius, color=AXIS_COLOR, stroke_width=LINE_THIN).move_to(center_left)

        theta = ValueTracker(0.0)

        vector = always_redraw(
            lambda: Arrow(
                center_left,
                center_left + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
                buff=0,
                color=RED_MAIN,
                stroke_width=3,
            )
        )
        tip = always_redraw(
            lambda: Dot(center_left + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]), color=RED_MAIN)
        )
        proj_line = always_redraw(
            lambda: Line(
                center_left + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
                center_left + radius * np.array([np.cos(theta.get_value()), 0, 0]),
                color=YELLOW_MAIN,
                stroke_width=LINE_THIN,
            )
        )

        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=3,
            axis_config={"color": AXIS_COLOR, "stroke_width": LINE_THIN},
        ).to_edge(RIGHT).shift(DOWN * 0.4)

        sine = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(x + theta.get_value()),
                x_range=[0, 2 * np.pi],
                color=BLUE_MAIN,
                stroke_width=3,
            )
        )
        wave_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    theta.get_value(),
                    np.sin(theta.get_value() + theta.get_value()),
                ),
                color=BLUE_MAIN,
            )
        )

        self.play(Create(circle), Create(axes), run_time=1)
        self.play(Create(vector), FadeIn(tip), Create(proj_line), run_time=1)
        self.play(Create(sine), FadeIn(wave_dot), run_time=1)

        self.play(theta.animate.set_value(2 * np.pi), run_time=14, rate_func=linear)
        self.wait(2)


class PolarToComplex(Scene):
    def construct(self):
        logo = engineer_logo()
        title = Text("Dari Polar ke Bilangan Kompleks", color=TEXT_MAIN, font_size=40)
        title.to_edge(UP)
        self.play(FadeIn(title), FadeIn(logo), run_time=1)

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": AXIS_COLOR, "stroke_width": LINE_THIN},
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1},
        ).shift(DOWN * 0.2)

        theta = 40 * DEGREES
        radius = 3.0
        origin = plane.c2p(0, 0)
        end = plane.c2p(radius * np.cos(theta), radius * np.sin(theta))

        vector = Arrow(origin, end, buff=0, color=GREEN_MAIN, stroke_width=3)
        x_proj = DashedLine(end, plane.c2p(radius * np.cos(theta), 0), color=YELLOW_MAIN, stroke_width=LINE_THIN)
        y_proj = DashedLine(end, plane.c2p(0, radius * np.sin(theta)), color=YELLOW_MAIN, stroke_width=LINE_THIN)

        eq1 = MathTex(r"Z = R\cos(\theta) + jR\sin(\theta)", color=TEXT_MAIN, font_size=36).to_edge(DOWN)
        eq2 = MathTex(r"Z = R e^{j\theta}", color=TEXT_MAIN, font_size=40).next_to(eq1, UP)

        self.play(Create(plane), run_time=1)
        self.play(Create(vector), run_time=1)
        self.play(Create(x_proj), Create(y_proj), run_time=1)
        self.play(FadeIn(eq1), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(eq2), run_time=1)
        self.wait(6)


class PhasorAddition(Scene):
    def construct(self):
        logo = engineer_logo()
        title = Text("Penjumlahan Phasor", color=TEXT_MAIN, font_size=40)
        title.to_edge(UP)
        self.play(FadeIn(title), FadeIn(logo), run_time=1)

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": AXIS_COLOR, "stroke_width": LINE_THIN},
            background_line_style={"stroke_color": GRID_COLOR, "stroke_width": 1},
        ).shift(DOWN * 0.2)
        self.play(Create(plane), run_time=1)

        origin = plane.c2p(0, 0)
        v1 = plane.c2p(2.6, 0.5)
        v2 = plane.c2p(1.6, 1.8)

        vec1 = Arrow(origin, v1, buff=0, color=RED_MAIN, stroke_width=3)
        vec2 = Arrow(origin, v2, buff=0, color=BLUE_MAIN, stroke_width=3)
        self.play(Create(vec1), Create(vec2), run_time=1)

        vec2_shifted = Arrow(v1, v1 + (v2 - origin), buff=0, color=BLUE_MAIN, stroke_width=3)
        result = Arrow(origin, v1 + (v2 - origin), buff=0, color=GREEN_MAIN, stroke_width=3)

        self.play(Transform(vec2, vec2_shifted), run_time=1.5)
        self.play(Create(result), run_time=1)

        eq = MathTex(r"\vec{V}_{total} = \vec{V}_1 + \vec{V}_2", color=TEXT_MAIN, font_size=36)
        eq.to_edge(DOWN)
        self.play(FadeIn(eq), run_time=1)
        self.wait(7.5)
