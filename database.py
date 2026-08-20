#!/usr/bin/env python3
"""
database.py — Setup & inisialisasi database SQLite
SPPG Blitar Talun Kamulan 2 — Website Nilai Gizi
"""

import sqlite3
import os
import json
from datetime import date, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "gizi.db")

# ── Password admin (ubah sesuai kebutuhan) ──────────────────────────────────
ADMIN_PASSWORD = "sppgkamulan2"

def get_db():
    """Dapatkan koneksi database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    """Buat tabel jika belum ada, lalu seed data awal."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db()
    c = conn.cursor()

    # ── Tabel menu ──────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal     TEXT    NOT NULL UNIQUE,
            foto        TEXT    DEFAULT 'images/menu-hari-ini.jpg',
            alergen     TEXT    DEFAULT '',
            catatan     TEXT    DEFAULT '',
            created_at  TEXT    DEFAULT (datetime('now','localtime')),
            updated_at  TEXT    DEFAULT (datetime('now','localtime'))
        )
    """)

    # ── Tabel item menu (relasi ke menu) ────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS menu_item (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            menu_id   INTEGER NOT NULL REFERENCES menu(id) ON DELETE CASCADE,
            nama      TEXT    NOT NULL,
            kategori  TEXT    NOT NULL DEFAULT 'Lainnya',
            ikon      TEXT    DEFAULT '🍽️',
            urutan    INTEGER DEFAULT 0
        )
    """)

    # ── Tabel nilai gizi ────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS gizi (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            menu_id     INTEGER NOT NULL REFERENCES menu(id) ON DELETE CASCADE,
            porsi       TEXT    NOT NULL,
            energi      REAL    DEFAULT 0,
            protein     REAL    DEFAULT 0,
            karbohidrat REAL    DEFAULT 0,
            lemak       REAL    DEFAULT 0,
            serat       REAL    DEFAULT 0,
            kalsium     REAL    DEFAULT 0
        )
    """)

    # ── Tabel statistik ─────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS statistik (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            label    TEXT    NOT NULL,
            nilai    INTEGER DEFAULT 0,
            ikon     TEXT    DEFAULT '📊',
            satuan   TEXT    DEFAULT ''
        )
    """)

    # ── Seed: statistik awal ────────────────────────────────────────────────
    if c.execute("SELECT COUNT(*) FROM statistik").fetchone()[0] == 0:
        c.executemany("INSERT INTO statistik (label, nilai, ikon, satuan) VALUES (?,?,?,?)", [
            ("Penerima Manfaat", 450,  "👨‍👩‍👧‍👦", "orang"),
            ("Jumlah Sekolah",   3,    "🏫",   "sekolah"),
            ("Jumlah Posyandu",  5,    "🏥",   "posyandu"),
        ])

    # ── Seed: menu 7 hari terakhir ──────────────────────────────────────────
    c.execute("SELECT COUNT(*) FROM menu")
    if c.fetchone()[0] == 0:
        today = date.today()
        seed_menus = [
            {
                "tanggal": str(today),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung susu sapi. Konsultasikan dengan wali kelas jika ada alergi.",
                "items": [
                    ("Nasi Putih",        "Bahan Pokok", "🍚", 1),
                    ("Ayam Bumbu Kuning", "Lauk Hewani", "🍗", 2),
                    ("Tumis Kangkung",    "Sayuran",     "🥬", 3),
                    ("Pisang Ambon",      "Buah Buahan", "🍌", 4),
                    ("Susu UHT Putih",    "Lainnya",     "🥛", 5),
                ],
                "gizi": (650, 22, 85, 18, 4, 210),
            },
            {
                "tanggal": str(today - timedelta(days=1)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung ikan.",
                "items": [
                    ("Nasi Putih",        "Bahan Pokok", "🍚", 1),
                    ("Ikan Goreng Tepung","Lauk Hewani", "🐟", 2),
                    ("Cap Cay",          "Sayuran",     "🥦", 3),
                    ("Jeruk Segar",      "Buah Buahan", "🍊", 4),
                    ("Susu UHT",         "Lainnya",     "🥛", 5),
                ],
                "gizi": (620, 20, 80, 16, 5, 200),
            },
            {
                "tanggal": str(today - timedelta(days=2)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung kedelai (tahu/tempe).",
                "items": [
                    ("Nasi Putih",        "Bahan Pokok", "🍚", 1),
                    ("Tahu Tempe Bacem",  "Lauk Nabati", "🧆", 2),
                    ("Sayur Bening Bayam","Sayuran",    "🥬", 3),
                    ("Semangka",         "Buah Buahan", "🍉", 4),
                    ("Susu UHT",         "Lainnya",     "🥛", 5),
                ],
                "gizi": (590, 18, 78, 15, 6, 195),
            },
            {
                "tanggal": str(today - timedelta(days=3)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung ayam & susu.",
                "items": [
                    ("Nasi Putih",    "Bahan Pokok", "🍚", 1),
                    ("Sop Ayam",      "Lauk Hewani", "🍲", 2),
                    ("Perkedel Jagung","Lauk Nabati", "🌽", 3),
                    ("Melon",         "Buah Buahan", "🍈", 4),
                    ("Susu UHT",      "Lainnya",     "🥛", 5),
                ],
                "gizi": (640, 21, 83, 17, 4, 205),
            },
            {
                "tanggal": str(today - timedelta(days=4)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung daging sapi & susu.",
                "items": [
                    ("Nasi Putih",    "Bahan Pokok", "🍚", 1),
                    ("Rendang Daging","Lauk Hewani", "🥩", 2),
                    ("Tumis Buncis",  "Sayuran",     "🫛", 3),
                    ("Pepaya",        "Buah Buahan", "🍈", 4),
                    ("Susu UHT",      "Lainnya",     "🥛", 5),
                ],
                "gizi": (680, 25, 86, 22, 4, 210),
            },
            {
                "tanggal": str(today - timedelta(days=5)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung telur & susu.",
                "items": [
                    ("Nasi Putih",  "Bahan Pokok", "🍚", 1),
                    ("Telur Dadar", "Lauk Hewani", "🍳", 2),
                    ("Sayur Lodeh", "Sayuran",     "🥣", 3),
                    ("Apel Merah",  "Buah Buahan", "🍎", 4),
                    ("Susu UHT",    "Lainnya",     "🥛", 5),
                ],
                "gizi": (600, 19, 79, 16, 4, 200),
            },
            {
                "tanggal": str(today - timedelta(days=6)),
                "foto": "images/menu-hari-ini.jpg",
                "alergen": "Mengandung ikan & susu.",
                "items": [
                    ("Nasi Putih",  "Bahan Pokok", "🍚", 1),
                    ("Pepes Ikan",  "Lauk Hewani", "🐠", 2),
                    ("Tumis Taoge", "Sayuran",     "🌿", 3),
                    ("Mangga",      "Buah Buahan", "🥭", 4),
                    ("Susu UHT",    "Lainnya",     "🥛", 5),
                ],
                "gizi": (610, 19, 80, 15, 5, 198),
            },
        ]

        for m in seed_menus:
            c.execute(
                "INSERT OR IGNORE INTO menu (tanggal, foto, alergen) VALUES (?, ?, ?)",
                (m["tanggal"], m["foto"], m["alergen"])
            )
            menu_id = c.lastrowid
            if menu_id:
                for item in m["items"]:
                    c.execute(
                        "INSERT INTO menu_item (menu_id, nama, kategori, ikon, urutan) VALUES (?,?,?,?,?)",
                        (menu_id, *item)
                    )
                e, p, k, l, s, ka = m["gizi"]
                c.execute(
                    "INSERT INTO gizi (menu_id, energi, protein, karbohidrat, lemak, serat, kalsium) VALUES (?,?,?,?,?,?,?)",
                    (menu_id, e, p, k, l, s, ka)
                )

    conn.commit()
    conn.close()
    print(f"[DB] Database siap: {DB_PATH}")


if __name__ == "__main__":
    init_db()
    print("[DB] Inisialisasi selesai.")
