from manim import *
import os
import numpy as np
from common import (
    FONT_BODY,
    FONT_SMALL,
    add_safe_area,
    is_portrait,
    on_screen_text,
    simple_grid_on,
    disable_glow_on,
)

DEBUG_SHOT_LABELS = False

SHOT_MAP = [
    ("S2-01", "shot_S2_01"),
    ("S2-02", "shot_S2_02"),
    ("S2-03", "shot_S2_03"),
    ("S2-04", "shot_S2_04"),
]


class Segment2(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.safe_area = add_safe_area(self)
        shot_id = os.getenv("SHOT_ID", "")
        if shot_id:
            self.render_shot(shot_id)
            return
        self.shot_S2_01(duration=60)
        self.shot_S2_02(duration=60)
        self.shot_S2_03(duration=60)
        self.shot_S2_04(duration=60)

    def _shot_label(self, text):
        if not DEBUG_SHOT_LABELS:
            return None
        label = Text(text, font_size=22).set_color(YELLOW)
        label.to_corner(UR, buff=0.2)
        return label

    def _on_screen(self, text):
        return on_screen_text(text, font_size=FONT_BODY)

    def _hold(self, duration, used_time):
        remaining = max(0.0, duration - used_time)
        if remaining > 0:
            self.wait(remaining)

    def _clear(self):
        keep = []
        if getattr(self, "safe_area", None) in self.mobjects:
            keep.append(self.safe_area)
        targets = [m for m in self.mobjects if m not in keep]
        if targets:
            self.play(FadeOut(*targets), run_time=0.6)

    def render_shot(self, shot_id):
        dispatch = {
            "S2-01": lambda: self.shot_S2_01(duration=60),
            "S2-02": lambda: self.shot_S2_02(duration=60),
            "S2-03": lambda: self.shot_S2_03(duration=60),
            "S2-04": lambda: self.shot_S2_04(duration=60),
        }
        if shot_id in dispatch:
            dispatch[shot_id]()

    # Shot S2-01 (00:04:00,000-00:05:00,000)
    def shot_S2_01(self, duration):
        shot_label = self._shot_label("S2-01")
        on_screen = self._on_screen("v(t) = Vm sin(omega t + phi)")

        x_len = 8 if not is_portrait() else 5.5
        y_len = 3 if not is_portrait() else 2.6
        axes = Axes(x_range=[0, 2 * PI, PI / 2], y_range=[-1.2, 1.2, 1.0], x_length=x_len, y_length=y_len)
        sine = axes.plot(lambda x: np.sin(x), color=BLUE)

        labels = VGroup(
            Text("Vm", font_size=FONT_SMALL).next_to(axes, LEFT, buff=0.2),
            Text("omega", font_size=FONT_SMALL).next_to(axes, DOWN, buff=0.2),
            Text("phi", font_size=FONT_SMALL).next_to(axes, RIGHT, buff=0.2),
        )

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(Create(axes), Create(sine), run_time=1.2)
        self.play(FadeIn(labels), run_time=0.6)
        self._hold(duration, used_time=1.8)

    # Shot S2-02 (00:05:00,000-00:06:00,000)
    def shot_S2_02(self, duration):
        self._clear()

        shot_label = self._shot_label("S2-02")
        on_screen = self._on_screen("delta t <-> delta phi")

        x_len = 8 if not is_portrait() else 5.5
        y_len = 3 if not is_portrait() else 2.6
        axes = Axes(x_range=[0, 2 * PI, PI / 2], y_range=[-1.2, 1.2, 1.0], x_length=x_len, y_length=y_len)
        sine1 = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine2 = axes.plot(lambda x: np.sin(x - PI / 3), color=GREEN)
        legend = VGroup(
            Dot(color=BLUE), Text("gelombang 1", font_size=FONT_SMALL),
            Dot(color=GREEN), Text("gelombang 2", font_size=FONT_SMALL),
        ).arrange(RIGHT, buff=0.2)
        legend.next_to(axes, DOWN, buff=0.3)

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(Create(axes), run_time=0.6)
        self.play(Create(sine1), Create(sine2), run_time=1.0)
        self.play(FadeIn(legend), run_time=0.6)
        self._hold(duration, used_time=2.2)

    # Shot S2-03 (00:06:00,000-00:07:00,000)
    def shot_S2_03(self, duration):
        self._clear()

        shot_label = self._shot_label("S2-03")
        on_screen = self._on_screen("e^(jtheta) = cos theta + j sin theta")

        circle = Circle(radius=2.0 if not is_portrait() else 1.6)
        angle_arc = Arc(radius=1.0, angle=PI / 3)
        theta_label = Text("theta", font_size=FONT_SMALL).next_to(angle_arc, RIGHT, buff=0.1)
        vector = Arrow(ORIGIN, RIGHT * 2.2, buff=0)

        group = VGroup(circle, angle_arc, theta_label, vector).shift(DOWN * 0.2)

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(Create(circle), GrowArrow(vector), run_time=1.0)
        self.play(Create(angle_arc), FadeIn(theta_label), run_time=0.8)
        self._hold(duration, used_time=1.8)

    # Shot S2-04 (00:07:00,000-00:08:00,000)
    def shot_S2_04(self, duration):
        self._clear()

        shot_label = self._shot_label("S2-04")
        on_screen = self._on_screen("Bidang kompleks: a + jb, phasor dan fase")

        if simple_grid_on():
            x_rng = [-2, 2, 1]
            y_rng = [-2, 2, 1]
            opacity = 0.18
        else:
            x_rng = [-3, 3, 1]
            y_rng = [-3, 3, 1]
            opacity = 0.25
        plane = NumberPlane(
            x_range=x_rng,
            y_range=y_rng,
            x_length=6 if not is_portrait() else 4.5,
            y_length=6 if not is_portrait() else 4.5,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_opacity": opacity,
                "stroke_width": 1,
            },
            axis_config={"stroke_width": 2},
        )
        plane.add_coordinates()

        vector = Arrow(ORIGIN, RIGHT * 2 + UP * 1.5, buff=0, stroke_width=6)
        a_label = Text("a", font_size=FONT_SMALL).next_to(vector.get_end(), RIGHT, buff=0.1)
        b_label = Text("b", font_size=FONT_SMALL).next_to(vector.get_end(), UP, buff=0.1)
        z_text = Text("Z = a + jb", font_size=FONT_BODY).next_to(plane, RIGHT, buff=0.6)
        phasor_text = Text("Phasor = magnitude + fase", font_size=FONT_SMALL).next_to(
            z_text, DOWN, buff=0.3
        )

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(Create(plane), run_time=1.0)
        self.play(GrowArrow(vector), run_time=0.8)
        self.play(FadeIn(a_label), FadeIn(b_label), run_time=0.6)
        self.play(FadeIn(z_text), FadeIn(phasor_text), run_time=0.6)
        self._hold(duration, used_time=3.0)
