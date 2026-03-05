from __future__ import annotations

from pathlib import Path
import numpy as np
from manim import *

# Output directory inside repo
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
config.media_dir = str(OUTPUT_DIR)
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = "#FFFFFF"

# Color spec
REAL_BLUE = "#1E88E5"
IMAG_ORANGE = "#F57C00"
MAG_GREEN = "#43A047"
ANGLE_PURPLE = "#8E24AA"
TEXT_MAIN = "#111827"
GRID = "#CBD5E1"
AXIS = "#94A3B8"

LINE_THIN = 2
LINE_MED = 3


class VIS01_PhasorRotation(Scene):
    def construct(self):
        title = Text("Phasor Berputar", font_size=44, color=TEXT_MAIN)
        title.to_edge(UP)
        self.play(FadeIn(title), run_time=1)

        # Left: complex plane
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": AXIS, "stroke_width": LINE_THIN},
            background_line_style={"stroke_color": GRID, "stroke_width": 1},
        ).shift(LEFT * 3)

        # Right: sine axis
        axes = Axes(
            x_range=[0, 2 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": AXIS, "stroke_width": LINE_THIN},
        ).shift(RIGHT * 3 + DOWN * 0.2)

        self.play(Create(plane), Create(axes), run_time=1)

        center = plane.c2p(0, 0)
        radius = 1.5
        theta = ValueTracker(0.0)

        vector = always_redraw(
            lambda: Arrow(
                center,
                center + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
                buff=0,
                color=REAL_BLUE,
                stroke_width=LINE_MED,
            )
        )
        tip = always_redraw(
            lambda: Dot(center + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]), color=REAL_BLUE)
        )
        proj_line = always_redraw(
            lambda: Line(
                center + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0]),
                center + radius * np.array([np.cos(theta.get_value()), 0, 0]),
                color=IMAG_ORANGE,
                stroke_width=LINE_THIN,
            )
        )

        sine = always_redraw(
            lambda: axes.plot(lambda x: np.sin(x + theta.get_value()), x_range=[0, 2 * np.pi], color=MAG_GREEN, stroke_width=LINE_MED)
        )

        self.play(Create(vector), FadeIn(tip), Create(proj_line), run_time=1)
        self.play(Create(sine), run_time=1)

        label_v1 = always_redraw(
            lambda: Text("V1", font_size=26, color=REAL_BLUE).next_to(tip, UR, buff=0.1)
        )
        self.play(FadeIn(label_v1), run_time=0.5)

        # Animatic timing placeholder (extend to match 270s)
        self.play(theta.animate.set_value(2 * np.pi), run_time=12, rate_func=linear)
        self.wait(1)

        # Second phasor and resultant placeholder
        theta2 = ValueTracker(np.pi / 3)
        vector2 = always_redraw(
            lambda: Arrow(
                center,
                center + 1.0 * np.array([np.cos(theta2.get_value()), np.sin(theta2.get_value()), 0]),
                buff=0,
                color=ANGLE_PURPLE,
                stroke_width=LINE_MED,
            )
        )
        tip2 = always_redraw(
            lambda: Dot(center + 1.0 * np.array([np.cos(theta2.get_value()), np.sin(theta2.get_value()), 0]), color=ANGLE_PURPLE)
        )
        label_v2 = always_redraw(
            lambda: Text("V2", font_size=26, color=ANGLE_PURPLE).next_to(tip2, UL, buff=0.1)
        )
        result = always_redraw(
            lambda: Arrow(
                center,
                center
                + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0])
                + 1.0 * np.array([np.cos(theta2.get_value()), np.sin(theta2.get_value()), 0]),
                buff=0,
                color=TEXT_MAIN,
                stroke_width=LINE_MED,
            )
        )
        result_tip = always_redraw(
            lambda: Dot(
                center
                + radius * np.array([np.cos(theta.get_value()), np.sin(theta.get_value()), 0])
                + 1.0 * np.array([np.cos(theta2.get_value()), np.sin(theta2.get_value()), 0]),
                color=TEXT_MAIN,
            )
        )
        label_vt = always_redraw(
            lambda: Text("Vt", font_size=26, color=TEXT_MAIN).next_to(result_tip, UR, buff=0.1)
        )

        self.play(Create(vector2), FadeIn(tip2), FadeIn(label_v2), Create(result), FadeIn(result_tip), FadeIn(label_vt), run_time=1)
        self.wait(2)


class VIS02_VectorProjection(Scene):
    def construct(self):
        title = Text("Proyeksi Vektor", font_size=44, color=TEXT_MAIN)
        title.to_edge(UP)
        self.play(FadeIn(title), run_time=1)

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": AXIS, "stroke_width": LINE_THIN},
            background_line_style={"stroke_color": GRID, "stroke_width": 1},
        )
        self.play(Create(plane), run_time=1)

        vector = Arrow(plane.c2p(0, 0), plane.c2p(2.5, 1.5), buff=0, color=REAL_BLUE, stroke_width=LINE_MED)
        x_proj = Line(plane.c2p(2.5, 1.5), plane.c2p(2.5, 0), color=IMAG_ORANGE, stroke_width=LINE_THIN)
        y_proj = Line(plane.c2p(2.5, 1.5), plane.c2p(0, 1.5), color=IMAG_ORANGE, stroke_width=LINE_THIN)

        self.play(Create(vector), Create(x_proj), Create(y_proj), run_time=1)

        label_a = Text("a", font_size=28, color=IMAG_ORANGE).next_to(plane.c2p(2.5, 0), DOWN, buff=0.1)
        label_b = Text("b", font_size=28, color=IMAG_ORANGE).next_to(plane.c2p(0, 1.5), LEFT, buff=0.1)
        self.play(FadeIn(label_a), FadeIn(label_b), run_time=0.5)

        # Placeholder text for polar and rectangular
        polar = Text("Z = R ∠ θ", font_size=32, color=TEXT_MAIN).to_edge(DOWN).shift(LEFT * 2)
        rect = Text("Z = a + jb", font_size=32, color=TEXT_MAIN).to_edge(DOWN).shift(RIGHT * 2)
        self.play(FadeIn(polar), FadeIn(rect), run_time=1)

        self.wait(2)
