import streamlit as st

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .stApp { background-color: #F4F9F4; }

    /* Paksa teks native Streamlit (subheader, write, caption) tetap gelap
       terlepas dari dark/light theme user */
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li,
    div[data-testid="stCaptionContainer"] {
        color: #1a1a1a !important;
    }

    .topnav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        padding: 0.8rem 1.5rem;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
    }
    .topnav-left { display: flex; align-items: center; gap: 0.6rem; }
    .logo-circle {
        width: 38px; height: 38px; border-radius: 50%;
        background: linear-gradient(135deg, #2E7D32, #66BB6A);
        display: flex; align-items: center; justify-content: center;
        font-size: 1.2rem;
    }
    .logo-text { font-size: 1.3rem; font-weight: 800; color: #2E7D32 !important; }
    .topnav-right { display: flex; align-items: center; gap: 0.7rem; flex-shrink: 0; white-space: nowrap; }
    .avatar-circle {
        width: 38px; height: 38px; border-radius: 50%;
        background: #E8F5E9; display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem; border: 2px solid #66BB6A;
        flex-shrink: 0;
    }
    .user-info { font-size: 0.85rem; color: #333333 !important; line-height: 1.1; flex-shrink: 0; }
    .user-info b { color: #2E7D32 !important; }

    .stButton > button {
        border: none !important;
        box-shadow: none !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"],
    .stButton > button[data-testid="baseButton-secondary"] {
        background-color: transparent !important;
        color: #333333 !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover,
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        color: #2E7D32 !important;
        background-color: #E8F5E9 !important;
    }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"],
    .stButton > button[data-testid="baseButton-primary"] {
        background: linear-gradient(135deg, #2E7D32, #66BB6A) !important;
        color: white !important;
    }

    div[data-testid="column"] .stButton > button[kind="secondary"] {
        background-color: transparent;
        border: none;
        color: #333333 !important;
        font-weight: 600;
        box-shadow: none;
    }
    div[data-testid="column"] .stButton > button[kind="secondary"]:hover {
        color: #2E7D32 !important;
    }
    div[data-testid="column"] .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #2E7D32, #66BB6A) !important;
        border: none !important;
        color: white !important;
        font-weight: 700;
    }

    .hero-banner {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        padding: 2rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(46, 125, 50, 0.25);
    }
    .hero-banner h1 { color: white !important; font-size: 1.9rem; margin-bottom: 0.3rem; }
    .hero-banner p { color: #E8F5E9 !important; font-size: 1rem; margin: 0; }

    .info-card {
        background: white;
        padding: 1.5rem 1.8rem;
        border-radius: 14px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
    }
    .info-card h3 { color: #2E7D32 !important; }
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

    /* ===== FIX: label tab tidak kelihatan ===== */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        border-radius: 10px 10px 0 0;
        padding: 0.6rem 1.2rem;
    }
    .stTabs [data-baseweb="tab"] p {
        color: #333333 !important;
        font-weight: 600 !important;
    }
    .stTabs [aria-selected="true"] p {
        color: #2E7D32 !important;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #2E7D32 !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# NAVBAR ATAS
# =========================================================
st.markdown("""
<div class="topnav">
    <div class="topnav-left">
        <div class="logo-circle">🌿</div>
        <span class="logo-text">GoGreen AI</span>
    </div>
</div>
""", unsafe_allow_html=True)

nav1, nav2, nav3, _ = st.columns([1.1, 1.1, 1.4, 5])
with nav1:
    if st.button("🏠 Dashboard", type="secondary", use_container_width=True, key="nav_dashboard"):
        st.switch_page("dashboard_page.py")
with nav2:
    if st.button("📷 Prediksi", type="secondary", use_container_width=True, key="nav_prediksi"):
        st.switch_page("pages/prediksi.py")
with nav3:
    st.button("📚 Info Sampah", type="primary", use_container_width=True, key="nav_info")

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero-banner">
    <h1>📚 Informasi Jenis Sampah</h1>
    <p>Kenali karakteristik dan contoh masing-masing kategori sampah</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🌿 Organik", "🧴 Anorganik", "☣️ B3"])

with tab1:
    st.markdown("""
    <div class="info-card">
        <h3>🌿 Sampah Organik</h3>
        <p>Sampah organik merupakan sampah yang mudah terurai secara alami melalui proses biologis,
        sehingga dapat diolah kembali menjadi kompos.</p>
        <p><b>Contoh:</b></p>
        <div>
            <span class="chip chip-organik">🍃 Daun</span>
            <span class="chip chip-organik">🥬 Sayuran</span>
            <span class="chip chip-organik">🍎 Buah</span>
            <span class="chip chip-organik">🍚 Sisa Makanan</span>
            <span class="chip chip-organik">🪵 Kayu</span>
        </div>
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
        <p>-Pencemaran Lingkungan
           -Penyumbatan Saluran Air</p>


    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="info-card">
        <h3>☣️ Sampah B3</h3>
        <p>B3 adalah Bahan Berbahaya dan Beracun yang memerlukan penanganan khusus
        karena berisiko bagi kesehatan dan lingkungan.</p>
        <p><b>Contoh:</b></p>
        <div>
            <span class="chip chip-b3">🔋 Baterai</span>
            <span class="chip chip-b3">💡 Lampu</span>
            <span class="chip chip-b3">🎨 Cat</span>
            <span class="chip chip-b3">🛢️ Oli Bekas</span>
            <span class="chip chip-b3">💊 Obat Kadaluarsa</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.warning("⚠️ Jangan membuang sampah B3 sembarangan. Serahkan ke fasilitas pengolahan limbah B3 resmi.")