import json
import subprocess
from pathlib import Path


OUTPUTS = [
    ("draft", "16x9", Path("renders/CORE001_Seg1-2_16x9_draft.mp4")),
    ("draft", "9x16", Path("renders/CORE001_Seg1-2_9x16_draft.mp4")),
    ("final", "16x9", Path("renders/CORE001_Seg1-2_16x9_final.mp4")),
    ("final", "9x16", Path("renders/CORE001_Seg1-2_9x16_final.mp4")),
]


def ffprobe_info(path: Path):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,avg_frame_rate,r_frame_rate",
        "-show_entries",
        "format=duration",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None, result.stderr.strip()
    data = json.loads(result.stdout or "{}")
    return data, None


def parse_fps(rate_str):
    if not rate_str or rate_str == "0/0":
        return None
    num, den = rate_str.split("/")
    try:
        num = float(num)
        den = float(den)
        if den == 0:
            return None
        return num / den
    except Exception:
        return None


def expected_resolution(mode, fmt):
    if mode != "final":
        return None
    return (1920, 1080) if fmt == "16x9" else (1080, 1920)


def expected_fps(mode):
    if mode == "final":
        return 30
    if mode == "draft":
        return 12
    return 5


def main():
    print("QC CHECK OUTPUTS")
    print("=" * 60)
    all_ok = True
    for mode, fmt, path in OUTPUTS:
        print(f"\n[{mode.upper()}] {fmt} -> {path.as_posix()}")
        if not path.exists():
            print("  MISSING: file not found")
            all_ok = False
            continue

        data, err = ffprobe_info(path)
        if err:
            print(f"  ERROR: ffprobe failed: {err}")
            all_ok = False
            continue

        streams = data.get("streams", [])
        fmt_info = data.get("format", {})
        duration = float(fmt_info.get("duration", 0) or 0)
        if not streams:
            print("  ERROR: no video stream")
            all_ok = False
            continue

        s = streams[0]
        width = int(s.get("width", 0) or 0)
        height = int(s.get("height", 0) or 0)
        fps = parse_fps(s.get("avg_frame_rate")) or parse_fps(s.get("r_frame_rate"))

        print(f"  duration: {duration:.2f}s")
        print(f"  resolution: {width}x{height}")
        print(f"  fps: {fps:.2f}" if fps else "  fps: unknown")

        if duration <= 0.5:
            print("  FAIL: duration too short")
            all_ok = False

        expected = expected_resolution(mode, fmt)
        if expected:
            if (width, height) != expected:
                print(f"  FAIL: expected resolution {expected[0]}x{expected[1]}")
                all_ok = False

        target_fps = expected_fps(mode)
        if fps:
            if abs(fps - target_fps) > 0.5:
                print(f"  WARN: fps {fps:.2f} != target {target_fps}")
        else:
            print("  WARN: fps not detected")

    print("\nSUMMARY")
    print("PASS" if all_ok else "CHECK WARN/FAIL ABOVE")


if __name__ == "__main__":
    main()
