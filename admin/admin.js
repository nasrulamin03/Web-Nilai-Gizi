/* ============================================================
   admin.js — Logic Admin Panel SPPG Kamulan 2
   ============================================================ */

'use strict';

// ── State ──────────────────────────────────────────────────────────────────
let menuItems   = [];   // item menu saat ini di form
let statsData   = [];   // data statistik dari API
let editingId   = null; // menu_id yang sedang diedit (null = mode tambah)

// ── Toast ──────────────────────────────────────────────────────────────────
function showToast(msg, type = 'success') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className   = `toast show ${type}`;
  setTimeout(() => t.classList.remove('show'), 3500);
}

// ── Halaman / Navigasi ─────────────────────────────────────────────────────
function showPage(name, linkEl) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  document.getElementById(`page-${name}`)?.classList.add('active');
  if (linkEl) linkEl.classList.add('active');

  if (name === 'dashboard')  loadDashboard();
  if (name === 'riwayat')    loadRiwayat();
  if (name === 'statistik')  loadStatistik();
  if (name === 'tambah' && !editingId) prepareFormNew();

  // Tutup sidebar di mobile
  document.getElementById('sidebar').classList.remove('open');
}

function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

// ── Auth ───────────────────────────────────────────────────────────────────
async function checkAuth() {
  try {
    const res  = await fetch('/api/admin/check');
    const data = await res.json();
    if (!data.logged_in) window.location.href = '/admin/login';
  } catch {
    window.location.href = '/admin/login';
  }
}

async function doLogout() {
  await fetch('/api/admin/logout', { method: 'POST' });
  window.location.href = '/admin/login';
}

// ── Tanggal Indonesia ──────────────────────────────────────────────────────
const HARI  = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu'];
const BULAN = ['Januari','Februari','Maret','April','Mei','Juni',
               'Juli','Agustus','September','Oktober','November','Desember'];

function formatTgl(str) {
  const d = str ? new Date(str + 'T00:00:00') : new Date();
  return `${HARI[d.getDay()]}, ${d.getDate()} ${BULAN[d.getMonth()]} ${d.getFullYear()}`;
}

function todayISO() {
  return new Date().toISOString().split('T')[0];
}

// ══════════════════════════════════════════════════════════════════════════
// DASHBOARD
// ══════════════════════════════════════════════════════════════════════════

async function loadDashboard() {
  // Set date subtitle
  const sub = document.getElementById('dashDateSub');
  if (sub) sub.textContent = formatTgl(null);

  await Promise.all([loadDashToday(), loadDashStats()]);
}

async function loadDashToday() {
  const el = document.getElementById('dashTodayContent');
  el.innerHTML = '<div class="skeleton-block" style="height:120px;"></div>';
  try {
    const res  = await fetch('/api/menu/today');
    if (!res.ok) throw new Error('Belum ada menu');
    const data = await res.json();
    el.innerHTML = renderTodayCard(data);
  } catch {
    el.innerHTML = `
      <div class="today-empty">
        <div class="empty-icon">🍽️</div>
        <div>Menu hari ini belum ditambahkan.</div>
        <button class="btn btn-primary" style="margin-top:1rem"
          onclick="showPage('tambah', document.querySelector('[data-page=tambah]'))">
          ➕ Tambah Menu Sekarang
        </button>
      </div>`;
  }
}

function renderTodayCard(data) {
  const itemsHtml = (data.menu || []).map(m => `
    <div class="today-item">
      <span class="today-item-emoji">${m.ikon}</span>
      <div>
        <div class="today-item-name">${m.nama}</div>
        <div class="today-item-cat">${m.kategori}</div>
      </div>
    </div>`).join('');

  const g = data.gizi || {};
  const giziHtml = g.energi ? `
    <div class="today-gizi-card">
      <h4>📊 Nilai Gizi</h4>
      <div class="today-gizi-row"><span>⚡ Energi</span><span>${g.energi?.nilai || 0} kkal</span></div>
      <div class="today-gizi-row"><span>💪 Protein</span><span>${g.protein?.nilai || 0} g</span></div>
      <div class="today-gizi-row"><span>🌾 Karbo</span><span>${g.karbohidrat?.nilai || 0} g</span></div>
      <div class="today-gizi-row"><span>🥑 Lemak</span><span>${g.lemak?.nilai || 0} g</span></div>
      <div class="today-gizi-row"><span>🥦 Serat</span><span>${g.serat?.nilai || 0} g</span></div>
    </div>` : '';

  return `
    <div class="today-menu-grid">
      <div>
        <div style="font-size:0.8rem; color:var(--muted); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.75rem;">
          📅 ${formatTgl(data.tanggal)}
        </div>
        <div class="today-menu-items">${itemsHtml}</div>
        ${data.alergen ? `
          <div style="margin-top:0.75rem; background:#FFF8E1; border:1.5px solid #FFC94D; border-radius:0.75rem; padding:0.65rem 1rem; font-size:0.82rem; color:#7a5200; font-weight:600;">
            ⚠️ ${data.alergen}
          </div>` : ''}
      </div>
      ${giziHtml}
    </div>`;
}

async function loadDashStats() {
  const el = document.getElementById('dashStats');
  try {
    const res  = await fetch('/api/statistik');
    statsData  = await res.json();
    el.innerHTML = statsData.map(s => `
      <div class="stat-mini">
        <div class="stat-mini-emoji">${s.ikon}</div>
        <div class="stat-mini-val">${s.nilai.toLocaleString('id-ID')}</div>
        <div class="stat-mini-lbl">${s.label}</div>
      </div>`).join('');
  } catch {
    el.innerHTML = '<div class="stat-mini"><div class="stat-mini-lbl">Gagal memuat</div></div>';
  }
}

// ══════════════════════════════════════════════════════════════════════════
// FORM TAMBAH / EDIT MENU
// ══════════════════════════════════════════════════════════════════════════

// Kategori default & emoji default
const DEFAULT_ITEMS = [
  { nama: '',  kategori: 'Bahan Pokok', ikon: '🍚' },
  { nama: '',  kategori: 'Lauk Nabati', ikon: '🥜' },
  { nama: '',  kategori: 'Lauk Hewani', ikon: '🍗' },
  { nama: '',  kategori: 'Sayuran',     ikon: '🥬' },
  { nama: '',  kategori: 'Buah Buahan', ikon: '🍌' },
];

const KATEGORI_LIST = ['Bahan Pokok','Lauk Nabati','Lauk Hewani','Sayuran','Buah Buahan','Lainnya'];

function prepareFormNew() {
  editingId = null;
  document.getElementById('menuForm').reset();
  document.getElementById('fTanggal').value = todayISO();
  menuItems = DEFAULT_ITEMS.map(i => ({...i}));
  renderMenuItemList();
}

function renderMenuItemList() {
  const list = document.getElementById('menuItemList');
  if (!list) return;
  list.innerHTML = menuItems.map((item, idx) => `
    <div class="menu-item-row" id="item-row-${idx}">
      <input class="item-emoji-inp" type="text" value="${item.ikon}"
        maxlength="4" placeholder="🍚"
        oninput="menuItems[${idx}].ikon = this.value"
        aria-label="Emoji item ${idx+1}"/>
      <input type="text" value="${item.nama}" placeholder="Nama makanan…"
        oninput="menuItems[${idx}].nama = this.value"
        required aria-label="Nama item ${idx+1}"/>
      <select class="item-kat-sel"
        onchange="menuItems[${idx}].kategori = this.value"
        aria-label="Kategori item ${idx+1}">
        ${KATEGORI_LIST.map(k => `<option value="${k}" ${k===item.kategori?'selected':''}>${k}</option>`).join('')}
      </select>
      <span style="font-size:0.72rem; color:var(--muted); font-weight:700; text-align:center; padding:0 0.25rem;">#${idx+1}</span>
      <button type="button" class="item-del-btn"
        onclick="removeMenuItem(${idx})"
        aria-label="Hapus item ${idx+1}">×</button>
    </div>`).join('');
}

function addMenuItem() {
  menuItems.push({ nama: '', kategori: 'Lainnya', ikon: '🍽️' });
  renderMenuItemList();
}

function removeMenuItem(idx) {
  if (menuItems.length <= 1) { showToast('Minimal 1 item menu!', 'error'); return; }
  menuItems.splice(idx, 1);
  renderMenuItemList();
}


// Submit form
async function submitMenu(e) {
  e.preventDefault();
  const btn     = document.getElementById('submitBtn');
  const btnText = btn.querySelector('.btn-text');
  const btnSpin = btn.querySelector('.btn-spinner');

  // Validasi item
  const validItems = menuItems.filter(i => i.nama.trim());
  if (validItems.length === 0) {
    showToast('⚠️ Minimal isi 1 nama item menu!', 'error');
    return;
  }

  btn.disabled = true;
  btnText.style.display = 'none';
  btnSpin.style.display = 'inline';

  try {
    const fotoUrl = 'images/menu-hari-ini.jpg';

    const payload = {
      tanggal:     document.getElementById('fTanggal').value,
      foto:        fotoUrl,
      alergen:     document.getElementById('fAlergen').value.trim(),
      catatan:     document.getElementById('fCatatan').value.trim(),
      menu:        validItems,
      gizi: {
        Balita: {
          energi:      parseFloat(document.getElementById('gEnergi_Balita').value)   || 0,
          protein:     parseFloat(document.getElementById('gProtein_Balita').value)   || 0,
          karbohidrat: parseFloat(document.getElementById('gKarbo_Balita').value)     || 0,
          lemak:       parseFloat(document.getElementById('gLemak_Balita').value)     || 0,
          serat:       parseFloat(document.getElementById('gSerat_Balita').value)     || 0,
        },
        Kecil: {
          energi:      parseFloat(document.getElementById('gEnergi_Kecil').value)   || 0,
          protein:     parseFloat(document.getElementById('gProtein_Kecil').value)   || 0,
          karbohidrat: parseFloat(document.getElementById('gKarbo_Kecil').value)     || 0,
          lemak:       parseFloat(document.getElementById('gLemak_Kecil').value)     || 0,
          serat:       parseFloat(document.getElementById('gSerat_Kecil').value)     || 0,
        },
        Besar: {
          energi:      parseFloat(document.getElementById('gEnergi_Besar').value)   || 0,
          protein:     parseFloat(document.getElementById('gProtein_Besar').value)   || 0,
          karbohidrat: parseFloat(document.getElementById('gKarbo_Besar').value)     || 0,
          lemak:       parseFloat(document.getElementById('gLemak_Besar').value)     || 0,
          serat:       parseFloat(document.getElementById('gSerat_Besar').value)     || 0,
        },
        Bumil: {
          energi:      parseFloat(document.getElementById('gEnergi_Bumil').value)   || 0,
          protein:     parseFloat(document.getElementById('gProtein_Bumil').value)   || 0,
          karbohidrat: parseFloat(document.getElementById('gKarbo_Bumil').value)     || 0,
          lemak:       parseFloat(document.getElementById('gLemak_Bumil').value)     || 0,
          serat:       parseFloat(document.getElementById('gSerat_Bumil').value)     || 0,
        }
      },
    };

    const res  = await fetch('/api/admin/menu', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await res.json();

    if (data.ok) {
      showToast('✅ Menu berhasil disimpan!');
      editingId = null;
      prepareFormNew();
      // Refresh dashboard jika aktif
      loadDashboard();
    } else {
      showToast('❌ Gagal: ' + (data.error || 'Error'), 'error');
    }
  } catch (err) {
    showToast('❌ Gagal menyimpan: ' + err.message, 'error');
  } finally {
    btn.disabled = false;
    btnText.style.display = '';
    btnSpin.style.display = 'none';
  }
}

function resetForm() {
  editingId = null;
  prepareFormNew();
  showToast('Form direset.', 'success');
}

// Load menu hari ini ke form (dari dashboard)
async function loadTodayForEdit() {
  try {
    const res  = await fetch('/api/menu/today');
    if (!res.ok) return;
    const data = await res.json();
    fillForm(data);
  } catch { /* ignore */ }
}

// Load menu tertentu ke form (dari riwayat)
async function loadMenuForEdit(menuId) {
  try {
    const res  = await fetch(`/api/admin/menu/${menuId}`);
    if (!res.ok) throw new Error();
    const data = await res.json();
    showPage('tambah', document.querySelector('[data-page=tambah]'));
    fillForm(data);
    editingId = menuId;
  } catch {
    showToast('Gagal memuat data menu.', 'error');
  }
}

function fillForm(data) {
  document.getElementById('fTanggal').value = data.tanggal || todayISO();
  document.getElementById('fAlergen').value = data.alergen || '';
  document.getElementById('fCatatan').value = data.catatan || '';

  // Gizi
  const portions = ['Balita', 'Kecil', 'Besar', 'Bumil'];
  portions.forEach(p => {
    const g = (data.gizi && data.gizi[p]) ? data.gizi[p] : {};
    document.getElementById(`gEnergi_${p}`).value   = g.energi?.nilai      || 0;
    document.getElementById(`gProtein_${p}`).value  = g.protein?.nilai     || 0;
    document.getElementById(`gKarbo_${p}`).value    = g.karbohidrat?.nilai || 0;
    document.getElementById(`gLemak_${p}`).value    = g.lemak?.nilai       || 0;
    document.getElementById(`gSerat_${p}`).value    = g.serat?.nilai       || 0;
  });

  // Items
  menuItems = (data.menu || []).map(i => ({
    nama:     i.nama,
    kategori: i.kategori,
    ikon:     i.ikon,
  }));
  if (menuItems.length === 0) menuItems = DEFAULT_ITEMS.map(i => ({...i}));
  renderMenuItemList();


}

// Tabs Gizi
function switchGiziTab(tabId) {
  // Hide all contents
  document.querySelectorAll('.gizi-tab-content').forEach(c => c.classList.remove('active'));
  // Show target content
  document.getElementById(`gizi-tab-${tabId}`).classList.add('active');
  
  // Update button styles
  document.querySelectorAll('.gizi-tab-btn').forEach(btn => {
    if(btn.textContent.includes(tabId) || (tabId === 'Bumil' && btn.textContent.includes('Bumil'))) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

// ══════════════════════════════════════════════════════════════════════════
// RIWAYAT
// ══════════════════════════════════════════════════════════════════════════

async function loadRiwayat() {
  const tbody = document.getElementById('riwayatBody');
  tbody.innerHTML = '<tr><td colspan="5" class="table-loading">Memuat data…</td></tr>';
  try {
    const res  = await fetch('/api/admin/menu');
    const list = await res.json();
    const today = todayISO();

    if (!list.length) {
      tbody.innerHTML = '<tr><td colspan="5" class="table-loading">Belum ada data menu.</td></tr>';
      return;
    }

    tbody.innerHTML = list.map(m => {
      const isToday = m.tanggal === today;
      const menuNames = (m.menu || []).map(i => i.nama).join(', ');
      const energi = m.gizi?.energi?.nilai || '—';
      return `
        <tr>
          <td>
            <strong>${formatTgl(m.tanggal)}</strong>
            ${isToday ? '<span class="badge-today">Hari Ini</span>' : ''}
          </td>
          <td style="max-width:280px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="${menuNames}">
            ${menuNames || '—'}
          </td>
          <td>${energi} kkal</td>
          <td style="max-width:150px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="${m.alergen}">
            ${m.alergen || '—'}
          </td>
          <td>
            <div class="table-actions">
              <button class="btn btn-sm btn-outline" onclick="loadMenuForEdit(${m.id})">✏️ Edit</button>
              <button class="btn btn-sm btn-danger"  onclick="deleteMenu(${m.id}, '${m.tanggal}')">🗑️</button>
            </div>
          </td>
        </tr>`;
    }).join('');
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="5" class="table-loading" style="color:var(--danger)">Gagal memuat: ${err.message}</td></tr>`;
  }
}

async function deleteMenu(menuId, tanggal) {
  if (!confirm(`Hapus menu tanggal ${formatTgl(tanggal)}?\nTindakan ini tidak dapat dibatalkan.`)) return;
  try {
    const res  = await fetch(`/api/admin/menu/${menuId}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.ok) {
      showToast('🗑️ Menu berhasil dihapus.');
      loadRiwayat();
    }
  } catch {
    showToast('Gagal menghapus menu.', 'error');
  }
}

// ══════════════════════════════════════════════════════════════════════════
// STATISTIK
// ══════════════════════════════════════════════════════════════════════════

async function loadStatistik() {
  const el = document.getElementById('statsForm');
  el.innerHTML = '<div class="skeleton-block" style="height:60px; margin-bottom:1rem;"></div>'.repeat(4);
  try {
    const res  = await fetch('/api/statistik');
    statsData  = await res.json();
    el.innerHTML = statsData.map(s => `
      <div class="stat-edit-row" data-stat-id="${s.id}">
        <div class="stat-edit-emoji">${s.ikon}</div>
        <div>
          <div class="stat-edit-label">${s.label}</div>
          <div class="stat-edit-sub">${s.satuan}</div>
        </div>
        <input type="number" min="0" value="${s.nilai}"
          id="stat-${s.id}"
          aria-label="Nilai ${s.label}"
          style="text-align:right; font-family:'Poppins',sans-serif; font-size:1.1rem; font-weight:700;"/>
      </div>`).join('');
  } catch {
    el.innerHTML = '<div style="color:var(--danger)">Gagal memuat statistik.</div>';
  }
}

async function saveStatistik() {
  const payload = statsData.map(s => ({
    id:    s.id,
    nilai: parseInt(document.getElementById(`stat-${s.id}`)?.value || 0, 10),
  }));
  try {
    const res  = await fetch('/api/admin/statistik', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (data.ok) showToast('✅ Statistik berhasil disimpan!');
    else showToast('Gagal menyimpan.', 'error');
  } catch {
    showToast('Gagal menyimpan statistik.', 'error');
  }
}


// ══════════════════════════════════════════════════════════════════════════
// INIT
// ══════════════════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', async () => {
  await checkAuth();
  prepareFormNew();
  loadDashboard();

});
