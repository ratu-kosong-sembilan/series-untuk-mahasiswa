import os
from manim import Rectangle, Text, YELLOW, UP, config


FONT_TITLE = 36
FONT_BODY = 32
FONT_SMALL = 24


def get_format():
    return os.getenv("ANIM_FORMAT", "16x9")


def is_portrait():
    return get_format() == "9x16"

def simple_grid_on():
    return os.getenv("SIMPLE_GRID", "off") == "on"

def disable_glow_on():
    return os.getenv("DISABLE_GLOW", "off") == "on"


def on_screen_text(text, font_size=FONT_BODY):
    t = Text(text, font_size=font_size)
    t.to_edge(UP, buff=0.4)
    return t


def add_safe_area(scene):
    if os.getenv("SAFEAREA", "off") != "on":
        return None
    frame_w = config.frame_width
    frame_h = config.frame_height
    if is_portrait():
        margin_x = 0.10
        margin_y = 0.12
    else:
        margin_x = 0.08
        margin_y = 0.08
    rect = Rectangle(
        width=frame_w * (1 - 2 * margin_x),
        height=frame_h * (1 - 2 * margin_y),
        stroke_color=YELLOW,
        stroke_opacity=0.35,
        stroke_width=2,
    )
    rect.set_z_index(1000)
    scene.add(rect)
    return rect
