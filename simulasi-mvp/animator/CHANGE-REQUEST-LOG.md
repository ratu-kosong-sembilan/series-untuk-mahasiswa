# CHANGE REQUEST LOG

## 2026-02-06
1. File `01-MASTER-PLAN/ANIMATIC-PACK-SEG1-SEG2.md` dibuat dari dokumen LOCK.  
   - Aksi: mapping ShotID berdasarkan storyboard dan script.  
   - Dampak: shot list konsisten dengan timecode.

2. Aset A-02/A-04/A-05 belum tersedia.  
   - Aksi: gunakan placeholder SVG berlabel di `assets/svg/`.  
   - Dampak: animatic bisa jalan, asset final perlu diganti.

3. Refinement visual (grid styling, projection lines, safe area overlay).  
   - Aksi: tambah `scenes/common.py` dan update S1/S2.  
   - Dampak: visual lebih rapi dan aman untuk 9:16.

4. Render error: Camera frame tidak tersedia pada `Scene`.  
   - Aksi: ubah `Segment1` dan `Segment2` ke `MovingCameraScene`.  
   - Dampak: zoom/push-in berjalan dan render tidak error.

5. Render error: `UP` not defined pada `common.py`.  
   - Aksi: tambahkan import `UP`.  
   - Dampak: on-screen text positioning berjalan.

6. Update runner untuk safearea dan concat output.  
   - Aksi: tambah flag `--safearea` dan concat ffmpeg pada `make_animatic.py`.  
   - Dampak: overlay guide bisa ON/OFF dan output gabungan siap.

7. Render preview timeout (durasi panjang).  
   - Aksi: catat di `RENDER-REPORT.md` dan turunkan fps untuk percobaan.  
   - Dampak: butuh waktu render lebih panjang untuk output final.

8. Tambah FAST PREVIEW MODE + resume + shot render.  
   - Aksi: update `make_animatic.py`, refactor shot dispatcher di S1/S2.  
   - Dampak: render cepat dan debugging per-shot tersedia.

9. Tambah strategi render dan parameter mode.  
   - Aksi: buat `RENDER-STRATEGY.md` + update `RENDER-REPORT.md`.  
   - Dampak: workflow render lebih jelas dan repeatable.

10. Verifikasi render cepat + resume + per-shot.  
    - Aksi: jalankan preview S1 dan shot S1-01, update `RENDER-REPORT.md`.  
    - Dampak: output preview tersedia dan resume terbukti skip output.

11. Update README animator ke flag baru (`--mode`, `--scene`, `--shot`).  
    - Aksi: revisi command contoh dan output path.  
    - Dampak: panduan render sesuai pipeline baru.

12. QC checklist diperbarui untuk status preview/resume.  
    - Aksi: tandai item QC tambahan sebagai pass.  
    - Dampak: kualitas pipeline render tervalidasi sebagian.

13. Fix collision output path antara 16:9 dan 9:16.  
    - Aksi: pisahkan `media_dir` per format (`renders/<format>/...`).  
    - Dampak: resume dan output per-format tidak saling menimpa.

14. Fix resolusi 9:16 agar sesuai ukuran vertikal (1080x1920).  
    - Aksi: ubah perhitungan resolusi supaya input `1080p` menjadi 1080x1920 untuk format 9:16.  
    - Dampak: output 9:16 final/draft sesuai spesifikasi.
