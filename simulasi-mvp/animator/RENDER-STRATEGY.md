# RENDER STRATEGY (SEG1-SEG2)

## Workflow Rekomendasi
1. Preview per-shot (cek framing & safe area)
2. Preview per-scene (cek pacing per segmen)
3. Draft per-scene (review tim)
4. Final per-scene (output master)

## Command Examples
### Preview per-shot (16:9)
```powershell
python make_animatic.py --format 16x9 --mode preview --shot S1-01 --resume on
python make_animatic.py --format 16x9 --mode preview --shot S2-04 --resume on
```

### Preview per-scene (9:16)
```powershell
python make_animatic.py --format 9x16 --mode preview --scene S1 --resume on
python make_animatic.py --format 9x16 --mode preview --scene S2 --resume on
```

### Draft per-scene (16:9)
```powershell
python make_animatic.py --format 16x9 --mode draft --scene all --resume on
```

### Final per-scene (16:9)
```powershell
python make_animatic.py --format 16x9 --mode final --scene all --resume on
```

## Recover from Timeout
1. Jalankan preview per-shot untuk verifikasi framing.
2. Gunakan `--resume on` agar scene yang sudah jadi tidak dirender ulang.
3. Jika concat output sudah ada, runner akan skip otomatis.

## Output Paths
- Per-shot: `renders/shots/<ShotID>_<format>_<mode>.mp4`
- Per-scene: `renders/<format>/videos/<S1|S2>/<height>p<fps>/Segment*.mp4`
- Gabungan (scene=all): `renders/CORE001_Seg1-2_<format>_<mode>.mp4`
