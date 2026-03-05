# STORYBOARD VISUAL CORE-001

## Tujuan
Menyediakan storyboard per scene untuk video CORE-001 dengan detail visual, animasi, dan audio cue.

## Ruang Lingkup
Semua segmen 0:00-40:00 sesuai naskah.

## Definisi Selesai (DoD)
- Storyboard per segmen tersedia.
- Setiap scene memiliki visual, animasi, dan cue audio.

## Checklist
- [x] Storyboard per segmen lengkap
- [x] Sinkron dengan script
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md](./17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md)
- [27-STORYBOARD-DETAIL-FRAME.md](./27-STORYBOARD-DETAIL-FRAME.md)

## Storyboard Per Scene
| Time | Scene | Visual | Animasi | Audio Cue |
| --- | --- | --- | --- | --- |
| 00:00:00,000-00:00:45,000 | Hook | Split screen persamaan panjang vs phasor sederhana | Kamera statis, push-in 5% ke sisi phasor | Musik tegang, drop pada "j" |
| 00:00:45,000-00:02:00,000 | Problem | Rumus Z muncul, highlight `j` | Glow 0.6 s, tahan 1.2 s, transisi cut | VO menekankan "bukan hafal" |
| 00:02:00,000-00:03:00,000 | Target | Jarum jam berputar -> sinus | Rotasi halus, transisi wipe | FX soft |
| 00:03:00,000-00:04:00,000 | Roadmap | 3 blok: Phasor, Impedansi, Faktor daya | Slide in bertahap 0.4 s | VO roadmap |
| 00:04:00,000-00:05:00,000 | Sinus | Grafik sinus dengan label | Label muncul satu per satu | VO formula |
| 00:05:00,000-00:06:00,000 | Pergeseran fase | Dua sinus bergeser | Offset animasi 0.8 s | VO delta t vs delta phi |
| 00:06:00,000-00:07:00,000 | Euler | Lingkaran satuan + e^(jtheta) | Draw circle 0.6 s, highlight theta | VO Euler |
| 00:07:00,000-00:08:00,000 | Bidang kompleks | Grid kompleks | Axis draw 0.5 s, grid fade-in | VO sumbu real/imag |
| 00:08:00,000-00:09:30,000 | Vektor berputar | Vektor berputar | Rotate loop | VO proyeksi |
| 00:09:30,000-00:11:00,000 | Snapshot phasor | Vektor berhenti pada phi | Freeze + label | VO phasor |
| 00:11:00,000-00:12:00,000 | Perpindahan domain | Panah waktu -> phasor | Morph | VO konversi |
| 00:12:00,000-00:13:00,000 | Contoh | Vm sin -> V angle phi | Text transform | VO konversi |
| 00:13:00,000-00:14:30,000 | Penjumlahan vektor | Dua vektor + resultant | Parallelogram | VO penjumlahan |
| 00:14:30,000-00:16:00,000 | Rotasi j | Vektor rotasi 90 deg | Rotate 90 deg | VO makna j |
| 00:16:00,000-00:18:00,000 | Aljabar | Operasi kompleks | Step overlay | VO aljabar |
| 00:18:00,000-00:20:00,000 | Ringkasan | 3 poin: rotasi, fase, alat | Bullet appear | VO ringkasan |
| 00:20:00,000-00:21:30,000 | Resistor | V dan I sefase | Overlay V/I | VO Z_R |
| 00:21:30,000-00:23:30,000 | Induktor | V mendahului I | Lead fase | VO Z_L |
| 00:23:30,000-00:25:00,000 | Kapasitor | I mendahului V | Lead fase | VO Z_C |
| 00:25:00,000-00:27:00,000 | Contoh | Hitung Z, I; tampilkan Z = a + jb | Step-by-step | VO contoh |
| 00:27:00,000-00:28:30,000 | Daya kompleks | Segitiga daya | Draw triangle | VO S=P+jQ |
| 00:28:30,000-00:30:00,000 | Faktor daya | cos phi ditampilkan | Highlight phi | VO pf |
| 00:30:00,000-00:32:00,000 | Industri | Tagihan & kapasitor | Slide in | VO denda |
| 00:32:00,000-00:33:30,000 | Simulasi UI | Slider R, L, C | Pointer move | VO instruksi |
| 00:33:30,000-00:35:00,000 | Frekuensi | Grafik Z vs f | Curve animate | VO efek f |
| 00:35:00,000-00:36:00,000 | Studi kasus | Motor koreksi faktor daya | Before/after | VO case |
| 00:36:00,000-00:38:00,000 | Ringkasan | 3 poin utama | Cards | VO ringkas |
| 00:38:00,000-00:39:30,000 | Kuis | 3 kartu soal | Flip cards | VO kuis |
| 00:39:30,000-00:40:00,000 | CTA | Link simulasi + kuis | CTA screen | VO penutup |

## Changelog
- 2026-02-06: Menyusun storyboard CORE-001 per scene.
- 2026-02-06: Lock segmen 1-2 dengan timecode HH:MM:SS,mmm dan detail kamera/transisi; samakan istilah (phasor, fase). Alasan: sinkron dengan script/SRT. Dampak: storyboard siap animatic segmen 1-2 dan konsisten lintas dokumen.
- 2026-02-06: Ubah istilah "quiz" menjadi "kuis". Alasan: konsistensi istilah. Dampak: audio cue selaras dengan SRT.
- 2026-02-06: Tambah visual notasi "a + jb" pada contoh impedansi. Alasan: konsistensi notasi kompleks. Dampak: storyboard selaras dengan VO/SRT.
