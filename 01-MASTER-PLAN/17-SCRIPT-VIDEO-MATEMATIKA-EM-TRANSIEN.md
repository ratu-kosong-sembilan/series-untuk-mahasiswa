# SCRIPT VIDEO (LONG-FORM 40:00)
## Modul: CORE-001 Bilangan Kompleks dalam Sistem AC

## Tujuan
Menyediakan naskah lengkap (VO + on-screen) untuk video 40 menit tentang bilangan kompleks, phasor, impedansi, dan faktor daya.

## Ruang Lingkup
Hook, outline, VO beat-by-beat, on-screen text, dan catatan visual untuk seluruh durasi.

## Definisi Selesai (DoD)
- Script mencakup durasi 0:00-40:00.
- Setiap segmen memiliki VO, on-screen text, dan visual note.
- Konsistensi istilah teknis terjaga.

## Checklist
- [x] Hook dan outline lengkap
- [x] VO beat-by-beat tersedia
- [x] On-screen text dan visual note tersedia
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md](./18-STORYBOARD-MATEMATIKA-EM-TRANSIEN.md)
- [20-NASKAH-DETAIL-PER-MENIT.md](./20-NASKAH-DETAIL-PER-MENIT.md)
- [25-VO-SUBTITLE-SRT.md](./25-VO-SUBTITLE-SRT.md)

## Metadata Produksi
- Durasi target: 40:00
- Format: 16:9 (long-form) + 9:16 (short cut)
- Pacing: 120-140 kata/menit

## Outline
1. Hook dan problem framing
2. Prasyarat: sinus, fase, Euler
3. Vektor berputar dan phasor
4. Bilangan kompleks sebagai alat
5. Impedansi R, L, C
6. Faktor daya dan daya kompleks
7. Simulasi dan studi kasus
8. Ringkasan, kuis, CTA

---

## Segmen 1 (00:00:00,000-00:04:00,000) | Hook + Problem Framing
Status: LOCKED (animatic-ready)

**Beat 1 (00:00:00,000-00:00:45,000)**  
VO: "Kenapa angka imajiner bisa menjelaskan listrik yang nyata? Di sistem AC, satu simbol `j` bisa memangkas perhitungan yang panjang menjadi satu langkah."  
On-screen: "Imaginasi yang menyederhanakan listrik nyata"  
Visual: Split screen persamaan time-domain vs phasor. Kamera statis, push-in 5% ke sisi phasor. Transisi: cut.

**Beat 2 (00:00:45,000-00:02:00,000)**  
VO: "Mahasiswa sering hafal Z = R + jX, tapi tidak tahu kenapa ada `j`. Di video ini kita bongkar maknanya, bukan hanya rumusnya."  
On-screen: "Bukan hafal, tapi paham"  
Visual: Rumus Z muncul, highlight `j`. Kamera statis, glow 0.6 s, tahan 1.2 s. Transisi: cut.

**Beat 3 (00:02:00,000-00:03:00,000)**  
VO: "Target kita sederhana: kamu bisa melihat gelombang AC seperti vektor yang berputar. Dari situ, bilangan kompleks jadi bahasa yang natural."  
On-screen: "Gelombang = vektor berputar"  
Visual: Jarum jam berputar membentuk sinus. Kamera top-down ringan, rotasi halus 1 putaran/2 s. Transisi: wipe lembut.

**Beat 4 (00:03:00,000-00:04:00,000)**  
VO: "Kita akan sampai ke impedansi, faktor daya, dan contoh industri. Semua dengan satu alat: phasor."  
On-screen: "Phasor -> Impedansi -> Faktor daya"  
Visual: Roadmap tiga blok. Kamera statis, elemen muncul berurutan 0.4 s. Transisi: slide-in.

---

## Segmen 2 (00:04:00,000-00:08:00,000) | Prasyarat Singkat
Status: LOCKED (animatic-ready)

**Beat 1 (00:04:00,000-00:05:00,000)**  
VO: "Ingat gelombang sinus: amplitudo, frekuensi, dan fase. Fase adalah pergeseran waktu."  
On-screen: "v(t) = Vm sin(omega t + phi)"  
Visual: Sinus dengan parameter muncul. Kamera statis, label muncul satu per satu 0.3 s. Transisi: cut.

**Beat 2 (00:05:00,000-00:06:00,000)**  
VO: "Dua gelombang dengan fase berbeda artinya puncaknya terjadi di waktu yang berbeda."  
On-screen: "delta t <-> delta phi"  
Visual: Dua sinus bergeser. Kamera statis, offset animasi 0.8 s. Transisi: cut.

**Beat 3 (00:06:00,000-00:07:00,000)**  
VO: "Euler bilang: e^(jtheta) = cos theta + j sin theta. Ini jembatan dari sinus ke vektor."  
On-screen: "e^(jtheta) = cos theta + j sin theta"  
Visual: Lingkaran satuan. Kamera statis, draw-on 0.6 s, highlight sudut theta. Transisi: wipe lembut.

**Beat 4 (00:07:00,000-00:08:00,000)**  
VO: "Sumbu horizontal = real, vertikal = imajiner. Ini bukan dunia khayal, ini alat visual."  
On-screen: "Real - Imaginary plane"  
Visual: Grid kompleks. Kamera statis, axis draw 0.5 s, grid fade-in. Transisi: cut.

---

## Segmen 3 (8:00-13:00) | Vektor Berputar & Phasor
**Beat 1 (8:00-9:30)**  
VO: "Bayangkan vektor berputar dengan kecepatan omega. Proyeksinya di sumbu real adalah gelombang sinus."  
On-screen: "Vektor berputar -> sinus"  
Visual: Vektor berputar, proyeksi sinus.

**Beat 2 (9:30-11:00)**  
VO: "Phasor adalah snapshot vektor itu, beserta sudut fasenya."  
On-screen: "Phasor = magnitude + fase"  
Visual: Vektor berhenti pada sudut phi.

**Beat 3 (11:00-12:00)**  
VO: "Menulis sinus dengan phasor berarti kita bekerja di ruang vektor, bukan di waktu."  
On-screen: "Time-domain -> Phasor-domain"  
Visual: Arrow dari grafik waktu ke diagram vektor.

**Beat 4 (12:00-13:00)**  
VO: "Konversi cepat: Vm sin(omega t + phi) -> V angle phi."  
On-screen: "Vm sin(omega t + phi) -> V angle phi"  
Visual: Contoh konversi.

---

## Segmen 4 (13:00-20:00) | Bilangan Kompleks sebagai Alat
**Beat 1 (13:00-14:30)**  
VO: "Bilangan kompleks itu vektor. Penjumlahan = penjumlahan vektor."  
On-screen: "Z1 + Z2 = vector addition"  
Visual: Dua vektor dijumlahkan.

**Beat 2 (14:30-16:00)**  
VO: "Perkalian dengan `j` artinya rotasi 90 derajat. Inilah kenapa induktor dan kapasitor memberi fase."  
On-screen: "j = rotasi 90 deg"  
Visual: Vektor berotasi 90 deg.

**Beat 3 (16:00-18:00)**  
VO: "Dengan kompleks, kita bisa menambah, mengalikan, dan membagi seperti biasa, tapi maknanya tetap geometris."  
On-screen: "Aljabar = Geometri"  
Visual: Operasi kompleks dalam diagram.

**Beat 4 (18:00-20:00)**  
VO: "Jadi `j` bukan angka asing. Ia adalah cara kita menulis rotasi."  
On-screen: "j = rotasi"  
Visual: Ringkasan visual.

---

## Segmen 5 (20:00-27:00) | Impedansi R, L, C
**Beat 1 (20:00-21:30)**  
VO: "Resistor: Z = R, tanpa fase. Arus dan tegangan sefase."  
On-screen: "Z_R = R"  
Visual: V dan I sefase.

**Beat 2 (21:30-23:30)**  
VO: "Induktor: Z = j omega L, tegangan mendahului arus 90 deg."  
On-screen: "Z_L = j omega L"  
Visual: V mendahului I.

**Beat 3 (23:30-25:00)**  
VO: "Kapasitor: Z = 1/(j omega C), arus mendahului tegangan 90 deg."  
On-screen: "Z_C = 1/(j omega C)"  
Visual: I mendahului V.

**Beat 4 (25:00-27:00)**  
VO: "Contoh cepat: R=10 ohm, L=50 mH, f=50 Hz. Gabungkan R dan reaktansi jadi a + jb, lalu hitung arus."  
On-screen: "Z = a + jb"  
Visual: Step-by-step hitung Z, tampilkan bentuk a + jb.

---

## Segmen 6 (27:00-32:00) | Faktor Daya & Daya Kompleks
**Beat 1 (27:00-28:30)**  
VO: "Daya kompleks: S = P + jQ. P adalah daya aktif, Q daya reaktif."  
On-screen: "S = P + jQ"  
Visual: Segitiga daya.

**Beat 2 (28:30-30:00)**  
VO: "Faktor daya = cos phi. Semakin besar phi, semakin banyak daya reaktif."  
On-screen: "pf = cos phi"  
Visual: Sudut phi pada segitiga daya.

**Beat 3 (30:00-32:00)**  
VO: "Di industri, faktor daya rendah berarti denda. Karena arus tinggi tanpa menghasilkan kerja."  
On-screen: "PF rendah = denda"  
Visual: Tagihan listrik + kapasitor bank.

---

## Segmen 7 (32:00-36:00) | Simulasi & Studi Kasus
**Beat 1 (32:00-33:30)**  
VO: "Di simulasi, geser R, L, C dan lihat vektor phasor bergeser."  
On-screen: "Coba ubah R, L, C"  
Visual: UI simulasi dengan slider.

**Beat 2 (33:30-35:00)**  
VO: "Naikkan frekuensi, induktif makin besar, kapasitif makin kecil."  
On-screen: "Z_L naik, Z_C turun saat f naik"  
Visual: Grafik impedansi vs frekuensi.

**Beat 3 (35:00-36:00)**  
VO: "Studi kasus: motor induksi 5 kW, PF 0.7. Tambah kapasitor untuk naik ke 0.95."  
On-screen: "PF correction case"  
Visual: Sebelum-sesudah segitiga daya.

---

## Segmen 8 (36:00-40:00) | Ringkasan + Kuis + CTA
**Beat 1 (36:00-38:00)**  
VO: "Intinya: sinus bisa dilihat sebagai vektor berputar. Bilangan kompleks adalah cara kita menulis rotasi dan fase."  
On-screen: "Sinus = vektor berputar"  
Visual: Ringkasan 3 poin.

**Beat 2 (38:00-39:30)**  
VO: "Kuis singkat: 1) Apa arti `j`? 2) Mengapa Z_L punya fase +90 deg? 3) Apa itu faktor daya?"  
On-screen: "Kuis cepat"  
Visual: Kartu soal muncul.

**Beat 3 (39:30-40:00)**  
VO: "Coba simulasi interaktif dan kerjakan bank soal. Itu cara tercepat bikin konsep ini nempel."  
On-screen: "Coba simulasi + kuis"  
Visual: CTA screen.

## Changelog
- 2026-02-06: Menulis ulang naskah lengkap CORE-001 dengan timecode dan beat-by-beat.
- 2026-02-06: Lock segmen 1-2 dengan timecode HH:MM:SS,mmm, detail kamera/transisi, dan istilah konsisten (phasor, fase, omega, phi). Alasan: siap animatic dan QC sinkron. Dampak: segmen 1-2 animatic-ready dan konsisten dengan storyboard/SRT.
- 2026-02-06: Ganti "quiz" menjadi "kuis" pada segmen 8. Alasan: konsistensi istilah Indonesia. Dampak: CTA dan SRT selaras.
- 2026-02-06: Ubah on-screen "Rotating vector" menjadi "Vektor berputar". Alasan: konsistensi istilah Indonesia. Dampak: on-screen selaras dengan modul dan storyboard.
- 2026-02-06: Tambah notasi "a + jb" pada contoh impedansi. Alasan: konsistensi notasi kompleks dengan SRT. Dampak: VO dan on-screen selaras.
