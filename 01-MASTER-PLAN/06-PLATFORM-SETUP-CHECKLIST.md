# PLATFORM SETUP CHECKLIST

## Tujuan
Menjamin semua kebutuhan platform produksi dan publikasi siap sebelum produksi berjalan.

## Ruang Lingkup
Repo, struktur folder, naming, render setting, export, QC, dan upload.

## Definisi Selesai (DoD)
- Checklist setup selesai 100%.
- SOP export dan QC terdokumentasi.
- Rujukan lintas dokumen tersedia.

## Checklist
- [x] Struktur folder dan naming convention
- [x] Render setting dan export setting
- [x] QC teknis dan konten
- [x] Upload dan metadata

## Rujukan
- [07-ANIMATION-STORYBOARD.md](./07-ANIMATION-STORYBOARD.md)
- [24-PRODUCTION-READY-PACKAGE.md](./24-PRODUCTION-READY-PACKAGE.md)

## Checklist Setup
### Repo & Struktur
- [ ] Folder: `01-MASTER-PLAN`, `02-MODUL-KONTEN`, `03-TEMPLATE`, `04-ASSETS`, `production`
- [ ] Naming: `CORE-001_SEG01_v01.mp4`, `CORE-001_SRT_v01.srt`

### Render Settings
- [ ] 16:9: 1920x1080, 30 fps, H.264, 20-25 Mbps
- [ ] 9:16: 1080x1920, 30 fps, H.264, 12-18 Mbps
- [ ] Audio: 48 kHz, AAC 320 kbps
- [ ] Export preset tersimpan (16:9 dan 9:16)

### QC (Technical)
- [ ] FPS konsisten
- [ ] Tidak ada frame hitam di awal/akhir
- [ ] Audio peak -3 dB, noise floor < -55 dB
- [ ] Subtitle sinkron 95%+
- [ ] Validasi SRT di editor (no overlap, no missing)
- [ ] Cek loudness terintegrasi (target -14 LUFS)

### Upload & Metadata
- [ ] Judul, deskripsi, tags
- [ ] Thumbnail 16:9 dan 9:16
- [ ] Chapter markers untuk long-form
- [ ] CTA di end screen

## Changelog
- 2026-02-06: Menyusun checklist setup platform dan QC.
- 2026-02-06: Tambah validasi SRT, cek loudness, dan preset export. Alasan: QC operasional. Dampak: konsistensi output 16:9 dan 9:16 terjaga.
