# Prompt / PRD Restyle UI
# Landing Page SPPG Blitar Talun Kamulan 2 → Gaya "Sunshine Pediatric Clinic"

**Versi:** 1.0
**Tanggal:** 20 Agustus 2026
**Tujuan dokumen:** Panduan (bisa langsung dipakai sebagai prompt ke AI coding/desainer) untuk mengubah tampilan landing page SPPG yang sudah ada agar mengikuti gaya visual referensi — bersih, hangat, profesional, dengan aksen navy & gold.

---

## 1. Ringkasan Perubahan

Landing page SPPG saat ini bergaya "ceria anak-anak" (biru tua/biru muda, kartu membulat besar bergaya taman kanak-kanak). Referensi baru (*Sunshine Pediatric Clinic*) tetap ramah dan hangat, tapi jauh lebih **rapi, minim clutter, dan profesional** — cocok untuk membangun kepercayaan institusi kesehatan/gizi. Restyle ini **mempertahankan struktur konten SPPG** (menu hari ini, tanggal, nilai gizi, tentang program, dsb.), hanya mengganti bahasa visual (warna, tipografi, layout section, komponen UI).

---

## 2. Palet Warna Baru

| Elemen | Warna | Kode Hex (perkiraan) |
|---|---|---|
| Primary text/heading | Navy tua | `#0F2A52` |
| Aksen tombol utama (CTA) | Gold/Kuning hangat | `#F5B301` |
| Aksen sekunder (ikon, garis bawah) | Biru cerah | `#2F80ED` |
| Latar belakang section terang | Putih | `#FFFFFF` |
| Latar belakang section alternatif | Biru sangat pucat | `#EAF3FB` |
| Latar belakang section CTA bawah | Biru medium | `#3E8FD8` |
| Footer | Navy sangat gelap | `#0B1F3A` |
| Aksen hangat pendukung (bintang, testimoni) | Krem lembut | `#FCEFD8` |

> Perbedaan kunci dari versi lama: dominasi biru diturunkan, digantikan **putih bersih + navy sebagai warna teks/heading utama + gold sebagai warna aksi (tombol)**. Biru muda hanya jadi warna aksen ikon & latar selang-seling.

---

## 3. Tipografi

- **Heading:** Serif/sans tebal, tegas, ukuran besar (mirip "Healthy Kids, Happy Futures") — untuk SPPG bisa jadi headline seperti *"Gizi Baik, Masa Depan Cerah"*
- **Body text:** Sans-serif reguler, abu gelap, ukuran nyaman dibaca
- **Label kategori kecil di atas heading** (huruf kapital, letter-spacing lebar, warna biru) — pola "OUR SERVICES", "WHY CHOOSE US" pada referensi

---

## 4. Struktur Section (Mapping Konten Lama → Layout Baru)

| Section Referensi | Isi Adaptasi untuk SPPG |
|---|---|
| **Navbar** (logo + menu horizontal + tombol CTA kanan) | Logo SPPG Kamulan 2, menu: Beranda / Menu Hari Ini / Nilai Gizi / Tentang / Kontak, tombol CTA kanan: "Lihat Menu Hari Ini" |
| **Hero** (headline besar kiri, foto besar kanan, 3 badge fitur di bawah) | Headline besar: nama program + tagline, tombol "Lihat Menu Hari Ini" (gold) + "Tentang Program" (outline), foto kegiatan makan bergizi, 3 badge kecil: Tanggal Hari Ini / Menu Bergizi / Standar BGN |
| **Grid layanan (6 kartu ikon bulat)** | Diganti jadi **grid kategori nilai gizi**: Energi, Protein, Karbohidrat, Lemak, Serat, Info Alergen — tiap kartu ikon bulat warna biru/gold bergantian |
| **"Why Choose Us" (list 2 kolom + gambar/teks kiri)** | "Kenapa SPPG Kamulan 2" — poin: Menu Terstandar BGN, Transparan & Terbuka, Diawasi Ahli Gizi, Update Setiap Hari |
| **Foto interior + teks "A Place Where Kids Feel at Home"** | Foto dapur/proses masak SPPG + teks "Dapur Bersih, Proses Terpantau" dengan tombol "Selengkapnya" |
| **Grid tim (foto bulat + nama + spesialisasi)** | Diganti jadi **tim/ahli gizi & penanggung jawab SPPG** (foto bulat, nama, peran) — opsional jika data tersedia |
| **Testimoni (3 kartu quote + bintang)** | Testimoni dari sekolah/PIC atau orang tua siswa tentang program |
| **CTA banner (background biru, tombol gold, ilustrasi maskot kanan)** | "Pantau Menu & Gizi Anak Setiap Hari" + tombol "Lihat Menu Hari Ini" |
| **Footer navy gelap (4 kolom + sosial media)** | Kolom: Logo+alamat, Tautan Cepat, Layanan (Menu/Gizi/Riwayat), Kontak, Sosial Media |

---

## 5. Spesifikasi Komponen UI

- **Tombol utama (CTA):** latar gold `#F5B301`, teks navy tebal, sudut membulat penuh (pill-shape), ikon kecil di kiri teks
- **Tombol sekunder:** outline putih/navy tipis, teks navy, ikon play/panah kecil
- **Kartu ikon (grid gizi):** kotak putih, sudut membulat sedang (rounded-xl), shadow lembut, ikon dalam lingkaran warna solid (biru atau gold bergantian), judul bold navy, deskripsi 1 baris abu-abu
- **Badge kecil di hero:** ikon bulat kecil + 2 baris teks (judul bold + subjudul tipis)
- **Section label:** teks kecil huruf kapital biru dengan garis bawah pendek kuning di bawah heading utama
- **Testimoni card:** latar putih, tanda kutip besar, rating bintang gold, nama + peran di bawah
- **Footer:** latar navy gelap `#0B1F3A`, teks putih/abu muda, ikon sosial media bulat kecil

---

## 6. Nada Visual & Fotografi

- Gunakan foto asli kegiatan (penyajian makanan, anak-anak makan, dapur SPPG) — bukan ilustrasi kartun seperti versi lama
- Foto hero: natural, hangat, pencahayaan cerah, bentuk foto dengan sudut membulat mengikuti kontur (blob shape) seperti referensi
- Kurangi elemen dekoratif berlebihan (awan, siput, karakter kartun) — cukup 1-2 aksen halus (mis. bintang kecil atau garis lengkung tipis) agar tetap terasa "hangat" tanpa terasa "TK"

---

## 7. Prompt Siap Pakai (untuk AI coding/desain)

> Ubah tampilan landing page SPPG Blitar Talun Kamulan 2 dari gaya "ceria anak-anak biru tua/biru muda" menjadi gaya bersih dan profesional seperti referensi klinik anak "Sunshine Pediatric Clinic". Gunakan palet warna: navy `#0F2A52` untuk heading/teks utama, gold `#F5B301` untuk tombol CTA, biru cerah `#2F80ED` untuk aksen ikon, latar putih dan biru pucat `#EAF3FB` berselang-seling antar section, dan footer navy gelap `#0B1F3A`. Pertahankan struktur konten yang sudah ada (menu hari ini, tanggal, nilai gizi, tentang program, kontak), tapi susun ulang mengikuti pola: navbar horizontal dengan tombol CTA pill-shape gold di kanan; hero dua kolom (headline besar + foto asli dengan 3 badge fitur singkat di bawah teks); grid 6 kartu ikon bulat untuk kategori nilai gizi; section "kenapa memilih kami" dua kolom; section foto interior/dapur dengan teks pendamping; grid testimoni 3 kolom dengan rating bintang; CTA banner besar berlatar biru dengan tombol gold; dan footer 4 kolom gelap. Gunakan tipografi heading tebal besar, label section kapital kecil berwarna biru, kartu bersudut membulat dengan shadow lembut, dan foto asli (bukan ilustrasi kartun) sebagai elemen visual utama.

---

*Dokumen ini dapat langsung digunakan sebagai instruksi ke AI pembuat kode (mis. saat membangun ulang file HTML/React) atau sebagai brief ke desainer.*
