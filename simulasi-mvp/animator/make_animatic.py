import argparse
import subprocess
import sys
from pathlib import Path
import os


SCENES = [
    ("scenes/S1.py", "Segment1"),
    ("scenes/S2.py", "Segment2"),
]


def parse_args():
    parser = argparse.ArgumentParser(description="Render animatic Segmen 1-2 (Manim CE).")
    parser.add_argument("--format", default="16x9", choices=["16x9", "9x16"])
    parser.add_argument("--mode", default="preview", choices=["preview", "draft", "final"])
    parser.add_argument("--resume", default="on", choices=["on", "off"])
    parser.add_argument("--scene", default="all", choices=["S1", "S2", "all"])
    parser.add_argument("--shot", default="all")
    parser.add_argument("--resolution", default=None, choices=["360p", "540p", "720p", "1080p"])
    parser.add_argument("--renderer", default="cairo", choices=["cairo", "opengl"])
    parser.add_argument("--disable_glow", default=None, choices=["on", "off"])
    parser.add_argument("--simple_grid", default=None, choices=["on", "off"])
    parser.add_argument("--fps", default=None, type=int)
    parser.add_argument("--safearea", default="off", choices=["on", "off"])
    parser.add_argument("--concat", default="on", choices=["on", "off"])
    return parser.parse_args()


def quality_flag(mode):
    return {"preview": "-ql", "draft": "-qm", "final": "-qh"}[mode]


def mode_defaults(mode):
    if mode == "preview":
        return {"fps": 5, "resolution": "540p", "simple_grid": "on", "disable_glow": "on"}
    if mode == "draft":
        return {"fps": 12, "resolution": "720p", "simple_grid": "off", "disable_glow": "off"}
    return {"fps": 30, "resolution": "1080p", "simple_grid": "off", "disable_glow": "off"}


def resolution_from_height(fmt, size):
    if fmt == "16x9":
        width = int(round(size * 16 / 9))
        height = size
    else:
        width = size
        height = int(round(size * 16 / 9))
    return (width, height)


def height_from_resolution(res):
    return int(res.replace("p", ""))


def scene_output_path(media_dir, scene_short, height, fps, scene_name):
    return media_dir / "videos" / scene_short / f"{height}p{fps}" / f"{scene_name}.mp4"


def main():
    args = parse_args()
    defaults = mode_defaults(args.mode)
    fps = args.fps if args.fps is not None else defaults["fps"]
    resolution = args.resolution if args.resolution is not None else defaults["resolution"]
    height = height_from_resolution(resolution)
    width, height = resolution_from_height(args.format, height)
    root_dir = Path("renders").resolve()
    media_dir = root_dir / args.format
    media_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["ANIM_FORMAT"] = args.format
    env["SAFEAREA"] = args.safearea
    env["SIMPLE_GRID"] = args.simple_grid if args.simple_grid is not None else defaults["simple_grid"]
    env["DISABLE_GLOW"] = (
        args.disable_glow if args.disable_glow is not None else defaults["disable_glow"]
    )

    # Shot mode
    if args.shot != "all":
        shot_id = args.shot
        if shot_id.startswith("S1-"):
            scene_file, scene_name, scene_short = "scenes/S1.py", "Segment1", "S1"
        elif shot_id.startswith("S2-"):
            scene_file, scene_name, scene_short = "scenes/S2.py", "Segment2", "S2"
        else:
            print("Invalid shot id. Use S1-01..S2-04")
            return
        env["SHOT_ID"] = shot_id
        shots_dir = root_dir / "shots"
        shots_dir.mkdir(parents=True, exist_ok=True)
        shot_out = shots_dir / f"{shot_id}_{args.format}_{args.mode}.mp4"
        if args.resume == "on" and shot_out.exists():
            print("Resume on: shot output exists, skip", shot_out)
            return
        cmd = [
            sys.executable,
            "-m",
            "manim",
            quality_flag(args.mode),
            "--renderer",
            args.renderer,
            "--fps",
            str(fps),
            "-r",
            f"{width},{height}",
            "--media_dir",
            str(media_dir),
            scene_file,
            scene_name,
        ]
        print("Running:", " ".join(cmd))
        result = subprocess.run(cmd, env=env)
        if result.returncode != 0:
            raise SystemExit(result.returncode)
        src = scene_output_path(media_dir, scene_short, height, fps, scene_name)
        if src.exists():
            shot_out.write_bytes(src.read_bytes())
            print("Shot output:", shot_out)
        return

    # Scene mode
    scenes_to_run = SCENES
    if args.scene == "S1":
        scenes_to_run = [SCENES[0]]
    elif args.scene == "S2":
        scenes_to_run = [SCENES[1]]

    for scene_file, scene_name in scenes_to_run:
        scene_short = "S1" if "S1.py" in scene_file else "S2"
        out_path = scene_output_path(media_dir, scene_short, height, fps, scene_name)
        if args.resume == "on" and out_path.exists():
            print("Resume on: scene output exists, skip", out_path)
            continue
        cmd = [
            sys.executable,
            "-m",
            "manim",
            quality_flag(args.mode),
            "--renderer",
            args.renderer,
            "--fps",
            str(fps),
            "-r",
            f"{width},{height}",
            "--media_dir",
            str(media_dir),
            scene_file,
            scene_name,
        ]
        print("Running:", " ".join(cmd))
        result = subprocess.run(cmd, env=env)
        if result.returncode != 0:
            raise SystemExit(result.returncode)

    # concat Segment1 + Segment2 into a single preview file (scene=all only)
    if args.scene == "all" and args.concat == "on":
        quality_dir = f"{height}p{fps}"
        seg1_path = media_dir / "videos" / "S1" / quality_dir / "Segment1.mp4"
        seg2_path = media_dir / "videos" / "S2" / quality_dir / "Segment2.mp4"
        if not seg1_path.exists() or not seg2_path.exists():
            print("Missing scene outputs:", seg1_path, seg2_path)
            return

        concat_list = root_dir / f"concat_list_{args.format}_{args.mode}.txt"
        concat_list.write_text(
            f"file '{seg1_path.as_posix()}'\nfile '{seg2_path.as_posix()}'\n",
            encoding="utf-8",
        )

        output_name = f"CORE001_Seg1-2_{args.format}_{args.mode}.mp4"
        output_path = root_dir / output_name
        if args.resume == "on" and output_path.exists():
            print("Resume on: concat output exists, skip", output_path)
            return

        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(output_path),
        ]
        print("Concat:", " ".join(ffmpeg_cmd))
        subprocess.run(ffmpeg_cmd, check=False)


if __name__ == "__main__":
    main()
