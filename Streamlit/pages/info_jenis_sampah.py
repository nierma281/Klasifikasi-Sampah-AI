import streamlit as st

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }

    /* Paksa teks native Streamlit (subheader, write, caption) tetap gelap
       terlepas dari dark/light theme user */
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li,
    div[data-testid="stCaptionContainer"] {
        color: #1E293B !important;
    }

    .topnav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        padding: 1rem 1.8rem;
        border-bottom: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }
    .topnav-left { display: flex; align-items: center; gap: 0.6rem; }
    .logo-circle {
        width: 40px; height: 40px; border-radius: 10px;
        background: #CCFBF1;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.3rem;
    }
    .logo-text { font-size: 1.25rem; font-weight: 800; color:  #14B8A6 !important; }

    .hero-banner {
        background: #14B8A6;
        padding: 2rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(15, 118, 110, 0.25);
    }
    div[data-testid="stMarkdownContainer"] .hero-banner h1 { color: white !important; font-size: 1.9rem; margin-bottom: 0.3rem; }
    div[data-testid="stMarkdownContainer"] .hero-banner p { color: #CCFBF1 !important; font-size: 1rem; margin: 0; }

    .info-card {
        background: white;
        padding: 1.5rem 1.8rem;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
    }
    .info-card h3 { color: #0F766E !important; }
    .info-card p { color: #333333 !important; }

    .chip {
        display: inline-block;
        padding: 0.45rem 0.9rem;
        border-radius: 20px;
        color: white !important;
        font-weight: 600;
        margin: 0.25rem;
        font-size: 0.9rem;
    }
    .chip-organik { background: linear-gradient(135deg, #43A047, #66BB6A); }
    .chip-anorganik { background: linear-gradient(135deg, #1565C0, #42A5F5); }
    .chip-b3 { background: linear-gradient(135deg, #D84315, #FF7043); }

    /* ===== TAB REDESIGN: pill style, bukan underline default ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 6px;
        border-radius: 14px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        display: inline-flex;
        width: fit-content;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.4rem !important;
        transition: all 0.2s ease;
        border: none !important;
    }
    .stTabs [data-baseweb="tab"] p {
        color: #666666 !important;
        font-weight: 600 !important;
        margin: 0 !important;
    }
    .stTabs [aria-selected="true"] p {
        color: #0F766E !important;
    }
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }
    .stTabs [data-baseweb="tab"]:focus,
    .stTabs [data-baseweb="tab"]:focus-visible,
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }
    .stTabs [data-baseweb="tab-list"] button {
        outline: none !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGO / BRANDING
# =========================================================
st.markdown("""
<div class="topnav">
    <div class="topnav-left">
        <div class="logo-circle">📚</div>
        <span class="logo-text">Informasi Jenis Sampah</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero-banner">
    <h1>📚 Informasi Jenis Sampah</h1>
    <p>Temukan informasi lengkap mengenai jenis, contoh, dampak, dan pengolahan sampah Organik, Anorganik, dan B3.</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🌿 Organik", "🧴 Anorganik", "☣️ B3"])

with tab1:
    st.markdown("""
    <div class="info-card">
        <h3>🌿 Sampah Organik</h3>
        <p>Sampah organik adalah sampah yang berasal dari makhluk hidup, seperti tumbuhan dan hewan, serta dapat terurai secara alami oleh mikroorganisme dalam waktu yang relatif singkat. Sampah ini dapat diolah kembali menjadi produk yang bermanfaat, seperti kompos atau biogas.</p>
        <p><b>Contoh:</b></p>
        <div>
            <span class="chip chip-organik">🍃 Daun</span>
            <span class="chip chip-organik">🥬 Sayuran</span>
            <span class="chip chip-organik">🍎 Buah</span>
            <span class="chip chip-organik">🍚 Sisa Makanan</span>
            <span class="chip chip-organik">🪵 Kayu</span>
        </div>
        <p></p>
        <p><b>Dampak Negatif Sampah Organik:</b></p>
        <p>1. Menimbulkan bau tidak sedap<br> 
           2. Menjadi tempat berkembang biaknya hama dan penyakit <br>
           3. Mencemari lingkungan<br> 
           4. Menghasilkan gas metana (CH4) yang berkontribusi terhadap pemanasan global<br> 
           5. Mengganggu kebersihan dan kenyamanan lingkungan</b>
        </p> 
        <p><b>Pengolahan Sampah Organik yang Tepat:</b></p> 
        <p>1. Pisahkan dari jenis sampah lainnya<br> 
           2. Olah menjadi pupuk organik atau kompos<br>
           3. Manfaatkan sebagai bahan biogas atau pakan ternak (sesuai jenisnya)<br> 
           4. Lakukan pengolahan secara rutin untuk mengurangi timbunan sampah dan dampak pencemaran<br> 
        </p>

    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="info-card">
        <h3>🧴 Sampah Anorganik</h3>
        <p>Sampah anorganik merupakan jenis sampah yang berassal dari bahan-bahan nonhayati, baik berupa produk sintesis maupun hasil proses teknologi pengolahan bahan tambang. Sampah Anorganik sulit atau butuh waktu lama untuk terurai secara alami,
        namun banyak yang bisa didaur ulang.</p>
        <p><b>Contoh:</b></p>
        <div>
            <span class="chip chip-anorganik">🍾 Styrofoam</span>
            <span class="chip chip-anorganik">🍾 Tekstil</span>
            <span class="chip chip-anorganik">🍾 Plastik</span>
            <span class="chip chip-anorganik"> Karet</span>
            <span class="chip chip-anorganik">🥫 Aluminium</span>
            <span class="chip chip-anorganik">🪟 Kaca</span>
            <span class="chip chip-anorganik">📦 Kardus</span>
            <span class="chip chip-anorganik">📄 Kertas</span>
        </div>
        <p></p>
        <p><b>Dampak Negatif Sampah Anorganik:</b></p>
        <p>1. Pencemaran Lingkungan <br> 
           2. Penyumbatan Saluran Air <br>
           3. Mengganggu Estetika <br> 
           4. Menimbulkan Penyakit (Pernapasan, Penyakit kulit, Kanker) <br> 
           5. Mengancam Kehidupan Satwa</b>
           6. Meningkatkan Emisi Gas Rumah Kaca
        </p>
        <p><b>Pengolahan Sampah Anorganik yang Tepat:</b></p> 
        <p>1. Menerapkan 3R (Reduce, Reuse, Recycle) <br> 
           2. Memilah Sampah <br>
           3. Pengelolaan Sampah yang Baik <br> 
           4. Peningkatan kesadaran masyarakat<br> 
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="info-card">
        <h3>☣️ Sampah B3</h3>
        <p>Sampah B3 (Bahan Berbahaya dan Beracun) adalah sampah yang mengandung zat, energi, atau komponen berbahaya yang dapat membahayakan kesehatan manusia dan mencemari lingkungan apabila tidak dikelola dengan benar. Sampah ini memerlukan penanganan dan pengolahan khusus sesuai dengan ketentuan yang berlaku.</p>
        <p><b>Contoh:</b></p>
        <div>
            <span class="chip chip-b3">🔋 Baterai</span>
            <span class="chip chip-b3">💡 Lampu</span>
            <span class="chip chip-b3">🎨 Cat</span>
            <span class="chip chip-b3">🛢️ Oli Bekas</span>
            <span class="chip chip-b3">💊 Obat Kadaluarsa</span>
        </div>
        <p></p>
        <p><b>Dampak Negatif Sampah B3:</b></p>
        <p>1. Pencemaran lingkungan <br> 
           2. Berbahaya bagi kesehatan manusia karena mengandung zat beracun <br>
           3. Mengancam kehidupan satwa & merusak ekosisten <br> 
           4. Menyebabkan kebakaran atau ledakan jita tidak dikelola dengan benar<br> 
        </p>
        <p><b>Pengolahan Sampah B3 yang Tepat:</b></p> 
        <p>1. Pisahkan dari sampah lainnya <br> 
           2. Simpan dalam wadah khusus yang aman <br>
           3. Jangan dibakar atau dibuang sembarangan<br> 
           4. Serahkan ke fasilitas pengolahan limbah B3 yang berizin<br>
           5. Olah menggunakan metode khusus sesuai limbahnya.<br> 
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.warning("⚠️ Jangan membuang sampah B3 sembarangan. Serahkan ke fasilitas pengolahan limbah B3 resmi.")