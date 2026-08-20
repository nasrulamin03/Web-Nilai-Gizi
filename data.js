// ============================================================
// DATA MENU HARIAN — SPPG Blitar Talun Kamulan 2
// Edit bagian ini setiap hari untuk memperbarui menu & gizi
// ============================================================

const menuHariIni = {
  tanggal: "", // Kosongkan "" untuk tanggal otomatis hari ini, atau isi "2026-08-18"
  foto: "images/menu-hari-ini.jpg",
  menu: [
    { nama: "Nasi Putih",        kategori: "Karbohidrat", ikon: "🍚" },
    { nama: "Ayam Bumbu Kuning", kategori: "Protein",     ikon: "🍗" },
    { nama: "Tumis Kangkung",    kategori: "Sayuran",     ikon: "🥬" },
    { nama: "Pisang Ambon",      kategori: "Buah",        ikon: "🍌" },
    { nama: "Susu UHT Putih",    kategori: "Minuman",     ikon: "🥛" },
  ],
  gizi: {
    energi:      { nilai: 650, satuan: "kkal" },
    protein:     { nilai: 22,  satuan: "g" },
    karbohidrat: { nilai: 85,  satuan: "g" },
    lemak:       { nilai: 18,  satuan: "g" },
    serat:       { nilai: 4,   satuan: "g" },
    kalsium:     { nilai: 210, satuan: "mg" },
  },
  alergen: "Mengandung susu sapi. Konsultasikan dengan wali kelas jika ada alergi.",
};

// ============================================================
// RIWAYAT MENU — 7 Hari Terakhir
// ============================================================

const riwayatMenu = [
  { tanggal: "2026-08-18", hari: "Senin",  menu: "Nasi, Ayam Bumbu Kuning, Tumis Kangkung, Pisang, Susu",     energi: 650, emoji: "🍗" },
  { tanggal: "2026-08-15", hari: "Jumat",  menu: "Nasi, Ikan Goreng Tepung, Cap Cay, Jeruk, Susu",            energi: 620, emoji: "🐟" },
  { tanggal: "2026-08-14", hari: "Kamis",  menu: "Nasi, Tahu Tempe Bacem, Sayur Bening Bayam, Semangka, Susu", energi: 590, emoji: "🧆" },
  { tanggal: "2026-08-13", hari: "Rabu",   menu: "Nasi, Sop Ayam, Perkedel Jagung, Melon, Susu",              energi: 640, emoji: "🍲" },
  { tanggal: "2026-08-12", hari: "Selasa", menu: "Nasi, Rendang Daging, Tumis Buncis, Pepaya, Susu",          energi: 680, emoji: "🥩" },
  { tanggal: "2026-08-11", hari: "Senin",  menu: "Nasi, Telur Dadar, Sayur Lodeh, Apel, Susu",                energi: 600, emoji: "🍳" },
  { tanggal: "2026-08-08", hari: "Jumat",  menu: "Nasi, Pepes Ikan, Tumis Taoge, Mangga, Susu",               energi: 610, emoji: "🐠" },
];

// ============================================================
// STATISTIK PROGRAM
// ============================================================

const statistik = [
  { label: "Siswa Terlayani", nilai: 1250, ikon: "👨‍🎓", satuan: "siswa" },
  { label: "Sekolah Mitra",   nilai: 8,    ikon: "🏫",   satuan: "sekolah" },
  { label: "Porsi Per Hari",  nilai: 1250, ikon: "🍱",   satuan: "porsi" },
  { label: "Hari Berjalan",   nilai: 120,  ikon: "📅",   satuan: "hari" },
];
