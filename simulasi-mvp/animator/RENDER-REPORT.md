# RENDER REPORT (SEG1-SEG2)

## Environment
- Python: 3.12.9
- Manim: 0.19.2
- ffmpeg: 8.0.1-essentials_build

## Commands Executed
1. `python make_animatic.py --format 16x9 --mode preview --scene S1 --resume on`
2. `python make_animatic.py --format 16x9 --mode preview --shot S1-01 --resume on`
3. (Belum dijalankan) `python make_animatic.py --format 9x16 --mode preview --scene S1 --resume on`
4. (Belum dijalankan) `python make_animatic.py --format 16x9 --mode preview --scene S2 --resume on`

## Legacy Attempts (Pre Fast-Preview)
1. `python make_animatic.py --format 16x9 --quality low --safearea off` (timeout)
2. `python make_animatic.py --format 16x9 --quality low --safearea off --fps 12` (timeout)
3. `python make_animatic.py --format 16x9 --quality low --safearea off --fps 5` (timeout)

## Result
- Preview per-scene S1 (16:9, 540p5) tersedia:
  `simulasi-mvp/animator/renders/videos/S1/540p5/Segment1.mp4`
- Preview per-shot S1-01 (16:9) tersedia:
  `simulasi-mvp/animator/renders/shots/S1-01_16x9_preview.mp4`
- Resume sudah terverifikasi (skip ketika output sudah ada).
- S2 preview dan concat output belum dijalankan.

## Render Time (Approx)
- Preview per-shot S1-01: ~6 detik (cache aktif).
- Resume check S1 scene: < 1 detik.

## Output Paths (Expected)
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_preview.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_preview.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_draft.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_draft.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_final.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_final.mp4`

## Issues / Notes
- Durasi total segmen 1-2 (8 menit) membuat render full masih berat pada 1080p.
- Ada `RuntimeWarning: manim.__main__` saat run per-shot, namun render sukses.
- Partial movie files dari percobaan lama masih tersimpan di `renders/videos/S1/`.

## Timeout Mitigation Plan
1. Gunakan `--mode preview` (fps 5, 540p, simple_grid on, disable_glow on).
2. Render per-shot untuk cek framing: `--shot S1-01` dst.
3. Gunakan `--resume on` agar hasil tidak diulang.
4. Naikkan ke draft/final hanya setelah preview lulus.

## Mode Parameter Table
| Mode | fps | Resolution | simple_grid | disable_glow |
| --- | --- | --- | --- | --- |
| preview | 5 | 540p | on | on |
| draft | 12 | 720p | off | off |
| final | 30 | 1080p | off | off |

## Changes Applied
- Added fast preview mode + resume + per-shot render.
- Added simple grid and disable glow toggles.
- Refactor S1/S2 to support shot dispatch.

## Recommended Fix
1. Jalankan preview S2 + 9:16 terlebih dahulu untuk cek framing.
2. Setelah preview lulus, lanjutkan draft lalu final per-scene.
3. Bersihkan partial files lama jika storage bermasalah.
