# README ANIMATOR (CORE-001 SEG1-SEG2)

## Tujuan
Menjalankan animatic Segmen 1-2 (Manim CE) sesuai timecode dan storyboard yang sudah LOCK.

## Struktur
- `scenes/S1.py` : Segmen 1 (00:00-04:00)
- `scenes/S2.py` : Segmen 2 (04:00-08:00)
- `make_animatic.py` : runner batch render
- `assets/svg/` : placeholder SVG
- `renders/` : output render (lokasi media manim)

## Dependensi
- Python 3.10+
- Manim Community Edition
- ffmpeg (wajib untuk render)

## Install (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Render Preview (cepat)
Jalankan dari folder `simulasi-mvp/animator`:
```powershell
python make_animatic.py --format 16x9 --mode preview --scene S1 --resume on
python make_animatic.py --format 9x16 --mode preview --scene S1 --resume on
```

## Render Preview (dengan Safe Area)
```powershell
python make_animatic.py --format 16x9 --mode preview --scene S1 --safearea on --resume on
python make_animatic.py --format 9x16 --mode preview --scene S1 --safearea on --resume on
```

## Render Per-Shot (Debug)
```powershell
python make_animatic.py --format 16x9 --mode preview --shot S1-01 --resume on
python make_animatic.py --format 9x16 --mode preview --shot S2-04 --resume on
```

## Render Draft / Final
```powershell
python make_animatic.py --format 16x9 --mode draft --scene all --resume on
python make_animatic.py --format 16x9 --mode final --scene all --resume on
```

## Override Resolution / Renderer
```powershell
python make_animatic.py --format 16x9 --mode preview --resolution 360p --renderer cairo
python make_animatic.py --format 9x16 --mode preview --resolution 540p --renderer opengl
```

## Output
Manim akan menaruh hasil render di:
`simulasi-mvp/animator/renders/<format>/videos/<S1|S2>/<height>p<fps>/`

File gabungan (scene=all):
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_preview.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_draft.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_16x9_final.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_preview.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_draft.mp4`
- `simulasi-mvp/animator/renders/CORE001_Seg1-2_9x16_final.mp4`

Output per-shot:
- `simulasi-mvp/animator/renders/shots/<ShotID>_<format>_<mode>.mp4`

## VO Timing Track (Cue Per Shot)
| ShotID | Timecode | Cue Ringkas |
| --- | --- | --- |
| S1-01 | 00:00-00:45 | Hook: simbol j menyederhanakan perhitungan AC |
| S1-02 | 00:45-02:00 | Masalah: hafal Z=R+jX tapi tidak paham |
| S1-03 | 02:00-03:00 | Target: gelombang = vektor berputar |
| S1-04 | 03:00-04:00 | Roadmap: phasor -> impedansi -> faktor daya |
| S2-01 | 04:00-05:00 | Sinus: v(t)=Vm sin(omega t + phi) |
| S2-02 | 05:00-06:00 | Pergeseran fase: delta t <-> delta phi |
| S2-03 | 06:00-07:00 | Euler: e^(jtheta)=cos theta + j sin theta |
| S2-04 | 07:00-08:00 | Bidang kompleks: a + jb, phasor, fase |

## Import SRT ke Editor (bukan ke Manim)
1. Buka editor (Premiere/DaVinci/CapCut).
2. Import file `01-MASTER-PLAN/26-SRT-LENGKAP-40-MENIT.md`:
   - Salin blok SRT (di dalam ```srt) ke file `.srt` terpisah.
3. Import `.srt` ke timeline video.
4. Cek sinkron segmen 1-2 (timecode 00:00-08:00).

## Troubleshooting
- Manim tidak jalan: pastikan `ffmpeg` terinstall dan ada di PATH.
- Error font: ganti ke font default dengan `Text(..., font="DejaVu Sans")`.
- Render lambat: gunakan `--mode preview` dan `--resolution 540p` atau `360p`.
- Resume tidak jalan: pastikan output file ada, lalu jalankan ulang dengan `--resume on`.
- Output gabungan tidak muncul: cek `renders/videos/` lalu pastikan `ffmpeg` tersedia.

## Catatan
- Beberapa aset (A-02/A-04/A-05) masih placeholder SVG. Lihat `CHANGE-REQUEST-LOG.md`.
- File animatic pack dibuat dari dokumen LOCK: `01-MASTER-PLAN/ANIMATIC-PACK-SEG1-SEG2.md`.
