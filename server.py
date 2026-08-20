#!/usr/bin/env python3
"""
server.py — Flask server untuk Website Nilai Gizi
SPPG Blitar Talun Kamulan 2

Jalankan: python3 server.py
Website:  http://localhost:3000
Admin:    http://localhost:3000/admin
"""

import os
import json
from datetime import date, datetime
from functools import wraps

from flask import (
    Flask, jsonify, request, session,
    send_from_directory, redirect, url_for, abort
)
from database import get_db, init_db, ADMIN_PASSWORD

# ── Setup Flask ──────────────────────────────────────────────────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
PUBLIC    = os.path.join(BASE_DIR, "public")
ADMIN_DIR = os.path.join(BASE_DIR, "admin")
UPLOAD    = os.path.join(PUBLIC, "images")

app = Flask(__name__, static_folder=None)
app.secret_key = "sppg-kamulan2-secret-2026"   # ganti di produksi
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB max upload

os.makedirs(UPLOAD, exist_ok=True)

# ══════════════════════════════════════════════════════════════════════════════
# AUTH DECORATOR
# ══════════════════════════════════════════════════════════════════════════════

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return jsonify({"error": "Unauthorized", "code": 401}), 401
    return decorated

def admin_login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect("/admin/login")
        return f(*args, **kwargs)
    return decorated

# ══════════════════════════════════════════════════════════════════════════════
# STATIC FILE SERVING
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/")
def index():
    return send_from_directory(PUBLIC, "index.html")

@app.route("/<path:filename>")
def public_files(filename):
    # Jangan izinkan akses ke admin lewat route ini
    if filename.startswith("admin"):
        abort(404)
    filepath = os.path.join(PUBLIC, filename)
    if os.path.isfile(filepath):
        return send_from_directory(PUBLIC, filename)
    abort(404)

@app.route("/admin")
@app.route("/admin/")
def admin_index():
    if not session.get("admin_logged_in"):
        return redirect("/admin/login")
    return send_from_directory(ADMIN_DIR, "index.html")

@app.route("/admin/login")
def admin_login_page():
    if session.get("admin_logged_in"):
        return redirect("/admin")
    return send_from_directory(ADMIN_DIR, "login.html")

@app.route("/admin/<path:filename>")
def admin_files(filename):
    filepath = os.path.join(ADMIN_DIR, filename)
    if os.path.isfile(filepath):
        return send_from_directory(ADMIN_DIR, filename)
    abort(404)

# ══════════════════════════════════════════════════════════════════════════════
# PUBLIC API
# ══════════════════════════════════════════════════════════════════════════════

def menu_to_dict(row, items, gizi_rows):
    """Konversi row SQLite ke dict JSON."""
    # Construct a dictionary mapping each 'porsi' to its nutritional values
    gizi_dict = {}
    if gizi_rows:
        for gr in gizi_rows:
            porsi = gr["porsi"]
            gizi_dict[porsi] = {
                "energi":      {"nilai": gr["energi"],      "satuan": "kkal"},
                "protein":     {"nilai": gr["protein"],     "satuan": "g"},
                "karbohidrat": {"nilai": gr["karbohidrat"], "satuan": "g"},
                "lemak":       {"nilai": gr["lemak"],       "satuan": "g"},
                "serat":       {"nilai": gr["serat"],       "satuan": "g"},
            }
    
    return {
        "id":       row["id"],
        "tanggal":  row["tanggal"],
        "foto":     row["foto"] or "images/menu-hari-ini.jpg",
        "alergen":  row["alergen"] or "",
        "catatan":  row["catatan"] or "",
        "menu": [
            {
                "nama":     i["nama"],
                "kategori": i["kategori"],
                "ikon":     i["ikon"],
            }
            for i in items
        ],
        "gizi": gizi_dict if gizi_dict else None,
    }


@app.route("/api/menu/today")
def api_menu_today():
    today = date.today().isoformat()
    db = get_db()
    row = db.execute("SELECT * FROM menu WHERE tanggal = ?", (today,)).fetchone()
    if not row:
        # Ambil yang paling baru jika hari ini tidak ada
        row = db.execute("SELECT * FROM menu ORDER BY tanggal DESC LIMIT 1").fetchone()
    if not row:
        db.close()
        return jsonify({"error": "Menu belum tersedia"}), 404
    items = db.execute(
        "SELECT * FROM menu_item WHERE menu_id = ? ORDER BY urutan", (row["id"],)
    ).fetchall()
    gizi_rows = db.execute("SELECT * FROM gizi WHERE menu_id = ?", (row["id"],)).fetchall()
    db.close()
    return jsonify(menu_to_dict(row, items, gizi_rows))


@app.route("/api/menu/history")
def api_menu_history():
    db = get_db()
    rows = db.execute(
        "SELECT * FROM menu ORDER BY tanggal DESC LIMIT 7"
    ).fetchall()
    result = []
    for row in rows:
        gizi = db.execute("SELECT energi FROM gizi WHERE menu_id=? AND porsi='Besar'", (row["id"],)).fetchone()
        items= db.execute(
            "SELECT ikon FROM menu_item WHERE menu_id=? ORDER BY urutan LIMIT 1", (row["id"],)
        ).fetchone()
        tgl = date.fromisoformat(row["tanggal"])
        HARI = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
        result.append({
            "id":      row["id"],
            "tanggal": row["tanggal"],
            "hari":    HARI[tgl.weekday()],
            "menu":    "",   # diisi dari items
            "energi":  gizi["energi"] if gizi else 0,
            "emoji":   items["ikon"] if items else "🍽️",
        })
    # Ambil nama menu singkat
    for i, row in enumerate(rows):
        items_rows = db.execute(
            "SELECT nama FROM menu_item WHERE menu_id=? ORDER BY urutan", (row["id"],)
        ).fetchall()
        result[i]["menu"] = ", ".join(r["nama"] for r in items_rows)
    db.close()
    return jsonify(result)


@app.route("/api/statistik")
def api_statistik():
    db = get_db()
    rows = db.execute("SELECT * FROM statistik ORDER BY id").fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])


# ══════════════════════════════════════════════════════════════════════════════
# ADMIN AUTH API
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/admin/login", methods=["POST"])
def api_admin_login():
    data = request.get_json(force=True)
    password = data.get("password", "")
    if password == ADMIN_PASSWORD:
        session["admin_logged_in"] = True
        session.permanent = True
        return jsonify({"ok": True})
    return jsonify({"ok": False, "error": "Password salah"}), 401


@app.route("/api/admin/logout", methods=["POST"])
def api_admin_logout():
    session.clear()
    return jsonify({"ok": True})


@app.route("/api/admin/check")
def api_admin_check():
    return jsonify({"logged_in": bool(session.get("admin_logged_in"))})


# ══════════════════════════════════════════════════════════════════════════════
# ADMIN MENU API
# ══════════════════════════════════════════════════════════════════════════════

def require_admin():
    if not session.get("admin_logged_in"):
        abort(401)


@app.route("/api/admin/menu", methods=["GET"])
def api_admin_menu_list():
    require_admin()
    db = get_db()
    rows = db.execute("SELECT * FROM menu ORDER BY tanggal DESC LIMIT 30").fetchall()
    result = []
    for row in rows:
        gizi  = db.execute("SELECT * FROM gizi WHERE menu_id=?", (row["id"],)).fetchone()
        items = db.execute(
            "SELECT * FROM menu_item WHERE menu_id=? ORDER BY urutan", (row["id"],)
        ).fetchall()
        result.append(menu_to_dict(row, items, gizi))
    db.close()
    return jsonify(result)


@app.route("/api/admin/menu/<int:menu_id>", methods=["GET"])
def api_admin_menu_get(menu_id):
    require_admin()
    db = get_db()
    row   = db.execute("SELECT * FROM menu WHERE id=?", (menu_id,)).fetchone()
    if not row:
        db.close()
        return jsonify({"error": "Tidak ditemukan"}), 404
    items = db.execute("SELECT * FROM menu_item WHERE menu_id=? ORDER BY urutan", (menu_id,)).fetchall()
    gizi  = db.execute("SELECT * FROM gizi WHERE menu_id=?", (menu_id,)).fetchone()
    db.close()
    return jsonify(menu_to_dict(row, items, gizi))


@app.route("/api/admin/menu", methods=["POST"])
def api_admin_menu_create():
    require_admin()
    data = request.get_json(force=True)
    tanggal     = data.get("tanggal", date.today().isoformat())
    foto        = data.get("foto", "images/menu-hari-ini.jpg")
    alergen     = data.get("alergen", "")
    catatan     = data.get("catatan", "")
    items_data  = data.get("menu", [])
    gizi_data   = data.get("gizi", {})

    db = get_db()
    try:
        # Upsert menu (update jika tanggal sudah ada)
        existing = db.execute("SELECT id FROM menu WHERE tanggal=?", (tanggal,)).fetchone()
        if existing:
            menu_id = existing["id"]
            db.execute(
                "UPDATE menu SET foto=?,alergen=?,catatan=?,updated_at=datetime('now','localtime') WHERE id=?",
                (foto, alergen, catatan, menu_id)
            )
            db.execute("DELETE FROM menu_item WHERE menu_id=?", (menu_id,))
            db.execute("DELETE FROM gizi WHERE menu_id=?", (menu_id,))
        else:
            db.execute(
                "INSERT INTO menu (tanggal, foto, alergen, catatan) VALUES (?,?,?,?)",
                (tanggal, foto, alergen, catatan)
            )
            menu_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

        # Insert items
        for idx, item in enumerate(items_data):
            db.execute(
                "INSERT INTO menu_item (menu_id, nama, kategori, ikon, urutan) VALUES (?,?,?,?,?)",
                (menu_id, item.get("nama",""), item.get("kategori","Lainnya"), item.get("ikon","🍽️"), idx+1)
            )

        # Insert gizi (gizi_data is now a dict of porsi -> nutrients)
        # e.g. {"Besar": {"energi": 100, ...}, "Kecil": {"energi": 80, ...}}
        for porsi, n_data in gizi_data.items():
            db.execute(
                "INSERT INTO gizi (menu_id, porsi, energi, protein, karbohidrat, lemak, serat, kalsium) VALUES (?,?,?,?,?,?,?,?)",
                (
                    menu_id,
                    porsi,
                    float(n_data.get("energi", 0)),
                    float(n_data.get("protein", 0)),
                    float(n_data.get("karbohidrat", 0)),
                    float(n_data.get("lemak", 0)),
                    float(n_data.get("serat", 0)),
                    float(n_data.get("kalsium", 0)),
                )
            )
        db.commit()
        db.close()
        return jsonify({"ok": True, "menu_id": menu_id})
    except Exception as e:
        db.rollback()
        db.close()
        return jsonify({"error": str(e)}), 500


@app.route("/api/admin/menu/<int:menu_id>", methods=["DELETE"])
def api_admin_menu_delete(menu_id):
    require_admin()
    db = get_db()
    db.execute("DELETE FROM menu WHERE id=?", (menu_id,))
    db.commit()
    db.close()
    return jsonify({"ok": True})


# ── Upload foto ──────────────────────────────────────────────────────────────

ALLOWED_EXT = {"jpg", "jpeg", "png", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


@app.route("/api/admin/upload", methods=["POST"])
def api_admin_upload():
    require_admin()
    if "foto" not in request.files:
        return jsonify({"error": "Tidak ada file"}), 400
    f = request.files["foto"]
    if f.filename == "" or not allowed_file(f.filename):
        return jsonify({"error": "Format tidak didukung (jpg/png/webp)"}), 400
    # Selalu simpan sebagai menu-hari-ini.jpg
    save_path = os.path.join(UPLOAD, "menu-hari-ini.jpg")
    f.save(save_path)
    return jsonify({"ok": True, "url": "images/menu-hari-ini.jpg"})


# ── Statistik ────────────────────────────────────────────────────────────────

@app.route("/api/admin/statistik", methods=["PUT"])
def api_admin_statistik_update():
    require_admin()
    data = request.get_json(force=True)  # list of {id, nilai}
    db = get_db()
    for item in data:
        db.execute("UPDATE statistik SET nilai=? WHERE id=?", (item["nilai"], item["id"]))
    db.commit()
    db.close()
    return jsonify({"ok": True})


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  SPPG Blitar Talun Kamulan 2 — Server Nilai Gizi")
    print("=" * 60)
    init_db()
    print(f"\n  🌐 Website Publik : http://localhost:3000")
    print(f"  🔐 Halaman Admin  : http://localhost:3000/admin")
    print(f"  🔑 Password Admin : {ADMIN_PASSWORD}")
    print("\n  Tekan Ctrl+C untuk menghentikan server.\n")
    app.run(host="0.0.0.0", port=3000, debug=False)
