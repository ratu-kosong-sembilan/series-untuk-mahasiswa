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
    ("S1-01", "shot_S1_01"),
    ("S1-02", "shot_S1_02"),
    ("S1-03", "shot_S1_03"),
    ("S1-04", "shot_S1_04"),
]


class Segment1(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.safe_area = add_safe_area(self)
        shot_id = os.getenv("SHOT_ID", "")
        if shot_id:
            self.render_shot(shot_id)
            return
        self.shot_S1_01(duration=45)
        self.shot_S1_02(duration=75)
        self.shot_S1_03(duration=60)
        self.shot_S1_04(duration=60)

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
            "S1-01": lambda: self.shot_S1_01(duration=45),
            "S1-02": lambda: self.shot_S1_02(duration=75),
            "S1-03": lambda: self.shot_S1_03(duration=60),
            "S1-04": lambda: self.shot_S1_04(duration=60),
        }
        if shot_id in dispatch:
            dispatch[shot_id]()

    # Shot S1-01 (00:00:00,000-00:00:45,000)
    def shot_S1_01(self, duration):
        shot_label = self._shot_label("S1-01")
        on_screen = self._on_screen("Imaginasi yang menyederhanakan listrik nyata")

        frame_w = config.frame_width
        frame_h = config.frame_height
        if is_portrait():
            box_w = frame_w * 0.9
            box_h = frame_h * 0.24
            left_box = Rectangle(width=box_w, height=box_h)
            right_box = Rectangle(width=box_w, height=box_h)
            boxes = VGroup(left_box, right_box).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)
        else:
            box_w = frame_w * 0.45
            box_h = frame_h * 0.42
            left_box = Rectangle(width=box_w, height=box_h)
            right_box = Rectangle(width=box_w, height=box_h)
            boxes = VGroup(left_box, right_box).arrange(RIGHT, buff=0.4)

        left_box, right_box = boxes[0], boxes[1]
        left_title = Text("Time-domain", font_size=28).next_to(left_box, UP, buff=0.2)
        right_title = Text("Phasor", font_size=28).next_to(right_box, UP, buff=0.2)

        left_eq = Text(
            "v(t) = Vm sin(omega t + phi)\n"
            "i(t) = Im sin(omega t + phi)",
            font_size=FONT_SMALL,
            line_spacing=0.8,
        ).move_to(left_box)
        right_eq = Text(
            "V angle phi\nZ = R + jX", font_size=FONT_BODY, line_spacing=0.9
        ).move_to(right_box)

        items = VGroup(left_box, right_box, left_title, right_title, left_eq, right_eq)
        if shot_label:
            items.add(shot_label)
        items.add(on_screen)

        self.play(FadeIn(items), run_time=1.6)
        tmp = left_title.copy()
        self.play(Transform(tmp, right_title), run_time=0.6)
        self.remove(tmp)
        # Push-in 5% to the phasor side (horizontal) or center (portrait)
        target = right_box.get_center() if not is_portrait() else boxes.get_center()
        self.play(
            self.camera.frame.animate.scale(0.95).move_to(target),
            run_time=1.2,
        )
        self._hold(duration, used_time=3.4)

    # Shot S1-02 (00:00:45,000-00:02:00,000)
    def shot_S1_02(self, duration):
        self._clear()
        self.camera.frame.restore()

        shot_label = self._shot_label("S1-02")
        on_screen = self._on_screen("Bukan hafal, tapi paham")

        z_left = Text("Z = R +", font_size=64)
        z_jx = Text("jX", font_size=64).set_color(YELLOW)
        z_group = VGroup(z_left, z_jx).arrange(RIGHT, buff=0.2)

        note = Text("Kenapa ada j?", font_size=FONT_BODY).next_to(z_group, DOWN, buff=0.6)

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(FadeIn(z_group), run_time=1.2)
        if disable_glow_on():
            self.play(z_jx.animate.set_color(ORANGE), run_time=0.4)
            self.play(z_jx.animate.set_color(YELLOW), run_time=0.4)
        else:
            self.play(Indicate(z_jx, scale_factor=1.2), run_time=0.6)
        self.play(FadeIn(note), run_time=0.6)
        self._hold(duration, used_time=2.4)

    # Shot S1-03 (00:02:00,000-00:03:00,000)
    def shot_S1_03(self, duration):
        self._clear()

        shot_label = self._shot_label("S1-03")
        on_screen = self._on_screen("Gelombang = vektor berputar")

        radius = 2.0 if not is_portrait() else 1.6
        circle = Circle(radius=radius)
        angle = ValueTracker(0)

        def vec_end():
            return np.array([np.cos(angle.get_value()), np.sin(angle.get_value()), 0]) * radius

        vector = always_redraw(lambda: Arrow(ORIGIN, vec_end(), buff=0, stroke_width=6))
        tip_dot = always_redraw(lambda: Dot(vec_end(), radius=0.06, color=YELLOW))
        if simple_grid_on():
            proj_line = always_redraw(
                lambda: Line(
                    vec_end(),
                    np.array([vec_end()[0], 0, 0]),
                    stroke_width=2,
                    stroke_opacity=0.5,
                )
            )
        else:
            proj_line = always_redraw(
                lambda: DashedLine(
                    vec_end(),
                    np.array([vec_end()[0], 0, 0]),
                    stroke_width=3,
                    stroke_opacity=0.6,
                    dash_length=0.15,
                )
            )
        vector_group = VGroup(circle, vector, proj_line, tip_dot)

        axes = Axes(x_range=[0, 2 * PI, PI / 2], y_range=[-1.2, 1.2, 1.0], x_length=5, y_length=2.5)
        sine = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_group = VGroup(axes, sine)
        if is_portrait():
            vector_group.shift(UP * 1.8)
            sine_group.shift(DOWN * 1.8)
        else:
            vector_group.shift(LEFT * 3.0)
            sine_group.shift(RIGHT * 3.0)

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(Create(circle), GrowArrow(vector), run_time=1.2)
        self.add(proj_line, tip_dot)
        self.play(Create(axes), Create(sine), run_time=1.2)
        self.play(angle.animate.set_value(TAU), run_time=2.0, rate_func=linear)
        self._hold(duration, used_time=4.4)

    # Shot S1-04 (00:03:00,000-00:04:00,000)
    def shot_S1_04(self, duration):
        self._clear()

        shot_label = self._shot_label("S1-04")
        on_screen = self._on_screen("Phasor -> Impedansi -> Faktor daya")

        box_w = 3.2 if not is_portrait() else 4.0
        box_h = 1.4
        box1 = RoundedRectangle(width=box_w, height=box_h, corner_radius=0.2)
        box2 = RoundedRectangle(width=box_w, height=box_h, corner_radius=0.2)
        box3 = RoundedRectangle(width=box_w, height=box_h, corner_radius=0.2)
        text1 = Text("Phasor", font_size=FONT_BODY)
        text2 = Text("Impedansi", font_size=FONT_BODY)
        text3 = Text("Faktor daya", font_size=FONT_BODY)

        g1 = VGroup(box1, text1)
        g2 = VGroup(box2, text2)
        g3 = VGroup(box3, text3)
        for g in (g1, g2, g3):
            g[1].move_to(g[0].get_center())

        if is_portrait():
            roadmap = VGroup(g1, g2, g3).arrange(DOWN, buff=0.4)
        else:
            roadmap = VGroup(g1, g2, g3).arrange(RIGHT, buff=0.6)
        roadmap.shift(DOWN * 0.4)

        if shot_label:
            self.add(shot_label)
        self.add(on_screen)
        self.play(FadeIn(g1, shift=LEFT), run_time=0.5)
        self.play(FadeIn(g2, shift=LEFT), run_time=0.5)
        self.play(FadeIn(g3, shift=LEFT), run_time=0.5)
        self._hold(duration, used_time=1.5)
