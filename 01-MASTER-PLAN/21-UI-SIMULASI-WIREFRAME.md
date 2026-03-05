# UI SIMULASI WIREFRAME

## Tujuan
Mendeskripsikan layout dan komponen UI untuk simulasi phasor dan impedansi.

## Ruang Lingkup
Wireframe halaman simulasi web (desktop dan mobile).

## Definisi Selesai (DoD)
- Layout dan komponen utama jelas.
- Interaksi dasar terdefinisi.

## Checklist
- [x] Layout desktop dan mobile dijelaskan
- [x] Komponen utama terdaftar
- [x] Rujukan lintas dokumen tersedia

## Rujukan
- [19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md](./19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md)

## Wireframe Desktop (16:9)
```
------------------------------------------------------------
| Header: CORE-001 Simulasi Phasor                          |
------------------------------------------------------------
| Left Panel (Controls) | Center (Canvas) | Right (Metrics) |
| - Vm slider           | - Phasor vector | - Z total        |
| - f slider            | - Time waveform | - I phasor       |
| - R, L, C sliders     | - Power triangle| - PF, P, Q       |
| - Toggle: RLC seri    |                 | - Notes          |
------------------------------------------------------------
| Footer: CTA + link kuis                                   |
------------------------------------------------------------
```

## Wireframe Mobile (9:16)
- Header sticky
- Canvas di atas (60% layar)
- Controls accordion di bawah
- Metrics tampil sebagai cards

## Komponen Utama
- Slider: Vm, f, R, L, C
- Toggle: mode seri/paralel (v1 hanya seri)
- Canvas: phasor + sinus + power triangle
- Metrics: Z_total, I, pf
- CTA: "Coba kuis"

## Interaksi
- Slider update real-time pada phasor dan grafik
- Hover/tooltip untuk makna tiap parameter
- Tombol reset ke default

## Changelog
- 2026-02-06: Menyusun wireframe UI simulasi CORE-001.
- 2026-02-06: Ubah "quiz" menjadi "kuis". Alasan: konsistensi istilah Indonesia. Dampak: UI copy selaras dengan naskah.
