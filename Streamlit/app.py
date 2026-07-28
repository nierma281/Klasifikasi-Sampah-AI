import streamlit as st

st.set_page_config(
    page_title="Klasifikasi Sampah",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pg = st.navigation(
    [
        st.Page("dashboard_page.py", title="Dashboard", icon="🏠", default=True),
        st.Page("pages/prediksi.py", title="Prediksi", icon="📷"),
        st.Page("pages/info_jenis_sampah.py", title="Info Sampah", icon="📚"),
    ],
    position="hidden"  # navbar sendiri sudah dibuat manual di tiap halaman, sidebar bawaan tidak dipakai
)

pg.run()