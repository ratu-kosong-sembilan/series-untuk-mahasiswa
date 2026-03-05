# Teleprompter Cue Sheet — CORE-001 (55:00)

Format: timecode — line — cue notes
Tone: Enthusiastic → serious → explanatory → systematic → practical

---
## Segment 1 — PRE-MODULE & HOOK (09:00)
00:00 Hook: "Bayangkan menjumlahkan dua gelombang sinus beda fase." [energy]
00:07 "Trigonometri manual: 5 langkah, 10 menit, rawan error." [contrast]
00:15 "Bilangan kompleks: satu operasi, 10 detik." [highlight]
00:22 "Hasilnya sama. Bedanya? Cara kerja." [pause 1s]
00:28 "Pertanyaan: Kenapa harus bilangan KOMPLEKS?" [lean in]
00:34 "Jawaban: ini SATU-SATUNYA cara efisien." [firm]
00:40 "Mari lihat kenapa." [transition]

00:45 Konteks: "Di kuliah: Rangkaian AC, Sistem Tenaga, Mesin Listrik..." [list]
01:05 "Di industri: load flow, relay proteksi, power quality." [clip]
01:20 "Di pekerjaan: power engineer hampir setiap hari." [matter-of-fact]
01:30 "Masalah: 70% bisa hitung, 80% tidak paham KENAPA." [emphasis]
01:45 "Itu bedanya hafal vs mengerti. Hari ini kita selesaikan." [resolve]

02:30 Roadmap: "6 tahap: Fenomena, Visualisasi, Makna, Model, Simulasi, Industri." [pace steady]
03:00 "Setiap tahap = pemahaman lebih dalam. Bukan hafal rumus." [assure]
03:20 "Kita butuh 55 menit. Worth it? Absolutely." [smile]

06:00 Key msg: "Jika Anda pernah bertanya: kenapa pakai j kalau sistem nyata?" [callout]
06:20 "Apa bedanya Laplace vs manual? Kenapa power factor penting?" [enumerate]
06:40 "Jawabannya mulai dari sini: memahami bilangan kompleks." [anchor]
07:00 "Setelah ini: Anda nyaman, bisa jelaskan, tidak takut lagi." [promise]
08:30 "Mari mulai." [close segment]

---
## Segment 2 — FENOMENA FISIK (07:00)
09:00 "Di sistem 3-fasa ada 3 gelombang, beda 120°." [setup]
09:15 "Pertanyaan simpel: berapa total tegangan di titik ini?" [pose]
09:30 "Coba cara manual..." [cue trig steps]
10:10 "v_total = 100 sin(ωt) + ... → 7-10 menit kerja." [slog]
10:25 "Kalau ada 10 beban? IMPOSSIBLE." [stress]

10:30 "Sekarang lihat perbandingan nyata." [transition]
10:40 "Load flow 100 bus: trigonometri = 1500-3000 langkah, beberapa hari." [slow]
11:05 "Phasor kompleks: 300 operasi sederhana, 10 menit dengan komputer." [clarity]
11:25 "KESIMPULAN: trigonometri manual tidak praktis." [declare]
11:40 "Phasor kompleks = SATU-SATUNYA cara feasible." [underscore]

14:30 "Jadi pertanyaannya bukan 'kenapa kompleks?'" [hook]
14:40 "Tapi: bagaimana mungkin kita tidak pakai kompleks?" [drive]
14:55 "Mari ke VISUALISASI." [transition]

---
## Segment 3 — VISUALISASI (11:00)
16:00 "Setiap gelombang sinus punya asal: vektor berputar." [state]
16:15 "Saat vektor berputar, proyeksinya = gelombang sinus." [link]
16:35 "Setiap titik di sinus = snapshot posisi vektor." [highlight]

18:00 Animation 1 intro: "Lihat vektor V₁ merah, V₂ biru, berputar sama ω." [guide]
18:30 "Proyeksi ke sumbu Y → gelombang sinus." [point]
19:00 "Tambah vektor = tambah gelombang." [bridge]
20:30 "Resultan hijau: magnitude & fase baru langsung terbaca." [show]
21:30 "Penjumlahan vektor jauh lebih mudah dari trig." [conclude]

22:00 Animation 2 intro: "Vektor di polar: R, θ. Proyeksi: R cosθ, R sinθ." [teach]
22:40 "X-axis jadi Real; Y-axis jadi Imag (×j)." [label]
23:00 "Z = R cosθ + j R sinθ." [state]
23:30 "Dalam Euler: Z = R e^(jθ)." [flash]
24:30 "Satu vektor, empat representasi: visual, rectangular, polar, Euler." [compare]
25:30 "Operasi kompleks = operasi vektor = operasi gelombang." [punch]

26:30 "Trigonometri: 5 langkah. Vector addition: 1 langkah." [contrast]
26:50 "Complex algebra adalah alat vector addition." [cap]
26:55 "Itu kenapa jauh lebih cepat." [segue]

---
## Segment 4 — MAKNA FISIS (11:00)
27:00 "'Imajiner' bukan berarti tidak nyata." [clarify]
27:20 "Real part: resistif. Imag part: reaktif. Dua-duanya fisik." [stress]
27:45 "j = operator rotasi 90°." [bold]

29:00 "Kalikan j empat kali: 0°, 90°, 180°, 270°, balik 360°." [rhythm]
29:30 "Induktor: V leads I 90° → jωL." [example]
29:50 "Kapasitor: I leads V 90° → -j/(ωC)." [example]

32:00 "Rectangular vs polar: kapan dipakai?" [ask]
32:15 "Rectangular untuk tambah/kurang; Polar untuk interpretasi magnitude/phase." [answer]
33:00 "Contoh: Z = 5 + j12 = 13∠67.4°." [state]
33:20 "Magnitude: oposisi total. Phase: timing V vs I." [interpret]

35:00 "Power triangle: S = P + jQ." [introduce]
35:20 "P nyata, Q bolak-balik, S gabungan." [explain]
36:00 "PF = cosφ; contoh motor 10 kW PF 0.6 → Q 13.33 kVAR." [numbers]
36:40 "Tambah kapasitor untuk PF correction." [lead]

37:30 "Rangkuman: Real dissipasi, Imag storage, Magnitude besarnya, Phase timing." [recap]
37:50 "Semua bisa diukur, semua ada makna fisik." [anchor]

---
## Segment 5 — MODEL MATEMATIS (10:00)
38:00 "Gunakan Ohm, KVL, Faraday. Asumsi: steady-state, linear, single frequency." [setup]
38:30 "Resistor: v = R i → Z_R = R, sefasa." [clean]
40:30 "Induktor: v = L di/dt → V leads I 90° → Z_L = jωL." [stress 90°]
42:30 "Kapasitor: i = C dv/dt → I leads V 90° → Z_C = -j/(ωC)." [stress -90°]
44:30 "RLC series: Z = R + j(ωL − 1/ωC)." [state]
45:00 "X > 0 induktif, X < 0 kapasitif, X = 0 resonansi." [interpret]
46:00 "Contoh: R=10, L=50mH, C=100µF, f=50 Hz → Z = 10 − j16.12 = 18.97∠-58.1°." [numbers]
47:00 "I = 11.6∠58.1° A; PF = cos(58.1°) ≈ 0.53 leading." [interpret]
48:30 "Cheatsheet: Z_R, Z_L, Z_C, |Z|, ∠Z." [wrap]

---
## Segment 6 — SIMULASI & APLIKASI (17:00)
49:30 "Sekarang eksperimen dengan simulator." [invite]
50:00 "Slider frekuensi: X_L naik, X_C turun; phasor bergerak." [describe]
51:00 "Cari resonansi: X_L = X_C, impedansi minimum, phase 0°." [callout]
52:00 "Set ke 71.2 Hz: lihat |Z| minimum, I maksimum." [observe]
53:00 "Ubah C: sistem makin kapasitif; prinsip PF correction." [link]
54:00 "Ubah R: |Z| naik, sudut tetap ditentukan X/R." [note]
55:00 "Rangkuman: parameter → phasor → perilaku sistem." [tie]

55:10 Case study PF correction:
55:20 "Motor 50 kW PF 0.6: S = 83.3 kVA, Q = 66.7 kVAR." [state]
55:50 "Target PF 0.95: Q_new = 16.5 kVAR; butuh 50.2 kVAR kapasitor." [compute]
56:20 "C ≈ 1000 µF @ 400 V, 50 Hz." [give]
56:40 "Sebelum: 50 + j66.7. Sesudah: 50 + j16.5. PF naik, losses turun." [impact]

57:00 Wrap:
57:05 "Recap 6 tahap: Fenomena, Visual, Makna, Model, Simulasi, Industri." [enumerate]
57:30 "Bilangan kompleks = bahasa efisien untuk sistem AC." [assert]
57:50 "Anda bisa jelaskan, visualisasikan, derive, dan aplikasikan." [affirm]
58:10 "Download cheatsheet; lanjut ke quiz & project." [CTA]
58:40 "See you di modul berikutnya." [warm close]

---
## Delivery Notes
- Micro-pauses before key numbers/equations; keep diction clear.
- Read rectangular and polar values explicitly when on screen.
- Reinforce 90° lead/lag verbally in Segment 4/5.
- Keep pace steady; avoid rushing during calculations.
