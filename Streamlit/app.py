import streamlit as st

st.set_page_config(
    page_title="GoGreen AI",
    page_icon="🌿",
    layout="wide"
)

pg = st.navigation(
    [
        st.Page("dashboard_page.py", title="Dashboard", icon="🏠", default=True),
        st.Page("pages/prediksi.py", title="Prediksi", icon="📷"),
        st.Page("pages/info_jenis_sampah.py", title="Info Sampah", icon="📚"),
    ],
    position="sidebar"
)

pg.run()