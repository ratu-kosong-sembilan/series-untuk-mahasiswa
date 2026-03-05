# BANK SOAL CORE-001 (20 SOAL)

## Tujuan
Menyediakan bank soal bertingkat untuk menguji pemahaman bilangan kompleks, phasor, impedansi, dan faktor daya.

## Ruang Lingkup
20 soal dengan jawaban dan pembahasan untuk CORE-001.

## Definisi Selesai (DoD)
- Minimal 20 soal tersedia.
- Setiap soal punya jawaban dan pembahasan singkat.

## Checklist
- [x] 20 soal lengkap
- [x] Jawaban dan pembahasan tersedia
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md](./17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md)
- [20-NASKAH-DETAIL-PER-MENIT.md](./20-NASKAH-DETAIL-PER-MENIT.md)

## Level 1 (Konsep Dasar)
1) Apa arti simbol `j` pada bilangan kompleks di teknik listrik?
- A. Angka acak
- B. Akar dari -1 dan rotasi 90 derajat
- C. Satuan arus
- D. Satuan tegangan
Jawaban: B
Pembahasan: `j` merepresentasikan sqrt(-1) dan secara geometris berarti rotasi 90 derajat.

2) Phasor dari v(t) = 10 sin(omega t + 30 deg) adalah?
- A. 10 angle 0
- B. 10 angle 30
- C. 10 angle -30
- D. 30 angle 10
Jawaban: B
Pembahasan: Magnitude 10 dan fase +30 derajat.

3) Pada induktor, hubungan fase arus terhadap tegangan adalah?
- A. Arus mendahului 90 deg
- B. Arus tertinggal 90 deg
- C. Arus sefase
- D. Arus tertinggal 180 deg
Jawaban: B
Pembahasan: Pada induktor, tegangan mendahului arus 90 derajat.

4) Pada kapasitor, arus terhadap tegangan adalah?
- A. Arus mendahului 90 deg
- B. Arus tertinggal 90 deg
- C. Arus sefase
- D. Arus tertinggal 180 deg
Jawaban: A
Pembahasan: Pada kapasitor, arus mendahului tegangan 90 derajat.

5) Impedansi resistor murni berada di?
- A. Sumbu imajiner
- B. Sumbu real
- C. Kuadran II
- D. Kuadran IV
Jawaban: B
Pembahasan: Resistor murni memiliki komponen real saja.

6) Faktor daya didefinisikan sebagai?
- A. sin phi
- B. cos phi
- C. tan phi
- D. 1/cos phi
Jawaban: B
Pembahasan: Faktor daya = cos phi.

7) Jika frekuensi naik, maka Z_L dan Z_C berubah menjadi?
- A. Z_L turun, Z_C naik
- B. Z_L naik, Z_C turun
- C. Z_L naik, Z_C tetap
- D. Z_L tetap, Z_C naik
Jawaban: B
Pembahasan: Z_L = j omega L (naik), Z_C = 1/(j omega C) (turun).

8) Proyeksi vektor berputar pada sumbu real menghasilkan?
- A. Garis lurus
- B. Gelombang sinus
- C. Gelombang segitiga
- D. Step function
Jawaban: B
Pembahasan: Proyeksi vektor berputar pada sumbu real menghasilkan sinus.

## Level 2 (Perhitungan Dasar)
9) Hitung Z_L untuk L = 0.1 H, f = 50 Hz.
- A. j15.7 ohm
- B. j31.4 ohm
- C. j50 ohm
- D. j100 ohm
Jawaban: B
Pembahasan: omega = 2 pi 50 = 314 rad/s, Z_L = j omega L = j31.4 ohm.

10) Hitung Z_C untuk C = 100 uF, f = 50 Hz.
- A. -j31.8 ohm
- B. -j10 ohm
- C. j31.8 ohm
- D. j10 ohm
Jawaban: A
Pembahasan: Z_C = 1/(j omega C) = -j31.8 ohm.

11) R = 10 ohm, L = 50 mH, f = 50 Hz. Z_total seri?
- A. 10 + j7.85
- B. 10 + j15.7
- C. 10 - j15.7
- D. 15.7 + j10
Jawaban: B
Pembahasan: omega = 314, omega L = 15.7, Z = 10 + j15.7.

12) V = 220 angle 0, Z = 10 + j10. Berapa I?
- A. 15.6 angle -45 deg
- B. 22 angle 0 deg
- C. 15.6 angle +45 deg
- D. 31.1 angle -90 deg
Jawaban: A
Pembahasan: |Z| = 14.14, I = 220/14.14 = 15.6 A, fase -45 deg.

13) Jika pf = 0.7, kira-kira sudut phi?
- A. 20 deg
- B. 45 deg
- C. 60 deg
- D. 80 deg
Jawaban: B
Pembahasan: arccos(0.7) sekitar 45.6 derajat.

14) Dampak utama memperbaiki faktor daya adalah?
- A. Arus naik
- B. Arus turun dan rugi-rugi turun
- C. Tegangan turun
- D. Frekuensi naik
Jawaban: B
Pembahasan: PF naik membuat arus lebih kecil untuk daya aktif sama.

## Level 3 (Aplikasi)
15) Dengan referensi cos, phasor untuk v(t) = 10 cos(omega t + 20 deg) adalah?
- A. 10 angle 20
- B. 10 angle -20
- C. 20 angle 10
- D. 10 angle 0
Jawaban: A
Pembahasan: Dengan referensi cos, fase langsung 20 derajat.

16) Z = 8 - j6 menunjukkan karakter beban?
- A. Induktif
- B. Kapasitif
- C. Resistif murni
- D. Tidak bisa ditentukan
Jawaban: B
Pembahasan: Imaginer negatif berarti kapasitif.

17) Pada resonansi seri RLC, kondisi yang benar?
- A. Z_L > Z_C
- B. Z_L = Z_C dan fase nol
- C. Z_L < Z_C
- D. Fase 90 deg
Jawaban: B
Pembahasan: Resonansi terjadi saat reaktansi saling meniadakan.

18) Rumus daya kompleks yang benar?
- A. S = V * I
- B. S = V * I*
- C. S = I / V
- D. S = V / I
Jawaban: B
Pembahasan: S = V dikali konjugat I.

19) Selisih fase 30 deg pada 50 Hz setara waktu?
- A. 0.83 ms
- B. 1.67 ms
- C. 3.33 ms
- D. 10 ms
Jawaban: B
Pembahasan: delta t = phi/(360 f) = 30/(360*50) = 1/600 s.

20) R = 20 ohm, X = 15 ohm (induktif). PF?
- A. 0.6
- B. 0.7
- C. 0.8
- D. 0.9
Jawaban: C
Pembahasan: phi = arctan(15/20)=36.9 deg, pf = cos phi = 0.8.

## Changelog
- 2026-02-06: Menyusun bank soal 20 butir dengan pembahasan.
