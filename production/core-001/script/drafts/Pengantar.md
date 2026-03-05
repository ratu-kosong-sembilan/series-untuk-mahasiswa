# Hari-1

## Draft Voiceover Segment 1 (PRE-MODULE & HOOK, ±3 menit)

[0:00–0:20]
[VISUAL: Split screen, kiri papan penuh rumus, kanan satu baris phasor]
NARASI:
“Bayangkan Anda harus menjumlahkan dua gelombang sinus dengan fase berbeda.”

[0:20–1:05]
[VISUAL: Kiri langkah trig singkat, kanan 1 baris phasor]
“Di sisi trig, kita perlu identitas:
sin(a+b) = sin a cos b + cos a sin b.
Itu asal munculnya cos45° dan sin45°.
Karena a = ωt, b = 45°.
Jadi sin(ωt+45°) = sin(ωt)·cos45° + cos(ωt)·sin45°.
Baru setelah itu kita gabungkan suku.
Di sisi phasor: satu baris operasi, selesai.”

[1:05–1:50]
[VISUAL: Montage industri: generator, relay, power analyzer, 3-phase]
“Pertanyaan klasik yang hampir semua mahasiswa tanya:
‘Kenapa harus bilangan kompleks?’
Jawaban singkatnya: bukan karena keren.
Tapi karena ini satu-satunya cara efisien untuk sistem nyata.”

[1:50–2:25]
[VISUAL: Daftar kuliah & industri]
“Di kuliah, Anda akan menemukannya di Rangkaian AC, Sistem Tenaga, Mesin Listrik, Proteksi, Elektronika Daya.
Di industri, semua analisis memakai phasor: load flow, relay proteksi, power quality.
Jadi bukan soal nilai ujian—ini bahasa kerja engineer.”

[2:25–2:40]
[VISUAL: Statistik teks]
“Masalahnya:
Banyak mahasiswa bisa menghitung bilangan kompleks, tapi tidak paham kenapa harus kompleks.
Akibatnya: hafal rumus, tapi kosong makna.”

[2:40–3:00]
[VISUAL: Title card “Kenapa Ada Bilangan Kompleks di AC?”]
“Hari ini kita bereskan itu.
Kita mulai dari fenomena—kenapa trigonometri tidak cukup untuk sistem AC.”

## Draft Voiceover Segment 2 (FENOMENA FISIK, ±6 menit)

[8:00–8:40]
[VISUAL: Osiloskop 3 fasa, tiga gelombang berbeda fase]
NARASI:
“Sekarang kita masuk ke fenomena yang membuat trigonometri jadi mimpi buruk: sistem 3 fasa.
Tiga gelombang sinus, beda fase 120 derajat.”

[8:40–9:40]
[VISUAL: Tulis persamaan v_R, v_S, v_T]
“Secara matematis:
- v_R = 100 sin(ωt)
- v_S = 100 sin(ωt - 120°)
- v_T = 100 sin(ωt - 240°)

Pertanyaannya sederhana:
Berapa total tegangan di titik tertentu?”

[9:40–10:20]
[VISUAL: Langkah trig manual muncul bertahap]
“Dengan trigonometri manual, Anda harus:
1) Ekspansi sin(ωt - 120°)
2) Substitusi cos dan sin 120°
3) Ulangi untuk sin(ωt - 240°)
4) Gabungkan semuanya

Empat sampai lima langkah—untuk hanya tiga gelombang.”

[10:20–11:00]
[VISUAL: Stopwatch berjalan, angka menit]
“Sekarang bayangkan kalau bukan 3, tapi 10 atau 100 beban.
Waktu habis di aljabar, bukan di analisis.”

[11:00–12:00]
[VISUAL: Perbandingan kiri = trig, kanan = phasor]
“Di sini bilangan kompleks masuk.
Dengan phasor:
V_total = V_R + V_S + V_T
Selesai. Satu baris.”

[12:00–12:40]
[VISUAL: Case industri, load flow 100 bus]
“Contoh nyata:
Load flow 100 bus.
Kalau pakai trig manual: ribuan langkah.
Kalau pakai kompleks: 300 persamaan sederhana.
Hasilnya: cepat, rapi, dan bisa diotomasi komputer.”

[12:40–13:20]
[VISUAL: Talking head, close-up]
“Jadi ini bukan soal ‘mahasiswa pintar pakai kompleks’.
Ini soal sistem nyata yang hanya bisa dihitung dengan cara efisien.”

[13:20–14:00]
[VISUAL: Transition ke visualisasi vektor berputar]
“Sekarang Anda sudah melihat masalahnya.
Tahap berikutnya: visualisasi—mengapa sinus bisa direpresentasikan sebagai vektor berputar.
Mari kita lanjut.”

## Draft Voiceover Segment 3 (VISUALISASI, ±9 menit)

[14:00–14:50]
[VISUAL: Satu gelombang sinus muncul, lalu vektor berputar]
NARASI:
“Setiap gelombang sinus yang Anda lihat di osiloskop sebenarnya adalah proyeksi.
Proyeksi dari sebuah vektor yang berputar dengan kecepatan konstan.”

[14:50–15:40]
[VISUAL: Vektor berputar, proyeksi ke sumbu Y membentuk sinus]
“Ketika vektor itu berputar, proyeksinya ke sumbu vertikal membentuk gelombang sinus.
Jadi gelombang bukan sesuatu yang berdiri sendiri.
Ia adalah bayangan dari gerak rotasi.”

[15:40–16:50]
[VISUAL: Dua vektor berbeda panjang dan fase]
“Sekarang bayangkan ada dua vektor:
V1 dengan magnitude 100 pada fase 0 derajat,
V2 dengan magnitude 80 pada fase 45 derajat.
Keduanya berputar dengan kecepatan yang sama.”

[16:50–17:40]
[VISUAL: Penjumlahan vektor tip-to-tail]
“Penjumlahan dua gelombang berarti penjumlahan dua vektor.
Dan penjumlahan vektor adalah operasi sederhana: tip-to-tail.
Hasilnya satu vektor baru dengan magnitude dan fase yang baru.”

[17:40–18:30]
[VISUAL: Proyeksi vektor total menjadi gelombang sinus baru]
“Proyeksi vektor total itulah gelombang hasil penjumlahan.
Jadi seluruh persoalan yang rumit di trigonometri
sebenarnya hanya penjumlahan vektor.”

[18:30–19:55]
[VISUAL: Koordinat kartesius berubah jadi complex plane]
“Di sini bilangan kompleks menjadi bahasa resmi untuk vektor.
Sumbu horizontal adalah bagian real.
Sumbu vertikal adalah bagian imajiner—atau lebih tepatnya, komponen yang berjarak 90 derajat.”

[19:55–20:45]
[VISUAL: Tampilkan bentuk rectangular, polar, dan Euler]
“Vektor yang sama bisa ditulis dalam tiga bentuk:
- Rectangular: Z = a + jb
- Polar: Z = R ∠ θ
- Euler: Z = R e^(jθ)

Tiga cara, satu makna.”

[20:45–21:35]
[VISUAL: Highlight ‘j = rotasi 90°’]
“Perhatikan ini baik-baik:
‘j’ bukan sekadar simbol imajiner.
Di domain AC, j berarti rotasi 90 derajat.
Itu sebabnya komponen imajiner selalu tegak lurus dari komponen real.”

[21:35–22:25]
[VISUAL: Ringkasan perbandingan trig vs vektor]
“Jadi kenapa bilangan kompleks lebih cepat?
Karena Anda mengubah problem gelombang menjadi problem vektor.
Dan vektor dijumlahkan dengan satu operasi.”

[22:25–23:00]
[VISUAL: Transition ke makna fisis]
“Sekarang kita sudah paham representasinya.
Tahap berikutnya: makna fisis.
Apa arti real dan imajiner dalam dunia nyata?”

## Draft Voiceover Segment 4 (MAKNA FISIS, ±9 menit)

[23:00–23:55]
[VISUAL: Complex plane dengan label R dan jX]
NARASI:
“Kata ‘imajiner’ sering membuat orang salah paham.
Padahal di sistem AC, imajiner bukan berarti tidak nyata.
Ini hanya komponen yang posisinya 90 derajat dari sumbu real.”

[23:55–24:50]
[VISUAL: Diagram impedansi Z = R + jX]
“Dalam impedansi:
- R adalah resistansi: bagian yang membuang energi.
- jX adalah reaktansi: bagian yang menyimpan dan mengembalikan energi.
Keduanya nyata, hanya berbeda dimensi.”

[24:50–26:00]
[VISUAL: Animasi rotasi 90° berulang]
“Sekarang inti paling penting: j itu operator rotasi.
Kalikan suatu vektor dengan j, maka vektornya berputar 90 derajat.
Itulah sebabnya:
- Induktor memberi +90°
- Kapasitor memberi -90°”

[26:00–27:10]
[VISUAL: Resistor, Induktor, Kapasitor dengan fase V dan I]
“Resistor: V dan I sefasa → Z = R
Induktor: V memimpin I 90° → Z = jωL
Kapasitor: I memimpin V 90° → Z = -j/(ωC)

Semua fase ini adalah fenomena fisik, bukan imajinasi.”

[27:10–28:25]
[VISUAL: Segitiga impedansi dan bentuk polar]
“Bilangan kompleks bisa dibaca dua cara:
- Rectangular: Z = R + jX
- Polar: Z = |Z| ∠ θ

Magnitude menunjukkan seberapa besar oposisi total.
Sudut menunjukkan hubungan waktu antara V dan I.”

[28:25–29:20]
[VISUAL: Power triangle, S = P + jQ]
“Hal yang sama berlaku di daya:
S = P + jQ
P = daya nyata (Watt)
Q = daya reaktif (VAR)
S = daya semu (VA)

Kita bisa melihat efisiensi sistem hanya dengan membaca sudutnya.”

[29:20–30:10]
[VISUAL: Example angka power factor sederhana]
“Contoh sederhana:
Jika faktor daya 0.6, berarti sudutnya sekitar 53°.
Itu menunjukkan banyak energi bolak-balik yang tidak berubah jadi kerja nyata.
Dengan kapasitor, sudut ini bisa diperkecil.”

[30:10–30:50]
[VISUAL: Recap poin makna fisis]
“Ringkasnya:
- Real part → dissipasi energi
- Imaginary part → penyimpanan energi
- Magnitude → besar total
- Phase → timing antar gelombang

Semua ini adalah bahasa fisik, bukan abstraksi.”

[30:50–32:00]
[VISUAL: Transition ke model matematis]
“Sekarang maknanya sudah jelas.
Selanjutnya: bagaimana rumusnya diturunkan dari fisika dasar.”

## Draft Voiceover Segment 5 (MODEL MATEMATIS, ±8 menit)

[32:00–32:40]
[VISUAL: Rangkaian RLC seri sederhana]
NARASI:
“Sekarang kita turunkan rumusnya secara sistematis.
Bukan hafalan, tapi dari hukum fisika dasar.”

[32:40–33:35]
[VISUAL: Resistor dengan V dan I sefasa]
“Pertama, resistor:
Hukum Ohm: v(t) = R i(t)
Dalam domain phasor:
V = R I → Z_R = R
Tidak ada pergeseran fase.”

[33:35–34:45]
[VISUAL: Induktor, turunan i(t)]
“Induktor:
v(t) = L di/dt
Jika i(t) = I_m sin(ωt), maka v(t) bergeser 90° di depan arus.
Dalam phasor:
Z_L = jωL
Artinya: impedansi induktor murni rotasi +90°.”

[34:45–36:00]
[VISUAL: Kapasitor, integral arus]
“Kapasitor:
i(t) = C dv/dt
Jika i(t) sinus, maka v(t) tertinggal 90°.
Dalam phasor:
Z_C = -j/(ωC)
Artinya: impedansi kapasitor murni rotasi -90°.”

[36:00–36:55]
[VISUAL: RLC seri dijumlahkan]
“Gabungkan semuanya:
Z_total = Z_R + Z_L + Z_C
= R + j(ωL - 1/(ωC))

Bagian real = R
Bagian imajiner = X = ωL - 1/(ωC)”

[36:55–37:50]
[VISUAL: Konversi rectangular ke polar]
“Dari sini kita bisa hitung:
|Z| = √(R² + X²)
θ = arctan(X/R)

Magnitude menentukan besarnya arus,
sudut menentukan siapa yang memimpin: V atau I.”

[37:50–38:45]
[VISUAL: Contoh numerik sederhana]
“Contoh cepat:
R = 10 O, L = 0.05 H, C = 100 µF, f = 50 Hz.
Hitung X_L, X_C, dan X.
Jika X negatif → sistem kapasitif → arus memimpin.
Jika X positif → sistem induktif → arus tertinggal.”

[38:45–39:25]
[VISUAL: Cheatsheet rumus]
“Ringkasannya:
Z_R = R
Z_L = jωL
Z_C = -j/(ωC)
Z_total = R + jX

Ini bukan sekadar rumus.
Ini cara membaca perilaku fisik rangkaian.”

[39:25–40:00]
[VISUAL: Transition ke simulasi]
“Sekarang kita uji semua rumus ini lewat simulasi.
Kita ubah parameter dan lihat apa yang benar-benar terjadi.”

## Draft Voiceover Segment 6 (SIMULASI & APLIKASI, ±15 menit)

[40:00–40:25]
[VISUAL: Transition ke simulator interaktif]
NARASI:
“Sekarang kita uji pemahaman lewat simulasi.
Bukan lagi angka di kertas, tapi perilaku nyata.”

[40:25–41:35]
[VISUAL: Simulator RLC dengan slider]
“Ini simulator RLC.
Ada slider untuk frekuensi, kapasitansi, induktansi, dan resistansi.
Lihat phasor dan gelombang berubah secara real-time.

Kita mulai dari frekuensi 50 Hz.”

[41:35–42:45]
[VISUAL: Slider frekuensi naik, phasor bergerak]
“Naikkan frekuensi.
Perhatikan: X_L naik, X_C turun.
Phasor arus bergeser.
Ini persis yang diprediksi rumus X = ωL - 1/(ωC).”

[42:45–43:55]
[VISUAL: Cari resonansi, sudut jadi 0°]
“Sekarang cari titik resonansi.
Atur sampai sudut fase 0 derajat.
Di titik ini: X_L = X_C, sehingga Z hanya R.
Arus maksimum, fase sefasa.”

[43:55–45:05]
[VISUAL: Slider C diubah]
“Ubah kapasitansi.
C makin besar → X_C makin kecil → sistem makin kapasitif.
Arus jadi lebih ‘leading’.”

[45:05–46:15]
[VISUAL: Slider R diubah]
“Ubah resistansi.
R makin besar → magnitude arus turun.
Tapi sudut fase tetap ditentukan rasio X/R.”

[46:15–47:05]
[VISUAL: Recap simulasi]
“Simulasi ini membuktikan:
Bilangan kompleks bukan teori abstrak.
Ia benar-benar menggambarkan perilaku sistem.”

[47:05–49:05]
[VISUAL: Studi kasus pabrik motor induksi]
“Sekarang studi kasus nyata.
Sebuah pabrik punya banyak motor induksi.
Faktor dayanya 0.6.
Tagihan listrik naik karena penalty.”

[49:05–50:15]
[VISUAL: Power triangle dan perhitungan Q]
“Jika daya nyata 50 kW:
S = 50 / 0.6 = 83.3 kVA
Q = √(S² - P²) = 66.7 kVAR
Artinya banyak energi bolak-balik yang tidak jadi kerja nyata.”

[50:15–51:50]
[VISUAL: Tambahkan kapasitor bank]
“Kita tambahkan kapasitor untuk koreksi faktor daya.
Target PF 0.95.
Q baru sekitar 16.5 kVAR.
Jadi kapasitor harus mengkompensasi sekitar 50 kVAR.”

[51:50–53:00]
[VISUAL: Before-after phasor]
“Hasilnya:
- Arus turun
- Rugi-rugi I²R turun
- Tagihan listrik berkurang
Semua keputusan desain ini dibuat dengan bilangan kompleks.”

[53:00–53:50]
[VISUAL: Rekap 6 tahap]
“Mari kita rangkum perjalanan hari ini:
1) Fenomena: trigonometri tidak praktis
2) Visualisasi: sinus = proyeksi vektor berputar
3) Makna fisis: real & imajiner = dua dimensi nyata
4) Model matematis: rumus diturunkan dari fisika
5) Simulasi: verifikasi perilaku
6) Aplikasi: kasus industri nyata”

[53:50–54:35]
[VISUAL: Closing, talking head]
“Sekarang Anda tidak lagi sekadar bisa menghitung.
Anda memahami bahasa kerja engineer.
Dan itu yang membedakan antara hafal dan paham.”

[54:35–55:00]
[VISUAL: CTA + teaser modul berikutnya]
“Di modul berikutnya kita masuk ke sinyal dan sistem.
Dengan fondasi ini, semuanya akan jauh lebih masuk akal.
Terima kasih sudah mengikuti sampai akhir.
Sampai jumpa di episode berikutnya.”





