import os
import streamlit as st
from tema import terapkan_tema, header

terapkan_tema()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

# ====== SESUAIKAN ======
VIDEO_FILE = os.path.join(ASSETS, "video_edukasi.mp4")
VIDEO_URL = ""          # contoh: "https://www.youtube.com/watch?v=xxxx"
NARASI = os.path.join(ASSETS, "narasi.mp3")
MUSIK = os.path.join(ASSETS, "musik_latar.mp3")
# =======================

header("🎬 Video Edukasi", "Tonton cara memilah sampah dengan benar, lalu coba prediksi dan kuisnya.")

if os.path.exists(VIDEO_FILE):
    st.video(VIDEO_FILE)
elif VIDEO_URL:
    st.video(VIDEO_URL)
else:
    st.info("Video belum tersedia. Letakkan file di `assets/video_edukasi.mp4` atau isi `VIDEO_URL` pada file ini.")

c1, c2 = st.columns(2)
with c1:
    st.markdown("#### 🎧 Narasi")
    if os.path.exists(NARASI):
        st.audio(NARASI)
    else:
        st.caption("Tambahkan `assets/narasi.mp3`.")
with c2:
    st.markdown("#### 🎵 Musik latar")
    if os.path.exists(MUSIK):
        st.audio(MUSIK, loop=True)
    else:
        st.caption("Tambahkan `assets/musik_latar.mp3`.")

st.markdown('<div class="section-title">Poin penting</div>', unsafe_allow_html=True)
st.markdown('<div class="poin-box">♻️ <b>Prinsip 3R:</b> Reduce (kurangi), Reuse (pakai ulang), Recycle (daur ulang).</div>',
            unsafe_allow_html=True)
a, b, c = st.columns(3)
for col, ikon, judul, desc in [
    (a, "🍃", "Organik", "Jadikan kompos. Gunakan tempat sampah hijau."),
    (b, "♻️", "Anorganik", "Bersihkan lalu setor ke bank sampah. Tempat sampah kuning."),
    (c, "☣️", "B3", "Serahkan ke titik pengumpulan khusus. Tempat sampah merah."),
]:
    col.markdown(f'<div class="feature-box"><div class="feature-icon">{ikon}</div>'
                 f'<div class="feature-title">{judul}</div><div class="feature-desc">{desc}</div></div>',
                 unsafe_allow_html=True)

st.write("")
if st.button("Coba Prediksi Sampah", type="primary"):
    st.switch_page("pages/prediksi.py")
