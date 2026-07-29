import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
    .stApp { background-color: #F4F9F4; }

    /* Paksa teks native Streamlit (subheader, write, label) tetap gelap
       terlepas dari dark/light theme user */
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li,
    label, .stFileUploader label,
    div[data-testid="stFileUploaderFileName"],
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

    .result-card {
        padding: 1.5rem 1.8rem;
        border-radius: 14px;
        color: white !important;
        font-weight: 700;
        font-size: 1.4rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .result-organik { background: linear-gradient(135deg, #43A047, #66BB6A); }
    .result-anorganik { background: linear-gradient(135deg, #1565C0, #42A5F5); }
    .result-b3 { background: linear-gradient(135deg, #D84315, #FF7043); }

    div[data-testid="stFileUploader"] {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    div[data-testid="stFileUploaderDropzone"] {
        background-color: #F4F9F4 !important;
        border: 2px dashed #66BB6A !important;
        border-radius: 10px !important;
    }
    div[data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploaderDropzone"] small,
    div[data-testid="stFileUploaderDropzone"] p {
        color: #333333 !important;
    }
    div[data-testid="stFileUploaderDropzone"] button {
        background-color: white !important;
        color: #2E7D32 !important;
        border: 1px solid #2E7D32 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    div[data-testid="stFileUploaderDropzone"] svg {
        fill: #2E7D32 !important;
    }
    div[data-testid="stFileUploaderFile"] {
        background-color: #F4F9F4 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stFileUploaderFile"] span,
    div[data-testid="stFileUploaderFile"] small {
        color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# NAVBAR ATAS
# =========================================================
st.markdown("""
<div class="topnav">
    <div class="topnav-left">
        <div class="logo-circle">♻️</div>
        <span class="logo-text">EcoSort AI</span>
    </div>
    <div class="topnav-right">
        <div class="avatar-circle">🙂</div>
        <div class="user-info"><b>Guest</b><br>User</div>
    </div>
</div>
""", unsafe_allow_html=True)

nav1, nav2, nav3, _ = st.columns([1.1, 1.1, 1.4, 5])
with nav1:
    if st.button("🏠 Dashboard", type="secondary", use_container_width=True, key="nav_dashboard"):
        st.switch_page("dashboard_page.py")
with nav2:
    st.button("📷 Prediksi", type="primary", use_container_width=True, key="nav_prediksi")
with nav3:
    if st.button("📚 Info Sampah", type="secondary", use_container_width=True, key="nav_info"):
        st.switch_page("pages/info_jenis_sampah.py")

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero-banner">
    <h1>📷 Prediksi Jenis Sampah</h1>
    <p>Upload foto sampah, model AI akan mengklasifikasikannya secara otomatis</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    # Naik dari pages/prediksi.py -> Streamlit/ -> root repo, tempat model .h5 berada
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))   # .../Streamlit/pages
    STREAMLIT_DIR = os.path.dirname(CURRENT_DIR)                # .../Streamlit
    REPO_ROOT = os.path.dirname(STREAMLIT_DIR)                  # .../klasifikasi-sampah-ai
    MODEL_PATH = os.path.join(REPO_ROOT, "Models", "MobileNet_Klasifikasi_Sampah.h5")
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

class_names = ["Anorganik", "B3", "Organik"]
class_style = {
    "Anorganik": ("result-anorganik", "🧴"),
    "B3": ("result-b3", "☣️"),
    "Organik": ("result-organik", "🌿"),
}

# =========================================================
# UPLOAD & PREDIKSI
# =========================================================
col_upload, col_result = st.columns([1, 1.3])

with col_upload:
    st.subheader("Upload Gambar")
    uploaded_file = st.file_uploader("Pilih gambar sampah", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, use_container_width=True, caption="Gambar yang diupload")

with col_result:
    if uploaded_file is not None:
        img = image.resize((224, 224))
        img_array = np.array(img).astype("float32") / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        with st.spinner("Sedang melakukan prediksi..."):
            prediction = model.predict(img_array)

        kelas = class_names[np.argmax(prediction)]
        confidence = np.max(prediction)
        css_class, icon = class_style[kelas]

        st.subheader("Hasil Prediksi")
        st.markdown(f"""
        <div class="result-card {css_class}">
            {icon} {kelas.upper()} — {confidence*100:.2f}% yakin
        </div>
        """, unsafe_allow_html=True)

        if kelas == "B3":
            st.warning("⚠️ Sampah B3 perlu penanganan khusus, jangan dibuang sembarangan!")

        st.markdown("#### Probabilitas per Kelas")
        for i, c in enumerate(class_names):
            prob = prediction[0][i]
            st.write(f"**{c}**: {prob*100:.2f}%")
            st.progress(float(prob))
    else:
        st.info("⬅️ Upload gambar terlebih dahulu untuk melihat hasil prediksi di sini.")