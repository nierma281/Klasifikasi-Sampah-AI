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

    /* ===== NAVBAR ATAS ===== */
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

    /* Tombol menu navbar - reset universal */
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

    /* ===== KONTEN LAIN ===== */
    .hero-banner {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(46, 125, 50, 0.25);
    }
    .hero-banner h1 { color: white !important; font-size: 2.2rem; margin-bottom: 0.3rem; }
    .hero-banner p { color: #E8F5E9 !important; font-size: 1.05rem; margin: 0; }

    .feature-card {
        background: white;
        padding: 1.3rem;
        border-radius: 12px;
        border-left: 5px solid #2E7D32;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 0.8rem;
        height: 100%;
    }
    .feature-card h4 { margin-top: 0; color: #2E7D32 !important; }
    .feature-card p { color: #333333 !important; margin: 0; }

    .class-card {
        padding: 1rem 1.2rem;
        border-radius: 12px;
        margin-bottom: 0.7rem;
        font-weight: 600;
        color: white !important;
    }
    .class-organik { background: linear-gradient(135deg, #43A047, #66BB6A); }
    .class-anorganik { background: linear-gradient(135deg, #1565C0, #42A5F5); }
    .class-b3 { background: linear-gradient(135deg, #D84315, #FF7043); }

    div[data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
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
    st.button("🏠 Dashboard", type="primary", use_container_width=True, key="nav_dashboard")
with nav2:
    if st.button("📷 Prediksi", type="secondary", use_container_width=True, key="nav_prediksi"):
        st.switch_page("pages/prediksi.py")
with nav3:
    if st.button("📚 Info Sampah", type="secondary", use_container_width=True, key="nav_info"):
        st.switch_page("pages/info_jenis_sampah.py")

# =========================================================
# HERO BANNER
# =========================================================
st.markdown("""
<div class="hero-banner">
    <h1>♻️ Aplikasi Klasifikasi Sampah</h1>
    <p>Identifikasi jenis sampah otomatis menggunakan Deep Learning (CNN - Transfer Learning)</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FITUR APLIKASI
# =========================================================
st.subheader("✨ Fitur Aplikasi")

f1, f2, f3, f4 = st.columns(4)
with f1:
    st.markdown("""<div class="feature-card"><h4>📷 Upload Gambar</h4><p>Upload foto sampah untuk dianalisis</p></div>""", unsafe_allow_html=True)
with f2:
    st.markdown("""<div class="feature-card"><h4>🤖 Prediksi AI</h4><p>Klasifikasi otomatis pakai model CNN</p></div>""", unsafe_allow_html=True)
with f3:
    st.markdown("""<div class="feature-card"><h4>📊 Confidence Score</h4><p>Tingkat keyakinan tiap prediksi</p></div>""", unsafe_allow_html=True)
with f4:
    st.markdown("""<div class="feature-card"><h4>📚 Edukasi</h4><p>Info lengkap jenis-jenis sampah</p></div>""", unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Jumlah Kelas", "3", help="Organik, Anorganik, B3")
with col2:
    st.metric("Model", "MobileNet")
with col3:
    st.metric("Framework", "TensorFlow")

st.divider()

st.subheader("🗂️ Kategori Sampah")
st.markdown("""
<div class="class-card class-organik">🌿 ORGANIK — sisa makanan, daun, bahan alami terurai</div>
<div class="class-card class-anorganik">🧴 ANORGANIK — plastik, kaca, logam, kertas</div>
<div class="class-card class-b3">☣️ B3 — baterai, limbah medis, bahan kimia berbahaya</div>
""", unsafe_allow_html=True)

st.caption("Model dikembangkan menggunakan TensorFlow dan Streamlit.")