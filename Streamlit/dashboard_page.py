import streamlit as st
import os

# =========================================================
# CUSTOM CSS - TEMA TEAL/EMERALD, GAYA LANDING PAGE
# =========================================================
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }

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
        margin-bottom: 0;
    }
    .topnav-left { display: flex; align-items: center; gap: 0.6rem; }
    .logo-circle {
        width: 40px; height: 40px; border-radius: 10px;
        background: #CCFBF1;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.3rem;
    }
    .logo-text { font-size: 1.25rem; font-weight: 800; color:  #14B8A6 !important; }

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
        color: #334155 !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover,
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        color: #0F766E !important;
    }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"],
    .stButton > button[data-testid="baseButton-primary"] {
        background-color: #14B8A6 !important;
        color: white !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover,
    .stButton > button[data-testid="baseButton-primary"]:hover {
        background-color: #0F766E !important;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        color: #14B8A6 !important;
        margin-bottom: 0.8rem;
    }
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1E293B !important;
        margin-bottom: 0.6rem;
    }
    .hero-desc {
        font-size: 1rem;
        color: #64748B !important;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    div[data-testid="stImage"] img {
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }

    /* Sejajarkan (vertical align center) kolom teks & gambar di hero */
    .st-key-hero_row div[data-testid="stHorizontalBlock"] {
        align-items: center !important;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #1E293B !important;
        text-align: center;
        margin: 3rem 0 2rem 0;
    }
    .step-icon-box {
        background: #99F6E4;
        border-radius: 16px;
        width: 90px; height: 90px;
        display: flex; align-items: center; justify-content: center;
        font-size: 2.2rem;
        margin-bottom: 1rem;
    }
    .step-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: #1E293B !important;
        margin-bottom: 0.4rem;
    }
    .step-desc {
        color: #64748B !important;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .feature-box {
        border: 1.5px solid #99F6E4;
        border-radius: 14px;
        padding: 1.8rem;
        height: 100%;
    }
    .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 1rem;
        color: #14B8A6 !important;
    }
    .feature-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: #1E293B !important;
        margin-bottom: 0.5rem;
    }
    .feature-desc {
        color: #64748B !important;
        font-size: 0.92rem;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGO / BRANDING
# =========================================================

st.markdown("""
<div class="topnav">
    <div class="topnav-left">
        <div class="logo-circle">🌿</div>
        <span class="logo-text">GoGreen AI</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.write("")
st.write("")

# =========================================================
# HERO SECTION
# =========================================================
hero_container = st.container(key="hero_row")
with hero_container:
    col_text, col_visual = st.columns([1.1, 1])

with col_text:
    st.markdown('<div class="hero-title">Klasifikasi<br>Sampah</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Klasifikasi sampah 3 jenis dengan Deep Learning End-to-End.</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-desc">
    Aplikasi yang mengintegrasikan model CNN (Transfer Learning) untuk mengklasifikasikan
    sampah menjadi Organik, Anorganik, dan B3 secara otomatis bagi pengguna.
    </div>
    """, unsafe_allow_html=True)
    if st.button("Mulai Sekarang", type="primary", key="hero_cta"):
        st.switch_page("pages/prediksi.py")

with col_visual:
    IMAGE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(IMAGE_DIR, "assets", "hero_waste.jpg")
    if os.path.exists(IMAGE_PATH):
        st.image(IMAGE_PATH, use_container_width=True)
    else:
        st.markdown("""
        <div style="background:#F0FDFA; border:2px dashed #99F6E4; border-radius:20px;
                    min-height:240px; display:flex; align-items:center; justify-content:center;
                    text-align:center; padding:1.5rem;">
            <div>
                <div style="font-size:2.5rem;">🖼️</div>
                <p style="color:#64748B !important; font-size:0.9rem; margin-top:0.5rem;">
                    Taruh foto ilustrasi sampah/daur ulang di<br>
                    <code>assets/hero_waste.jpg</code><br>
                    (sejajar dengan file ini) untuk tampil di sini.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# CARA MENGGUNAKAN
# =========================================================
st.markdown('<div class="section-title">Bagaimana cara menggunakannya?</div>', unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("""
    <div class="step-icon-box">🖼️</div>
    <div class="step-title">1. Pilih Gambar</div>
    <div class="step-desc">Pilih gambar sampah yang ingin diklasifikasikan.</div>
    """, unsafe_allow_html=True)
with s2:
    st.markdown("""
    <div class="step-icon-box">🤖</div>
    <div class="step-title">2. Klasifikasikan</div>
    <div class="step-desc">Model CNN akan mengklasifikasikan sampah berdasarkan 3 jenis kategori.</div>
    """, unsafe_allow_html=True)
with s3:
    st.markdown("""
    <div class="step-icon-box">📊</div>
    <div class="step-title">3. Hasil Klasifikasi</div>
    <div class="step-desc">Hasil klasifikasi ditampilkan berupa jenis sampah dan persentase kecocokan.</div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================================================
# KEUNGGULAN APLIKASI
# =========================================================
st.markdown('<div class="section-title">Keunggulan Aplikasi</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🗂️</div>
        <div class="feature-title">Klasifikasi 3 Jenis Sampah</div>
        <div class="feature-desc">Mengklasifikasikan sampah menjadi Organik, Anorganik, dan B3 beserta persentase kecocokan.</div>
    </div>
    """, unsafe_allow_html=True)
with f2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🙌</div>
        <div class="feature-title">Mudah Digunakan</div>
        <div class="feature-desc">Dapat digunakan siapa saja tanpa perlu memahami Machine Learning.</div>
    </div>
    """, unsafe_allow_html=True)
with f3:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🔗</div>
        <div class="feature-title">End-to-End</div>
        <div class="feature-desc">Model Machine Learning terintegrasi langsung berbasis web, tanpa perlu install Python.</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("© 2026 GoGreen AI — Waste Classification Project")