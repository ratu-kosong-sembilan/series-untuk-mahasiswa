# SIMULASI SPEC CORE-001 (PHASOR & IMPEDANSI)

## Tujuan
Menentukan spesifikasi simulasi interaktif untuk menjelaskan phasor, impedansi, dan faktor daya.

## Ruang Lingkup
Simulasi sinus, phasor, impedansi RLC, dan daya kompleks.

## Definisi Selesai (DoD)
- Parameter input, formula, dan output ditetapkan.
- Contoh angka tersedia untuk demo.
- Rujukan lintas dokumen tersedia.

## Checklist
- [x] Parameter input didefinisikan
- [x] Formula inti dicantumkan
- [x] Output visual ditetapkan

## Rujukan
- [21-UI-SIMULASI-WIREFRAME.md](./21-UI-SIMULASI-WIREFRAME.md)
- [17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md](./17-SCRIPT-VIDEO-MATEMATIKA-EM-TRANSIEN.md)

## Modul Simulasi
### 1) Sinus & Fase
**Input:** Vm, f, phi  
**Formula:** v(t) = Vm sin(omega t + phi), omega = 2 pi f  
**Output:** Plot sinus + marker fase

### 2) Phasor
**Input:** Vm, phi  
**Formula:** V = Vm angle phi  
**Output:** Diagram vektor kompleks (magnitude + fase)

### 3) Impedansi RLC
**Input:** R, L, C, f  
**Formula:**  
- Z_R = R  
- Z_L = j omega L  
- Z_C = 1 / (j omega C)  
- Z_total (seri) = Z_R + Z_L + Z_C  
**Output:** Nilai Z_total (rectangular + polar)

### 4) Arus & Tegangan
**Input:** V, Z_total  
**Formula:** I = V / Z_total  
**Output:** Phasor I dan pergeseran fase terhadap V

### 5) Daya Kompleks
**Input:** V, I  
**Formula:** S = V * I* = P + jQ  
**Output:** P, Q, S, faktor daya (pf = P/|S|)

## Contoh Angka (Default)
- Vm = 220 V (rms)
- f = 50 Hz
- R = 10 ohm
- L = 50 mH
- C = 100 uF

## Output Visual Minimum
- Plot sinus (time-domain)
- Diagram phasor (V dan I)
- Nilai Z_total dalam bentuk a + jb dan magnitude/fase
- Segitiga daya (P, Q, S)

## Changelog
- 2026-02-06: Menulis spesifikasi simulasi phasor, impedansi, dan daya kompleks.
- 2026-02-06: Ubah istilah "phase" menjadi "fase". Alasan: konsistensi istilah Indonesia. Dampak: spec selaras dengan script dan SRT.
