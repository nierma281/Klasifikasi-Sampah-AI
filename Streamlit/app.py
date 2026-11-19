import os
import streamlit as st

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "logo.png")
ADA_LOGO = os.path.exists(LOGO)

st.set_page_config(
    page_title="GoGreen AI",
    page_icon=LOGO if ADA_LOGO else "🌿",
    layout="wide"
)

if ADA_LOGO:
    st.logo(LOGO)  # logo di atas sidebar

pg = st.navigation(
    [
        st.Page("dashboard_page.py", title="Dashboard", icon="🏠", default=True),
        st.Page("pages/prediksi.py", title="Prediksi", icon="📷"),
        st.Page("pages/info_jenis_sampah.py", title="Info Sampah", icon="📚"),
        st.Page("pages/video_edukasi.py", title="Video Edukasi", icon="🎬"),
        st.Page("pages/kuis.py", title="Kuis", icon="🎯"),
        st.Page("pages/masukan.py", title="Masukan", icon="💬"),
    ],
    position="sidebar"
)

pg.run()
