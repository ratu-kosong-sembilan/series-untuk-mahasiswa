# Tahapan Perencanaan → Implementasi → Pengujian

## Ringkasan Tujuan
Membangun alat ukur arus petir dengan sensor Rogowski + integrator untuk mendapatkan:
- Arus puncak (I_peak)
- Front time (t10–t90)
- Half time (t50 setelah puncak)
- Steepness (di/dt maksimum atau slope 10–90%)

## 0. Spesifikasi Awal (Wajib ditetapkan)
- Rentang arus target: _____ kA (mis. 100–200 kA)
- Bentuk gelombang target: 10/350 µs (petir) atau 8/20 µs (surge)
- Output full-scale: 5 V atau 10 V
- Lingkungan: lab / lapangan
- Akurasi target: _____ %

## 1. Studi Referensi & Standar
- Definisi parameter wave shape (front time, half time)
- Rujukan metode pengukuran arus impuls (IEC/IEEE)
- Praktik proteksi & keselamatan HV

## 2. Desain Sistem (Block Diagram)
- Rogowski coil → integrator → proteksi → ADC/DAQ → firmware/PC
- Pilih analog vs digital integrator
- Tentukan bandwidth minimal (untuk front time 10 µs, perlu sampling >1–5 MS/s)

## 3. Desain Rogowski Coil
- Pilih: beli coil siap pakai vs fabrikasi sendiri
- Parameter: jumlah lilitan, diameter, M (mutual inductance)
- Output coil: v(t) = M * di/dt

## 4. Desain Integrator
- Integrator analog (op-amp) atau digital
- Tentukan RC (jika analog): K = M/(RC)
- Tambah reset/drift control

## 5. Proteksi & Isolasi
- TVS / MOV / GDT di input
- Isolasi & grounding
- Shielding enclosure (EMI tinggi)

## 6. DAQ & Perekaman
- ADC resolution: minimal 12–16 bit
- Sampling rate: ≥ 1–5 MS/s
- Simpan data raw untuk post-processing

## 7. Algoritma Ekstraksi Parameter
- I_peak = max(i(t))
- t10, t90 → front time = t90 - t10
- t50 after peak → half time = t50 - t_peak
- Steepness = max(di/dt) atau (0.9I - 0.1I)/(t90 - t10)

## 8. Prototipe & Kalibrasi
- Uji coil dengan injeksi arus terukur
- Validasi gain (5 V vs 10 V)
- Koreksi offset & drift

## 9. Pengujian Lab
- Uji waveform kecil dulu (generator pulsa)
- Uji bandwidth dan noise
- Bandingkan dengan sensor referensi

## 10. Pengujian Lapangan
- Pasang dengan SOP keselamatan HV
- Proteksi input aktif
- Cross-check data jika ada sistem referensi

## 11. Deliverables
- Skema rangkaian integrator
- Spesifikasi coil
- Prosedur pengujian
- Dataset contoh + laporan hasil

## 12. Risiko & Mitigasi
- Over-range → clamp & margin
- Noise tinggi → shielding + filtering
- Drift integrator → reset + digital correction

---

## Checklist Implementasi (siap dipakai)
- [ ] Spesifikasi final ditetapkan
- [ ] Coil tersedia & diuji
- [ ] Integrator stabil & terkalibrasi
- [ ] Proteksi input terpasang
- [ ] DAQ terkoneksi
- [ ] Algoritma ekstraksi parameter jalan
- [ ] Uji lab lulus
- [ ] Uji lapangan lulus

---

## Daftar Komponen & Spesifikasi Minimum

### 1) Rogowski Coil
- Bandwidth: minimal 1 MHz (lebih tinggi lebih baik)
- Linearitas: ±1% atau lebih baik
- Output: sesuai integrator (tegangan aman)
- Isolasi: sesuai level HV instalasi

### 2) Integrator (Analog)
- Op-amp: low-noise, high slew-rate, rail-to-rail jika diperlukan
- R_in & C_f ditentukan agar output full-scale 5 V/10 V
- Tambahkan reset/bleeder untuk mengatasi drift

### 3) Proteksi Input
- TVS diode / GDT / MOV sesuai level surge
- Resistor seri kecil untuk limit arus input

### 4) DAQ / ADC
- Sampling rate: ≥ 1–5 MS/s (untuk front time 10 µs)
- Resolusi: 12–16 bit
- Input range: sesuai 5 V atau 10 V

### 5) Power Supply
- Low-noise supply untuk op-amp
- Proteksi ESD & EMC filtering

### 6) Enclosure & Kabel
- Shielded enclosure (metal)
- Kabel coax / twisted pair ber-shield
- Grounding single-point

### 7) Perangkat Lunak
- Perekaman raw data
- Ekstraksi parameter (I_peak, t10, t90, t50, di/dt)

### 8) Referensi Uji
- Sensor referensi (CT/coil lain) jika tersedia
- Generator pulsa kecil untuk kalibrasi awal

