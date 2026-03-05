# SRT LENGKAP 40 MENIT (CORE-001)

## Tujuan
Menyediakan subtitle lengkap dan sinkron dengan timeline 0:00-40:00.

## Ruang Lingkup
Subtitle long-form CORE-001.

## Definisi Selesai (DoD)
- Subtitle mencakup seluruh durasi 40 menit.
- Sinkron dengan 20-NASKAH-DETAIL-PER-MENIT.

## Checklist
- [x] Subtitle lengkap 40 menit
- [x] Sinkron dengan timeline per menit
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [20-NASKAH-DETAIL-PER-MENIT.md](./20-NASKAH-DETAIL-PER-MENIT.md)
- [25-VO-SUBTITLE-SRT.md](./25-VO-SUBTITLE-SRT.md)

## SRT
```srt
1
00:00:00,000 --> 00:01:00,000
Kenapa angka imajiner bisa menjelaskan
listrik nyata? Simbol j menyederhanakan.

2
00:01:00,000 --> 00:02:00,000
Banyak mahasiswa hafal Z = R + jX,
tapi belum paham kenapa ada j.

3
00:02:00,000 --> 00:03:00,000
Target kita: lihat gelombang AC sebagai
vektor berputar. Konsep kompleks jadi natural.

4
00:03:00,000 --> 00:04:00,000
Roadmap: phasor, impedansi, lalu faktor daya.
Semua saling terhubung.

5
00:04:00,000 --> 00:05:00,000
Sinus dasar: v(t) = Vm sin(omega t + phi).
Amplitudo, frekuensi, dan fase.

6
00:05:00,000 --> 00:06:00,000
Pergeseran fase artinya puncak gelombang
terjadi di waktu berbeda: delta t = delta phi.

7
00:06:00,000 --> 00:07:00,000
Euler: e^(jtheta) = cos theta
+ j sin theta. Ini jembatan ke vektor.

8
00:07:00,000 --> 00:08:00,000
Sumbu real dan imajiner membentuk
bidang kompleks. Ini alat visual.

9
00:08:00,000 --> 00:09:00,000
Vektor berputar dengan kecepatan omega
punya proyeksi sinus di sumbu real.

10
00:09:00,000 --> 00:10:00,000
Phasor adalah snapshot vektor berputar
itu: magnitude dan fase dalam satu gambar.

11
00:10:00,000 --> 00:11:00,000
Kita pindah dari time-domain ke phasor
agar perhitungan jadi lebih sederhana.

12
00:11:00,000 --> 00:12:00,000
Konversi cepat: Vm sin(omega t + phi)
menjadi V angle phi.

13
00:12:00,000 --> 00:13:00,000
Rekap phasor: magnitude, fase,
dan hubungan dengan gelombang sinus.

14
00:13:00,000 --> 00:14:00,000
Bilangan kompleks adalah vektor.
Penjumlahan berarti vektor + vektor.

15
00:14:00,000 --> 00:15:00,000
Perkalian j berarti rotasi 90 derajat.
Inilah inti fase pada RLC.

16
00:15:00,000 --> 00:16:00,000
Aljabar kompleks tetap sederhana,
tapi maknanya geometris.

17
00:16:00,000 --> 00:17:00,000
Kita bisa menambah, mengalikan, membagi
tanpa kehilangan intuisi visual.

18
00:17:00,000 --> 00:18:00,000
Contoh sederhana menunjukkan hasil aljabar
selaras dengan gambar vektor.

19
00:18:00,000 --> 00:19:00,000
Ringkas: j adalah rotasi,
bilangan kompleks adalah alat visual.

20
00:19:00,000 --> 00:20:00,000
Masuk ke impedansi: menyatukan R, L, C
dalam satu bahasa.

21
00:20:00,000 --> 00:21:00,000
Resistor: Z = R, arus dan tegangan
sefase.

22
00:21:00,000 --> 00:22:00,000
Induktor: Z = j omega L,
tegangan mendahului arus 90 derajat.

23
00:22:00,000 --> 00:23:00,000
Kapasitor: Z = 1/(j omega C),
arus mendahului tegangan 90 derajat.

24
00:23:00,000 --> 00:24:00,000
Diagram phasor menunjukkan pergeseran fase
pada R, L, dan C.

25
00:24:00,000 --> 00:25:00,000
Contoh hitung Z seri:
gabungkan R dan reaktansi jadi a + jb.

26
00:25:00,000 --> 00:26:00,000
Arus dihitung dengan I = V / Z.
Fase arus otomatis terlihat.

27
00:26:00,000 --> 00:27:00,000
Diagram phasor V dan I
membuat hubungan fase jadi jelas.

28
00:27:00,000 --> 00:28:00,000
Daya kompleks: S = P + jQ,
memisahkan daya aktif dan reaktif.

29
00:28:00,000 --> 00:29:00,000
Segitiga daya memperlihatkan hubungan
P, Q, dan S.

30
00:29:00,000 --> 00:30:00,000
Faktor daya adalah cos phi.
Semakin besar phi, daya reaktif bertambah.

31
00:30:00,000 --> 00:31:00,000
Industri kena denda bila faktor daya rendah
karena arus tinggi tanpa kerja.

32
00:31:00,000 --> 00:32:00,000
Koreksi faktor daya dengan kapasitor bank
mengurangi arus.

33
00:32:00,000 --> 00:33:00,000
Di simulasi, ubah R, L, C
dan lihat phasor bergerak real-time.

34
00:33:00,000 --> 00:34:00,000
Menaikkan R mengubah magnitude
dan sedikit mempengaruhi fase.

35
00:34:00,000 --> 00:35:00,000
Menaikkan L atau C mengubah fase
lebih signifikan.

36
00:35:00,000 --> 00:36:00,000
Frekuensi naik membuat Z_L naik
dan Z_C turun.

37
00:36:00,000 --> 00:37:00,000
Studi kasus motor: PF 0.7
ditingkatkan ke 0.95 dengan kapasitor.

38
00:37:00,000 --> 00:38:00,000
Ringkasan akhir: sinus sebagai vektor.
Phasor mudahkan hitung; faktor daya penting.

39
00:38:00,000 --> 00:39:00,000
Kuis cepat: arti j dan fase +90 pada Z_L
serta definisi faktor daya.

40
00:39:00,000 --> 00:40:00,000
Coba simulasi interaktif
dan kerjakan bank soal agar konsep kuat.
```

## Changelog
- 2026-02-06: Menyusun SRT lengkap 40 menit dan menyelaraskan dengan timeline.
- 2026-02-06: Rapikan SRT (line breaks 32-42 char), konsistensi istilah, dan notasi a + jb. Alasan: validasi QC subtitle. Dampak: SRT siap sinkron dan mudah dibaca.
