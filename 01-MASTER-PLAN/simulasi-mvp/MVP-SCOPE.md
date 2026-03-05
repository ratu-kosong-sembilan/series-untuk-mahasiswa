# SIMULASI MVP SCOPE

## Tujuan
Menetapkan scope dan acceptance criteria untuk simulasi MVP CORE-001.

## Ruang Lingkup
Simulasi phasor dan impedansi RLC seri dengan visual real-time.

## Definisi Selesai (DoD)
- Fitur utama berjalan sesuai acceptance criteria.
- Dapat digunakan untuk demo di video CORE-001.

## Checklist
- [x] Scope MVP jelas
- [x] Fitur utama terdaftar
- [x] Acceptance criteria terdefinisi

## Rujukan
- [../19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md](../19-SIMULASI-SPEC-MATEMATIKA-EM-TRANSIEN.md)
- [../21-UI-SIMULASI-WIREFRAME.md](../21-UI-SIMULASI-WIREFRAME.md)

## Scope Fitur MVP
- Slider Vm, f, R, L, C
- Plot sinus time-domain
- Diagram phasor V dan I
- Display Z_total (rectangular + magnitude/fase)
- Display P, Q, S dan faktor daya

## Non-Goals (V1)
- Mode paralel RLC
- Export data ke CSV
- Animasi 3D

## Acceptance Criteria
- Perubahan slider memperbarui grafik < 200 ms.
- Nilai Z_total dan I sesuai formula pada spec.
- UI tetap responsif pada layar 1366x768 dan 9:16.

## Changelog
- 2026-02-06: Membuat scope dan acceptance criteria simulasi MVP.
- 2026-02-06: Ubah istilah "phase" menjadi "fase". Alasan: konsistensi istilah. Dampak: teks UI spec selaras.
