import os
import streamlit as st
import streamlit.components.v1 as components

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "logo.png")
ADA_LOGO = os.path.exists(LOGO)
# True = musik latar dimatikan otomatis di halaman Video Edukasi (supaya tidak bertabrakan dengan suara video)
MATIKAN_DI_HALAMAN_VIDEO = False
MUSIK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "musik_latar.mp3")

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

# ---------- Musik latar ----------
# Browser memblokir suara otomatis sebelum pengguna berinteraksi, jadi musik mulai
# otomatis begitu pengguna klik/ketuk di mana saja. Berlaku di seluruh halaman
# (atur MATIKAN_DI_HALAMAN_VIDEO di atas untuk mematikannya di halaman video). Pengguna bisa mematikannya lewat toggle di sidebar.
if os.path.exists(MUSIK):
    musik_on = st.sidebar.toggle("🔊 Musik latar", value=True, key="musik_on")
    if musik_on and not (MATIKAN_DI_HALAMAN_VIDEO and pg.title == "Video Edukasi"):
        st.markdown(
            '<style>[data-testid="stSidebar"] [data-testid="stAudio"]'
            '{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none;overflow:hidden}</style>',
            unsafe_allow_html=True)
        with st.sidebar:
            st.audio(MUSIK, loop=True, autoplay=True)
            components.html("""<script>
            const d = window.parent.document;
            function go(){ const a = d.querySelector('audio'); if (a) { a.volume = 0.6; a.loop = true; a.play().catch(()=>{}); } }
            go();
            ['click','keydown','touchstart'].forEach(e => d.addEventListener(e, go, {once:true}));
            </script>""", height=0)

pg.run()
