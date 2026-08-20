# PRD (Product Requirements Document)
# Website Informasi Gizi — SPPG Blitar Talun Kamulan 2

**Versi:** 1.0
**Tanggal:** 18 Agustus 2026
**Disusun oleh:** Nasrul (SPPG Kamulan)
**Status:** Draft

---

## 1. Latar Belakang

SPPG Blitar Talun Kamulan 2 membutuhkan sebuah website sederhana sebagai kanal informasi publik mengenai menu harian dan kandungan nilai gizi program Makan Bergizi Gratis (MBG). Website ini bertujuan untuk meningkatkan transparansi kepada sekolah (PIC), orang tua siswa, serta pihak evaluator/pemangku kepentingan yang membutuhkan akses cepat terhadap informasi menu dan gizi tanpa perlu menghubungi pihak SPPG secara langsung.

Referensi gaya visual mengikuti template pendidikan anak (ceria, ramah, ilustratif) namun dengan palet warna disesuaikan menjadi **biru tua dan biru muda** agar terkesan lebih formal, bersih, dan terpercaya — cocok untuk konteks institusional pemerintah/gizi masyarakat.

---

## 2. Tujuan Produk

1. Menampilkan **menu makanan hari ini** secara jelas dan mudah dibaca.
2. Menampilkan **tanggal** penyajian menu secara otomatis/dinamis.
3. Menampilkan **nilai gizi** (kalori, protein, karbohidrat, lemak, dll.) dari menu yang disajikan.
4. Memberikan kesan profesional, bersih, dan terpercaya sesuai konteks program pemerintah.
5. Mudah diakses dari perangkat mobile maupun desktop (responsive).

---

## 3. Target Pengguna

| Pengguna | Kebutuhan |
|---|---|
| Sekolah / PIC | Melihat menu & gizi harian untuk keperluan koordinasi porsi/alergen |
| Orang tua siswa | Memastikan anak mendapat makanan bergizi dan aman (alergen) |
| Tim internal SPPG | Media publikasi menu tanpa proses manual berulang |
| Evaluator / Badan Gizi Nasional | Melihat rekam jejak transparansi penyajian menu |

---

## 4. Ruang Lingkup (Scope)

### Termasuk (In-Scope)
- Landing page single-page atau multi-section berisi:
  - Header/hero dengan identitas SPPG Kamulan 2
  - Tanggal hari ini (otomatis sesuai tanggal akses / dapat diatur manual)
  - Nama & foto menu hari ini
  - Tabel/kartu nilai gizi per menu
  - Riwayat menu (opsional — beberapa hari ke belakang)
- Tampilan responsif (mobile-first, karena banyak diakses via HP)

### Tidak Termasuk (Out-of-Scope) — versi awal
- Sistem login/dashboard admin (v1 bisa update manual via file data)
- Sistem pemesanan/RSVP
- Multi-bahasa

---

## 5. Fitur Utama

### 5.1 Header / Identitas
- Logo & nama "SPPG Blitar Talun Kamulan 2"
- Tagline singkat, contoh: *"Menyajikan Gizi, Membangun Generasi"*
- Navigasi sederhana: Beranda, Menu Hari Ini, Riwayat Menu, Tentang, Kontak

### 5.2 Tanggal & Menu Hari Ini
- Tanggal aktif ditampilkan besar & jelas (format: *Selasa, 18 Agustus 2026*)
- Kartu menu utama menampilkan:
  - Foto makanan
  - Nama menu (misal: Nasi, Ayam Bumbu Kuning, Tumis Kangkung, Buah Pisang, Susu)
  - Kategori (Karbohidrat / Protein / Sayur / Buah / Minuman)

### 5.3 Kartu Nilai Gizi
Ditampilkan sebagai kartu-kartu berwarna (mengikuti gaya referensi — kartu membulat dengan ikon), berisi:
- Energi (kkal)
- Protein (g)
- Karbohidrat (g)
- Lemak (g)
- Serat (g)
- Info alergen (jika ada)

### 5.4 Riwayat Menu (opsional v1.1)
- Grid/kalender kecil menu 7 hari terakhir yang bisa diklik

### 5.5 Tentang Program
- Penjelasan singkat program MBG & Badan Gizi Nasional
- Statistik singkat (jumlah siswa terlayani, jumlah sekolah, dsb.) — gaya "counter" seperti referensi

### 5.6 Footer / Kontak
- Alamat SPPG
- Kontak PIC / narahubung
- Jam operasional

---

## 6. Gaya Visual (Design Style Guide)

Mengadaptasi struktur & mood ceria dari referensi (kartu membulat, ilustrasi lembut, badge, ikon bulat besar), tetapi dengan palet warna yang lebih formal:

### 6.1 Palet Warna

| Elemen | Warna | Kode Hex (referensi) |
|---|---|---|
| Warna Utama (Primary / Header, Tombol) | Biru Tua | `#0B3C74` |
| Warna Aksen (Highlight, Badge) | Biru Muda | `#4FC3F7` |
| Latar Belakang Section | Biru Muda Pucat | `#EAF6FD` |
| Latar Belakang Umum | Putih | `#FFFFFF` |
| Teks Utama | Abu Gelap / Navy | `#1B2A41` |
| Aksen Sukses/Gizi (misal badge protein) | Biru Kehijauan Lembut | `#2FA4A9` |
| Warna Peringatan Alergen | Kuning Lembut | `#FFC94D` (dipakai secukupnya, tetap dominan biru) |

> Catatan: Berbeda dari referensi (oranye/kuning ceria untuk anak), tema ini didominasi **gradasi biru** agar terasa bersih, resmi, dan terpercaya — cocok untuk data gizi & instansi.

### 6.2 Tipografi
- **Heading:** Font tebal, membulat (mis. Poppins / Baloo 2) — menjaga kesan ramah dari referensi
- **Body text:** Font sans-serif reguler (mis. Inter / Nunito Sans) untuk keterbacaan data gizi

### 6.3 Elemen Visual
- Kartu dengan sudut membulat (rounded-2xl) dan bayangan lembut, seperti kartu "Introduction Basic Academics" pada referensi
- Ikon bulat besar untuk kategori gizi (energi, protein, dsb.)
- Ilustrasi lembut (opsional): anak-anak makan sehat, ikon makanan sederhana — gaya flat/line-art, bukan foto stok generik
- Badge melingkar untuk angka statistik (mis. jumlah sekolah terlayani) — mengikuti gaya "93% / 26% / 16%" pada referensi
- Gelombang/curve dekoratif sebagai pemisah antar section (seperti pada referensi), menggunakan warna biru muda pucat

---

## 7. Struktur Halaman (Sitemap)

```
Beranda (Single Page Scroll)
├── Hero Section (identitas + tanggal hari ini)
├── Menu Hari Ini (foto + daftar menu)
├── Nilai Gizi (kartu-kartu gizi)
├── Riwayat Menu (opsional, grid 7 hari)
├── Tentang Program MBG & SPPG Kamulan 2
├── Statistik (jumlah siswa, sekolah, porsi harian)
└── Footer (kontak & alamat)
```

---

## 8. Kebutuhan Data (Content Model)

| Field | Tipe | Contoh |
|---|---|---|
| tanggal | Date | 2026-08-18 |
| nama_menu | Text | "Nasi, Ayam Bumbu Kuning, Tumis Kangkung" |
| foto_menu | Image URL | menu-18aug.jpg |
| kategori_makanan | List | Karbohidrat, Protein, Sayur, Buah |
| energi_kkal | Number | 650 |
| protein_g | Number | 22 |
| karbohidrat_g | Number | 85 |
| lemak_g | Number | 18 |
| serat_g | Number | 4 |
| info_alergen | Text | "Mengandung telur" |

Data dapat dikelola melalui file terstruktur (mis. JSON/CSV sederhana) yang diperbarui setiap hari oleh tim SPPG, tanpa memerlukan sistem login di v1.

---

## 9. Kebutuhan Teknis (Saran)

- **Platform:** Website statis/responsif (HTML/CSS atau React) — ringan, cepat diakses via HP
- **Update konten:** Manual oleh admin melalui file data (v1), atau form input sederhana (v2)
- **Hosting:** Shared hosting sederhana / static hosting (mis. Netlify, Vercel) — biaya rendah
- **Aksesibilitas:** Kontras warna teks-biru tetap memenuhi standar keterbacaan (WCAG AA)

---

## 10. Metrik Keberhasilan

- Website dapat diakses tanpa hambatan oleh PIC sekolah & orang tua
- Menu & nilai gizi harian selalu ter-update sebelum jam makan
- Mengurangi pertanyaan manual ke tim SPPG terkait menu/gizi harian
- Siap ditunjukkan sebagai bukti transparansi saat evaluasi dari Badan Gizi Nasional

---

## 11. Rencana Pengembangan Lanjutan (Roadmap v2+)

- Dashboard admin untuk update menu tanpa edit kode/file
- Notifikasi otomatis ke PIC sekolah saat menu baru terbit
- Filter alergen per siswa
- Statistik gizi mingguan/bulanan dalam bentuk grafik

---

*Dokumen ini adalah draft awal dan dapat disesuaikan berdasarkan masukan tim SPPG Blitar Talun Kamulan 2.*
