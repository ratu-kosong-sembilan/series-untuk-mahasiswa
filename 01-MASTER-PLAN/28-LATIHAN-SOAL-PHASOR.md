# LATIHAN SOAL PHASOR: Konversi Polar-Rectangular
## Dokumen Produksi - CORE-001 Extended

## Metadata Produksi
- **Kode**: CORE-001-EXT-01
- **Judul**: Latihan Soal Phasor: Konversi Polar ke Rectangular
- **Durasi**: 15:00 (video) + 30:00 (latihan mandiri)
- **Target**: Mahasiswa yang sudah nonton CORE-001 tapi butuh praktik
- **Status**: 🟡 Pre-Production

---

## Tujuan
1. Mahasiswa bisa konversi A∠θ → a + jb dengan cepat
2. Mahasiswa paham makna geometris konversi
3. Mahasiswa bisa operasikan phasor (tambah, kurang, kali)

---

## Script Video (15 menit)

### Segmen 1: Review Konsep (2:00)
**VO**: "Di video sebelumnya kita belajar phasor. Sekarang kita praktik."

**Visual**: 
- Text: "Polar: A∠θ" vs "Rectangular: a + jb"
- Diagram lingkaran satuan

---

### Segmen 2: Konversi Polar → Rectangular (5:00)
**Contoh 1 (Mudah)**:
- Soal: `10∠0°`
- VO: "Cos 0 adalah 1, sin 0 adalah 0. Jadi 10 + j0."
- Visual: Vektor horizontal, proyeksi ke sumbu real.

**Contoh 2 (Sudut 30°)**:
- Soal: `10∠30°`
- Hitung: 10×cos(30°) = 8.66, 10×sin(30°) = 5
- Hasil: `8.66 + j5`
- Visual: Diagram dengan proyeksi.

**Contoh 3 (Sudut 90°)**:
- Soal: `10∠90°`
- VO: "Cos 90 = 0, sin 90 = 1. Jadi 0 + j10."
- Visual: Vektor vertikal murni.

**Contoh 4 (Sudut 180°)**:
- Soal: `10∠180°`
- Hasil: `-10 + j0`

---

### Segmen 3: Konversi Rectangular → Polar (4:00)
**Rumus**: 
- A = √(a² + b²)
- θ = tan⁻¹(b/a)

**Contoh 1**: `3 + j4`
- A = √(9+16) = 5
- θ = tan⁻¹(4/3) = 53.13°
- Hasil: `5∠53.13°`

**Contoh 2**: `5 + j0` (tegangan DC)
- Hasil: `5∠0°`

**Contoh 3**: `0 + j10` (induktor murni)
- Hasil: `10∠90°`

---

### Segmen 4: Operasi Penjumlahan (2:00)
**Cara**: Konversi ke rectangular → Jumlahkan → Konversi balik

**Soal**: `10∠30° + 5∠60°`
- Langkah 1: Jadi `(8.66+j5) + (2.5+j4.33)`
- Langkah 2: Jumlahkan = `11.16 + j9.33`
- Langkah 3: Konversi ke polar ≈ `14.55∠39.8°`

**Visual**: Diagram vektor (parallelogram method).

---

### Segmen 5: Perkalian dengan j (1:00)
**Konsep**: `j = 1∠90°`
- Kalikan j = rotasi 90° CCW
- Contoh: `5∠0° × j = 5∠90°`

**Visual**: Vektor berputar 90 derajat.

---

### Segmen 6: CTA & Download Soal (1:00)
**VO**: "Download 10 soal latihan di link deskripsi. Praktikkan sendiri!"

**Visual**: 
- Button "Download PDF"
- Preview soal (blur)

---

## Asset List

| No | Asset | Tipe | Durasi | Status |
|----|-------|------|--------|--------|
| 1 | Diagram polar-rectangular | Animasi | 30s | ⬜ |
| 2 | Contoh perhitungan 1-4 | Screencast/Math | 5:00 | ⬜ |
| 3 | Animasi rotasi j | Animasi | 15s | ⬜ |
| 4 | Worksheet PDF | Dokumen | - | ⬜ |
| 5 | Thumbnail | Gambar | - | ⬜ |

---

## Soal Latihan (PDF)

### Level 1: Mudah (4 soal)
1. Konversi `10∠0°` ke rectangular
2. Konversi `0 + j5` ke polar
3. Konversi `100∠90°` ke rectangular
4. Konversi `-10 + j0` ke polar

### Level 2: Medium (4 soal)
5. Konversi `10∠30°` ke rectangular
6. Konversi `3 + j4` ke polar
7. Konversi `220∠-30°` ke rectangular (tegangan PLN)
8. Konversi `5 + j8.66` ke polar

### Level 3: Aplikasi (2 soal)
9. Jumlahkan: `10∠0° + 10∠90°`
10. Hitung: `j × (5 + j5)`

### Kunci Jawaban
[Disertakan di akhir PDF]

---

## Timeline Produksi

| Task | Estimasi | Assignee |
|------|----------|----------|
| Script final | 2 jam | You |
| Recording VO | 1 jam | You |
| Editing video | 4 jam | Editor |
| Animasi math | 3 jam | Animator |
| PDF worksheet | 1 jam | You |
| Upload & publish | 30 min | You |
| **Total** | **~12 jam** | |

---

## Integration ke Website

### Tampilan di index.html
```html
<section id="latihan-phasor">
  <h2>📝 Latihan Soal Phasor</h2>
  <p>Konversi Polar ↔ Rectangular</p>
  
  <div class="video-embed">
    <iframe src="YOUTUBE_EMBED_LINK"></iframe>
  </div>
  
  <a href="assets/latihan-soal-phasor.pdf" download>
    📥 Download Worksheet PDF
  </a>
</section>
```

---

## Success Metrics
- [ ] Video ditonton 100+ kali dalam 1 bulan
- [ ] Download PDF 50+ kali
- [ ] Feedback positif dari 5+ mahasiswa

---

**Status Produksi**: 🟡 Siap direkam
**Next Step**: Booking jadwal recording VO
