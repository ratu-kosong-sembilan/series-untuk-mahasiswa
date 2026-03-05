# PRODUCTION READY PACKAGE (CORE-001)

## Tujuan
Menjadi single source of truth untuk semua dokumen dan checklist siap produksi.

## Ruang Lingkup
Script, storyboard, asset, simulasi, VO, SRT, QC, dan publishing.

## Definisi Selesai (DoD)
- Semua dokumen tertaut dan status Ready.
- Checklist QC dan export lengkap.
- Tim bisa produksi tanpa penjelasan tambahan.

## Checklist
- [x] Semua dokumen terhubung
- [x] Checklist QC dan export tersedia
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [00-DOCUMENT-REFERENCE-INDEX.md](./00-DOCUMENT-REFERENCE-INDEX.md)
- [QA-CROSSCHECK-REPORT.md](./QA-CROSSCHECK-REPORT.md)

## Start Here
Urutan eksekusi produksi (ringkas):
1. Baca QA report untuk keputusan final.
2. Lock animatic segmen 1-2, lanjut produksi segmen 3-4.
3. Produksi aset prioritas tinggi dari shotlist.

## Urutan Eksekusi per Role
### VO Talent
1. Baca `17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md` segmen 1-2.
2. Rekam VO segmen 1-2 sesuai timecode.
3. Kirim take bersih untuk sinkron editor.

### Animator
1. Gunakan `18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md` segmen 1-2 (LOCKED).
2. Produksi animatic segmen 1-2, lalu mulai segmen 3-4.
3. Simpan render per segmen dengan naming standar.

### Editor
1. Impor VO segmen 1-2 dan animatic segmen 1-2.
2. Sinkron SRT dari `26-SRT-LENGKAP-40-MENIT.md`.
3. QC audio/visual lalu lanjut segmen 3-4.

## Paket Dokumen Inti
- [ANIMATIC-PACK-SEG1-SEG2.md](./ANIMATIC-PACK-SEG1-SEG2.md)
- [17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md](./17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md)
- [18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md](./18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md)
- [19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md](./19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md)
- [20-NASKAH-DETAIL-PER-MENIT.md](./20-NASKAH-DETAIL-PER-MENIT.md)
- [21-UI-SIMULASI-WIREFRAME.md](./21-UI-SIMULASI-WIREFRAME.md)
- [22-QUIZ-BANK-SOAL-MATEMATIKA-EM-TRANSIEN.md](./22-QUIZ-BANK-SOAL-MATEMATIKA-EM-TRANSIEN.md)
- [23-ASSET-SHOTLIST-MATEMATIKA-EM-TRANSIEN.md](./23-ASSET-SHOTLIST-MATEMATIKA-EM-TRANSIEN.md)
- [25-VO-SUBTITLE-SRT.md](./25-VO-SUBTITLE-SRT.md)
- [26-SRT-LENGKAP-40-MENIT.md](./26-SRT-LENGKAP-40-MENIT.md)
- [27-STORYBOARD-DETAIL-FRAME.md](./27-STORYBOARD-DETAIL-FRAME.md)

## QC Checklist (Final)
- [ ] Durasi 40:00 (+/-2 menit)
- [ ] Audio bersih, peak -3 dB
- [ ] Subtitle sinkron (>=95%)
- [ ] Konsistensi warna V/I/Z
- [ ] Tidak ada typo di formula

## Definition of Done (Sign-off)
- [ ] Script segmen 1-2 locked (PM)
- [ ] Storyboard segmen 1-2 locked (PM/Animator)
- [ ] Animatic segmen 1-2 approved (Animator/Editor)
- [ ] SRT segmen 1-2 validated (Editor)
- [ ] QC audio/visual segmen 1-2 pass (QA)
- [ ] Segmen 3-4 ready to produce (PM)

## Export Settings
- 16:9: 1920x1080, 30 fps, H.264, 20-25 Mbps
- 9:16: 1080x1920, 30 fps, H.264, 12-18 Mbps
- Audio: 48 kHz, AAC 320 kbps

## Publishing Steps
1. Upload master 16:9
2. Upload Shorts 9:16
3. Tambahkan chapter marker
4. Tambahkan CTA dan end screen

## Changelog
- 2026-02-06: Menyusun paket final siap produksi CORE-001.
- 2026-02-06: Tambah Start Here, urutan eksekusi per role, dan DoD sign-off + link QA. Alasan: pintu utama eksekusi. Dampak: tim bisa mulai produksi tanpa ambiguity.
- 2026-02-06: Tambah link animatic pack segmen 1-2. Alasan: pintu cepat ke shot list. Dampak: animator mudah akses.
