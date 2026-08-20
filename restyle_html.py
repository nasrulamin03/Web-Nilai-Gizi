import re

new_html = """
    <!-- ============================================================
     NAVBAR
     ============================================================ -->
    <nav id="navbar">
        <div class="container">
            <div class="navbar-inner">
                <a href="#hero" class="nav-brand" aria-label="SPPG Kamulan 2 - Beranda">
                    <div class="nav-logo-circle">K2</div>
                    <div class="nav-brand-text">
                        <span class="nav-brand-title">SPPG Blitar Talun Kamulan 2</span>
                        <span class="nav-brand-sub">Badan Gizi Nasional</span>
                    </div>
                </a>

                <ul class="nav-links" role="navigation" aria-label="Navigasi utama">
                    <li><a href="#hero" id="nav-beranda" class="active">Beranda</a></li>
                    <li><a href="#menu" id="nav-menu">Menu Hari Ini</a></li>
                    <li><a href="#gizi" id="nav-gizi">Nilai Gizi</a></li>
                    <li><a href="#riwayat" id="nav-riwayat">Riwayat</a></li>
                    <li><a href="#tentang" id="nav-tentang">Tentang</a></li>
                    <li><a href="#footer" id="nav-kontak">Kontak</a></li>
                </ul>

                <a href="#menu" class="btn btn-primary" style="display: none;" id="navCtaDesktop">Lihat Menu Hari Ini</a>

                <button class="hamburger" id="hamburgerBtn" aria-label="Buka menu navigasi" aria-expanded="false">
                    <span></span><span></span><span></span>
                </button>
            </div>

            <div class="mobile-nav" id="mobileNav" role="navigation" aria-label="Navigasi mobile">
                <a href="#hero" onclick="closeMobileNav()">Beranda</a>
                <a href="#menu" onclick="closeMobileNav()">Menu Hari Ini</a>
                <a href="#gizi" onclick="closeMobileNav()">Nilai Gizi</a>
                <a href="#riwayat" onclick="closeMobileNav()">Riwayat Menu</a>
                <a href="#tentang" onclick="closeMobileNav()">Tentang Program</a>
                <a href="#footer" onclick="closeMobileNav()">Kontak</a>
            </div>
        </div>
    </nav>

    <!-- ============================================================
     HERO SECTION
     ============================================================ -->
    <section id="hero" aria-labelledby="hero-title">
        <div class="container hero-content">
            <div class="hero-grid">
                <!-- Left: text -->
                <div>
                    <div class="section-label reveal">PROGRAM PEMERINTAH</div>
                    <h1 class="hero-title reveal reveal-delay-1" id="hero-title">
                        Gizi Baik,<br />
                        Masa Depan <span style="color:var(--accent);">Cerah</span>
                    </h1>

                    <p class="hero-tagline reveal reveal-delay-2">
                        Menyajikan makanan bergizi, seimbang, dan aman setiap hari untuk anak-anak SPPG Blitar Talun Kamulan 2.
                    </p>

                    <div class="hero-cta reveal reveal-delay-3">
                        <a href="#menu" class="btn btn-primary" id="heroMenuBtn">
                            Lihat Menu Hari Ini
                        </a>
                        <a href="#tentang" class="btn btn-outline" id="heroGiziBtn">
                            Tentang Program
                        </a>
                    </div>
                    
                    <!-- 3 Badges -->
                    <div class="hero-badges reveal reveal-delay-4" style="display:flex; gap:1.5rem; margin-top:2.5rem; flex-wrap:wrap;">
                        <div style="display:flex; align-items:center; gap:0.5rem;">
                            <div style="background:rgba(255,255,255,0.8); border-radius:50%; width:40px; height:40px; display:flex; align-items:center; justify-content:center; color:var(--primary); font-size:1.2rem;">📅</div>
                            <div>
                                <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600; text-transform:uppercase;">Tanggal</div>
                                <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;" id="heroDateDisplay">Memuat...</div>
                            </div>
                        </div>
                        <div style="display:flex; align-items:center; gap:0.5rem;">
                            <div style="background:rgba(255,255,255,0.8); border-radius:50%; width:40px; height:40px; display:flex; align-items:center; justify-content:center; color:var(--primary); font-size:1.2rem;">🍽️</div>
                            <div>
                                <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600; text-transform:uppercase;">Program</div>
                                <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;">Makan Bergizi</div>
                            </div>
                        </div>
                        <div style="display:flex; align-items:center; gap:0.5rem;">
                            <div style="background:rgba(255,255,255,0.8); border-radius:50%; width:40px; height:40px; display:flex; align-items:center; justify-content:center; color:var(--primary); font-size:1.2rem;">🏛️</div>
                            <div>
                                <div style="font-size:0.75rem; color:var(--text-muted); font-weight:600; text-transform:uppercase;">Standar</div>
                                <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;">BGN Terverifikasi</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right: photo -->
                <div class="hero-visual reveal reveal-delay-3">
                    <div class="hero-img-wrapper" style="border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; box-shadow:0 20px 40px rgba(15, 42, 82, 0.1);">
                        <img src="images/menu-hari-ini.jpg"
                            alt="Foto menu makan siang MBG: nasi, ayam bumbu kuning, tumis kangkung, pisang, dan susu"
                            loading="lazy"
                            onerror="this.src='https://placehold.co/600x450/0F2A52/F5B301?text=Menu+Hari+Ini'" />
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
     MENU HARI INI
     ============================================================ -->
    <section id="menu" aria-labelledby="menu-title" style="background: var(--bg-white);">
        <div class="container">
            <div class="reveal text-center" style="text-align: center;">
                <div class="section-label">HARI INI</div>
                <h2 class="section-title" id="menu-title">Menu Makanan & Gizi</h2>
                <p class="section-subtitle" id="menuDateSubtitle" style="margin-bottom:3rem;">Memuat data menu…</p>
            </div>

            <div class="menu-grid">
                <!-- Foto menu -->
                <div class="menu-photo-card reveal reveal-delay-1" style="border-radius: var(--radius-xl); overflow: hidden; box-shadow: var(--card-shadow);">
                    <img src="images/menu-hari-ini.jpg" alt="Foto menu makan siang program MBG SPPG Kamulan 2"
                        loading="lazy" onerror="this.src='https://placehold.co/600x450/0F2A52/F5B301?text=Foto+Menu'" />
                </div>

                <!-- Daftar menu -->
                <div class="menu-list-section">
                    <div class="menu-list-header reveal reveal-delay-1" style="margin-bottom:1.5rem;">
                        <h3 style="font-size:1.4rem; color:var(--primary-dark); margin-bottom:0.25rem;">Komposisi Menu</h3>
                        <p style="font-size:0.95rem; color:var(--text-muted);">Disiapkan oleh Tim Dapur SPPG Kamulan 2
                        </p>
                    </div>
                    <ul id="menuItemList" aria-label="Daftar item menu hari ini" style="display:flex; flex-direction:column; gap:0.75rem;">
                        <!-- Diisi oleh JavaScript -->
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
     NILAI GIZI
     ============================================================ -->
    <section id="gizi" aria-labelledby="gizi-title" style="background: var(--bg-pale); padding: 4rem 0;">
        <div class="container">
            <div class="reveal text-center" style="text-align:center; max-width:600px; margin:0 auto 3rem auto;">
                <div class="section-label">TRANSPARANSI KESEHATAN</div>
                <h2 class="section-title" id="gizi-title">Kandungan Nilai Gizi</h2>
                <p class="section-subtitle" style="margin-bottom:1.5rem;">Kandungan gizi per porsi menu hari ini yang disesuaikan dengan kebutuhan kalori harian.</p>
                <div class="gizi-public-tabs" role="tablist">
                    <button class="gizi-public-tab active" role="tab" onclick="changePublicGiziTab('Besar')">Porsi Besar</button>
                    <button class="gizi-public-tab" role="tab" onclick="changePublicGiziTab('Kecil')">Porsi Kecil</button>
                    <button class="gizi-public-tab" role="tab" onclick="changePublicGiziTab('Balita')">Porsi Balita</button>
                    <button class="gizi-public-tab" role="tab" onclick="changePublicGiziTab('Bumil')">Bumil & Busui</button>
                </div>
            </div>

            <!-- Diisi oleh JavaScript (diubah sedikit bentuk kartunya via CSS nanti) -->
            <div class="gizi-grid" id="giziGrid" role="list" aria-label="Kartu kandungan gizi" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(160px, 1fr)); gap:1.5rem;">
                
            </div>

            <div class="alergen-banner reveal" id="alergenBanner" role="alert" aria-live="polite" style="margin-top:2rem; background:rgba(245, 179, 1, 0.1); border:1px solid rgba(245, 179, 1, 0.3); border-radius:var(--radius-xl); padding:1rem 1.5rem; display:flex; gap:1rem; align-items:center;">
                <span class="alergen-icon" aria-hidden="true" style="font-size:1.5rem;">⚠️</span>
                <div>
                    <strong style="color:var(--primary-dark);">Info Alergen:</strong>
                    <span id="alergenText" style="color:var(--text-main);">Memuat informasi alergen…</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
     KENAPA MEMILIH KAMI (NEW SECTION)
     ============================================================ -->
    <section id="why-choose-us" style="background: var(--bg-white); padding: 5rem 0;">
        <div class="container">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center;">
                <div class="reveal">
                    <div class="section-label">MENGAPA SPPG KAMULAN 2</div>
                    <h2 class="section-title">Kualitas & Kebersihan Terjamin</h2>
                    <p style="color:var(--text-muted); margin-bottom:2rem;">Setiap porsi makanan yang kami sajikan telah melalui proses pemeriksaan ketat untuk memastikan pemenuhan standar gizi anak sekolah.</p>
                    
                    <div style="display:flex; flex-direction:column; gap:1.5rem;">
                        <div style="display:flex; gap:1rem;">
                            <div style="width:48px; height:48px; border-radius:50%; background:var(--bg-pale); color:var(--primary-light); display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:1.2rem;">📋</div>
                            <div>
                                <h4 style="color:var(--primary-dark); margin-bottom:0.25rem;">Menu Terstandar BGN</h4>
                                <p style="font-size:0.9rem; color:var(--text-muted);">Sesuai dengan pedoman gizi seimbang dari Kemenkes RI dan Badan Gizi Nasional.</p>
                            </div>
                        </div>
                        <div style="display:flex; gap:1rem;">
                            <div style="width:48px; height:48px; border-radius:50%; background:var(--bg-pale); color:var(--primary-light); display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:1.2rem;">👁️</div>
                            <div>
                                <h4 style="color:var(--primary-dark); margin-bottom:0.25rem;">Transparan & Terbuka</h4>
                                <p style="font-size:0.9rem; color:var(--text-muted);">Informasi komposisi bahan dan nilai gizi harian dapat diakses oleh publik setiap saat.</p>
                            </div>
                        </div>
                        <div style="display:flex; gap:1rem;">
                            <div style="width:48px; height:48px; border-radius:50%; background:var(--bg-pale); color:var(--primary-light); display:flex; align-items:center; justify-content:center; flex-shrink:0; font-size:1.2rem;">👨‍⚕️</div>
                            <div>
                                <h4 style="color:var(--primary-dark); margin-bottom:0.25rem;">Diawasi Ahli Gizi</h4>
                                <p style="font-size:0.9rem; color:var(--text-muted);">Menu disusun dan dipantau secara berkala oleh tenaga gizi profesional.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="reveal reveal-delay-2" style="position:relative;">
                    <img src="https://placehold.co/600x600/EAF3FB/0F2A52?text=Foto+Dapur" style="border-radius:var(--radius-2xl); box-shadow:var(--card-shadow); width:100%; object-fit:cover; aspect-ratio:1/1;" alt="Dapur Bersih">
                    <div style="position:absolute; bottom:-1.5rem; right:-1.5rem; background:white; padding:1.5rem; border-radius:var(--radius-xl); box-shadow:var(--card-shadow); max-width:200px;">
                        <h4 style="color:var(--primary-dark); margin-bottom:0.5rem; font-size:1rem;">Dapur Bersih</h4>
                        <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.4;">Proses pengolahan terpantau dengan standar higienis tinggi.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ============================================================
     RIWAYAT MENU
     ============================================================ -->
    <section id="riwayat" aria-labelledby="riwayat-title" style="background: var(--bg-pale); padding: 5rem 0;">
        <div class="container">
            <div class="reveal text-center" style="text-align:center; margin-bottom:3rem;">
                <div class="section-label">ARSIP PROGRAM</div>
                <h2 class="section-title" id="riwayat-title">Riwayat Menu 7 Hari</h2>
                <p class="section-subtitle">Catatan historis menu program MBG.</p>
            </div>

            <div class="riwayat-grid reveal" id="riwayatGrid" role="list" aria-label="Riwayat menu 7 hari">
                <!-- Diisi oleh JavaScript -->
            </div>

            <div class="riwayat-detail" id="riwayatDetail" role="region" aria-live="polite"
                aria-label="Detail riwayat menu">
                <!-- Diisi oleh JavaScript -->
            </div>
        </div>
    </section>
    
    <!-- ============================================================
     TESTIMONI
     ============================================================ -->
    <section id="testimoni" style="background: var(--bg-white); padding: 5rem 0;">
        <div class="container">
            <div class="reveal text-center" style="text-align:center; margin-bottom:3rem;">
                <div class="section-label">KATA MEREKA</div>
                <h2 class="section-title">Testimoni Program</h2>
            </div>
            
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:2rem;">
                <div class="reveal reveal-delay-1" style="background:var(--bg-pale); padding:2rem; border-radius:var(--radius-xl);">
                    <div style="color:var(--accent); font-size:1.2rem; margin-bottom:1rem;">★★★★★</div>
                    <p style="color:var(--text-main); font-style:italic; margin-bottom:1.5rem;">"Anak-anak sangat menyukai menu makan siangnya. Gizi terjamin dan sekolah kami merasa terbantu dengan program ini."</p>
                    <div style="display:flex; align-items:center; gap:1rem;">
                        <div style="width:40px; height:40px; background:var(--primary); color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">A</div>
                        <div>
                            <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;">Ibu Anita</div>
                            <div style="font-size:0.8rem; color:var(--text-muted);">Kepala Sekolah Mitra</div>
                        </div>
                    </div>
                </div>
                
                <div class="reveal reveal-delay-2" style="background:var(--bg-pale); padding:2rem; border-radius:var(--radius-xl);">
                    <div style="color:var(--accent); font-size:1.2rem; margin-bottom:1rem;">★★★★★</div>
                    <p style="color:var(--text-main); font-style:italic; margin-bottom:1.5rem;">"Transparansi menu gizi sangat bagus. Saya sebagai orang tua jadi tenang melihat apa yang dimakan anak saya di sekolah."</p>
                    <div style="display:flex; align-items:center; gap:1rem;">
                        <div style="width:40px; height:40px; background:var(--primary); color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">B</div>
                        <div>
                            <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;">Bapak Budi</div>
                            <div style="font-size:0.8rem; color:var(--text-muted);">Perwakilan Orang Tua Wali</div>
                        </div>
                    </div>
                </div>
                
                <div class="reveal reveal-delay-3" style="background:var(--bg-pale); padding:2rem; border-radius:var(--radius-xl);">
                    <div style="color:var(--accent); font-size:1.2rem; margin-bottom:1rem;">★★★★★</div>
                    <p style="color:var(--text-main); font-style:italic; margin-bottom:1.5rem;">"Pelayanan sangat bersih dan higienis. Menunya selalu bervariasi dan tepat waktu setiap hari."</p>
                    <div style="display:flex; align-items:center; gap:1rem;">
                        <div style="width:40px; height:40px; background:var(--primary); color:white; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">D</div>
                        <div>
                            <div style="font-weight:700; color:var(--primary-dark); font-size:0.9rem;">Dinas Kesehatan</div>
                            <div style="font-size:0.8rem; color:var(--text-muted);">Tim Evaluator</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- ============================================================
     CTA BANNER
     ============================================================ -->
    <section style="padding:4rem 1rem;">
        <div class="container reveal" style="background:var(--primary-light); border-radius:var(--radius-2xl); padding:4rem 2rem; text-align:center; color:white; box-shadow:0 20px 40px rgba(47, 128, 237, 0.2);">
            <h2 style="font-size:2.2rem; font-weight:800; margin-bottom:1rem; font-family:'Poppins',sans-serif;">Pantau Menu & Gizi Anak Setiap Hari</h2>
            <p style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem; max-width:600px; margin-left:auto; margin-right:auto;">Mari dukung program Makan Bergizi Gratis untuk mewujudkan generasi emas Indonesia yang sehat dan cerdas.</p>
            <a href="#menu" class="btn btn-primary" style="background:var(--accent); color:var(--primary-dark); font-size:1rem; padding:1rem 2.5rem;">Lihat Menu Hari Ini</a>
        </div>
    </section>

    <!-- ============================================================
     FOOTER
     ============================================================ -->
    <footer id="footer" role="contentinfo" style="background:var(--primary-dark); color:rgba(255,255,255,0.8); padding:5rem 0 2rem 0;">
        <div class="container">
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(250px, 1fr)); gap:3rem; margin-bottom:4rem;">
                <!-- Brand -->
                <div>
                    <div style="display:flex; align-items:center; gap:0.75rem; margin-bottom:1.5rem;">
                        <div style="width:40px; height:40px; background:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; color:var(--primary-dark); font-weight:bold; font-size:1.2rem;">K2</div>
                        <div style="color:white; font-family:'Poppins',sans-serif; font-weight:700; font-size:1.1rem; line-height:1.2;">SPPG Blitar Talun<br>Kamulan 2</div>
                    </div>
                    <p style="font-size:0.9rem; margin-bottom:1.5rem; line-height:1.6;">Satuan Pelayanan Pemenuhan Gizi yang berkomitmen menyajikan makanan bergizi, sehat, dan terjangkau.</p>
                    <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
                        <span style="background:rgba(255,255,255,0.1); color:white; padding:0.3rem 0.7rem; border-radius:999px; font-size:0.75rem; font-weight:600;">Badan Gizi Nasional</span>
                    </div>
                </div>

                <!-- Tautan -->
                <div>
                    <h3 style="color:white; font-family:'Poppins',sans-serif; font-size:1.1rem; margin-bottom:1.5rem;">Tautan Cepat</h3>
                    <ul style="display:flex; flex-direction:column; gap:0.75rem; font-size:0.95rem;">
                        <li><a href="#hero" style="color:inherit;">Beranda</a></li>
                        <li><a href="#menu" style="color:inherit;">Menu Hari Ini</a></li>
                        <li><a href="#gizi" style="color:inherit;">Kandungan Gizi</a></li>
                        <li><a href="#riwayat" style="color:inherit;">Riwayat Menu</a></li>
                    </ul>
                </div>

                <!-- Kontak -->
                <div>
                    <h3 style="color:white; font-family:'Poppins',sans-serif; font-size:1.1rem; margin-bottom:1.5rem;">Kontak Kami</h3>
                    <ul style="display:flex; flex-direction:column; gap:1rem; font-size:0.95rem;">
                        <li style="display:flex; gap:0.75rem;"><span>📍</span><span>Jl. Kamulan No. XX, Kec. Talun, Kab. Blitar</span></li>
                        <li style="display:flex; gap:0.75rem;"><span>📞</span><span>+62 812 3456 789</span></li>
                        <li style="display:flex; gap:0.75rem;"><span>✉️</span><span>sppg.kamulan2@gmail.com</span></li>
                    </ul>
                </div>

                <!-- Jam Operasional -->
                <div>
                    <h3 style="color:white; font-family:'Poppins',sans-serif; font-size:1.1rem; margin-bottom:1.5rem;">Jam Operasional</h3>
                    <ul style="display:flex; flex-direction:column; gap:1rem; font-size:0.95rem;">
                        <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:0.5rem;">
                            <span>Senin - Jumat</span>
                            <span style="color:white;">06.00 - 14.00</span>
                        </li>
                        <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:0.5rem;">
                            <span>Sabtu</span>
                            <span style="color:white;">06.00 - 10.00</span>
                        </li>
                        <li style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:0.5rem;">
                            <span>Minggu</span>
                            <span style="color:var(--accent);">Tutup</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:2rem; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; font-size:0.85rem;">
                <div>© <span id="footerYear"></span> SPPG Blitar Talun Kamulan 2. Hak cipta dilindungi.</div>
                <div>Dikelola oleh Tim SPPG · Didukung Badan Gizi Nasional</div>
            </div>
        </div>
    </footer>
"""

with open('/Users/user/Documents/WebNilaiGizi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Split based on "<!-- ============================================================
#      SCRIPTS"
parts = content.split('<!-- ============================================================\n     SCRIPTS')

if len(parts) >= 2:
    # Get everything up to <body>
    top_part = parts[0].split('<body>')[0]
    script_part = '<!-- ============================================================\n     SCRIPTS' + parts[1]
    
    final_content = top_part + '<body>\n' + new_html + '\n    ' + script_part
    with open('/Users/user/Documents/WebNilaiGizi/index.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Success replacing index.html")
else:
    print("Failed to split HTML")
