# QA CROSSCHECK REPORT (CORE-001)

## Tujuan
Memastikan konsistensi lintas dokumen dan menutup semua loose ends agar produksi CORE-001 bisa dimulai tanpa ambiguity.

## Ruang Lingkup
Dokumen utama: 24, 05, 20, 17, 18, 23, 26, 09, 06.

## Definisi Selesai (DoD)
- Checklist QC terverifikasi.
- Inkonstistensi tercatat dan diputuskan.
- Semua perubahan tercatat per file.

## Checklist QC (Pass/Fail)
| Item | Status | Catatan |
| --- | --- | --- |
| Durasi long-form 40:00 konsisten | Pass | Sesuai 24, 05, 20 |
| Terminologi (phasor, fase, phi, omega) | Pass | Diseragamkan |
| Segmen 1-2 locked (script+storyboard+timeline) | Pass | Timecode HH:MM:SS,mmm |
| On-screen text segmen 1-2 <= 16 kata | Pass | Ringkas |
| Instruksi visual segmen 1-2 cukup spesifik | Pass | Kamera/transisi ditambah |
| SRT indeks berurutan | Pass | 1-40 |
| SRT overlap time | Pass | Tidak ada overlap |
| SRT gap terlalu panjang | Pass | Kontinu per menit |
| Panjang baris SRT 32-42 karakter | Pass | Dirapikan per baris |
| Status produksi segmen 1-4 jelas | Pass | Dashboard diupdate |

## Temuan Inkonsistensi
1. "phase/phase shift" vs "fase/pergeseran fase" (05, 20, 18, 26) -> Diseragamkan ke "fase".
2. Format timecode campur mm:ss vs HH:MM:SS,mmm (17, 18, 20) -> Segmen 1-2 di-lock ke HH:MM:SS,mmm; timeline penuh diupdate.
3. "quiz" vs "kuis" (lintas dokumen) -> Diseragamkan ke "kuis".
4. "fasor" vs "phasor" (03-KURIKULUM) -> Diseragamkan ke "phasor".
5. Notasi impedansi jomega (17, 26) -> Diseragamkan ke "j omega".

## Keputusan Final (Source of Truth)
1. Ikuti 24-PRODUCTION-READY-PACKAGE sebagai pintu utama.
2. Durasi final long-form: 40:00.
3. Terminologi: phasor, fase, phi, omega, notasi kompleks a + jb.
4. Format timecode: HH:MM:SS,mmm untuk segmen 1-2 dan timeline.

## Perubahan yang Dilakukan (Per File)
- `01-MASTER-PLAN/17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md`: lock segmen 1-2, detail kamera/transisi, konsistensi istilah. Alasan: animatic-ready. Dampak: VO dan animasi lebih presisi.
- `01-MASTER-PLAN/18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md`: timecode konsisten, istilah seragam, detail animasi segmen 1-2. Alasan: sinkron script. Dampak: storyboard siap produksi.
- `01-MASTER-PLAN/20-NASKAH-DETAIL-PER-MENIT.md`: timecode format HH:MM:SS,mmm, istilah seragam. Alasan: sinkron lintas dokumen. Dampak: timeline jelas.
- `01-MASTER-PLAN/26-SRT-LENGKAP-40-MENIT.md`: perbaikan line breaks, konsistensi istilah, notasi a + jb. Alasan: keterbacaan subtitle. Dampak: SRT siap QC.
- `01-MASTER-PLAN/23-ASSET-SHOTLIST-MATEMATIKA-EM-TRANSIEN.md`: tambah kolom Owner/Deadline/Format/Path/Status QC. Alasan: operasional produksi. Dampak: tracking aset lebih jelas.
- `01-MASTER-PLAN/09-PRODUCTION-STATUS-DASHBOARD.md`: update status segmen 1-4. Alasan: prioritas produksi. Dampak: fokus kerja jelas.
- `01-MASTER-PLAN/06-PLATFORM-SETUP-CHECKLIST.md`: tambah validasi SRT, loudness check, export preset. Alasan: QC teknis. Dampak: output konsisten.
- `01-MASTER-PLAN/24-PRODUCTION-READY-PACKAGE.md`: tambah Start Here, role-based steps, DoD sign-off, link QA. Alasan: eksekusi tanpa ambiguity. Dampak: koordinasi tim lebih cepat.
- `01-MASTER-PLAN/05-CORE-001-PRODUCTION-PLAN.md`: seragamkan istilah fase/vektor berputar dan "kuis". Alasan: konsistensi. Dampak: istilah selaras.
- `01-MASTER-PLAN/ANIMATIC-PACK-SEG1-SEG2.md`: dibuat dari dokumen LOCK untuk shot list segmen 1-2. Alasan: kebutuhan animatic. Dampak: shot mapping jelas.
- `01-MASTER-PLAN/00-PEMETAAN-MASALAH-SOLUSI.md`: ganti "quiz/phase" ke "kuis/fase". Alasan: konsistensi istilah. Dampak: CTA selaras.
- `01-MASTER-PLAN/00-DOCUMENT-REFERENCE-INDEX.md`: tambah QA report ke index. Alasan: akses QC. Dampak: navigasi cepat.
- `01-MASTER-PLAN/03-KURIKULUM-IDEAL-S1-TEKNIK-ELEKTRO.md`: ganti "fasor" ke "phasor". Alasan: konsistensi istilah. Dampak: kurikulum selaras.
- `01-MASTER-PLAN/10-OPTION-1-EXECUTION-SUMMARY.md`: ganti "quiz" ke "kuis". Alasan: konsistensi istilah. Dampak: ringkasan selaras.
- `01-MASTER-PLAN/11-OPTION-2-EXPAND-CONTENT-FOUNDATION.md`: ganti "quiz" ke "kuis". Alasan: konsistensi istilah. Dampak: deliverable selaras.
- `01-MASTER-PLAN/19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md`: ganti "phase" ke "fase". Alasan: konsistensi istilah. Dampak: spec selaras.
- `01-MASTER-PLAN/21-UI-SIMULASI-WIREFRAME.md`: ganti "quiz" ke "kuis". Alasan: konsistensi istilah. Dampak: UI copy selaras.
- `01-MASTER-PLAN/27-STORYBOARD-DETAIL-FRAME.md`: ganti "quiz" ke "kuis". Alasan: konsistensi istilah. Dampak: detail frame selaras.
- `01-MASTER-PLAN/simulasi-mvp/MVP-SCOPE.md`: ganti "phase" ke "fase". Alasan: konsistensi istilah. Dampak: spec MVP selaras.
- `02-MODUL-KONTEN/CORE-001-Bilangan-Kompleks-AC.md`: ganti "quiz/rotating vector" ke "kuis/vektor berputar". Alasan: konsistensi istilah. Dampak: modul selaras.
- `03-TEMPLATE/TEMPLATE-QUIZ.md`: ganti "quiz" ke "kuis" pada template. Alasan: konsistensi istilah. Dampak: template selaras.
- `01-MASTER-PLAN/16-MODUL-MATEMATIKA-PONDASI-EM-TRANSIEN.md`: ganti "Quiz" ke "Kuis". Alasan: konsistensi istilah. Dampak: assessment selaras.

## Risiko Tersisa + Mitigasi
- Risiko: Deadline aset segmen 1-2 ketat.  
  Mitigasi: Prioritaskan A-12, A-01, A-03 terlebih dulu.
- Risiko: VO pacing meleset dari 40:00.  
  Mitigasi: Rekam segmen per menit, review durasi tiap segmen.
- Risiko: Simulasi MVP belum stabil.  
  Mitigasi: Siapkan rekaman fallback simulasi.

## Changelog
- 2026-02-06: Membuat QA report dan merangkum keputusan QC lintas dokumen.
- 2026-02-06: Lengkapi daftar perubahan per file. Alasan: transparansi QC. Dampak: audit perubahan lebih jelas.
- 2026-02-06: Update temuan inkonsistensi (phasor/fasor). Alasan: konsistensi istilah. Dampak: keputusan QC lebih lengkap.
- 2026-02-06: Tambah animatic pack ke daftar perubahan. Alasan: kebutuhan animator. Dampak: QC lintas dokumen lebih utuh.
