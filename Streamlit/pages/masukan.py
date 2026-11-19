import csv
import os
from datetime import datetime
import streamlit as st
from tema import terapkan_tema, header

terapkan_tema()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "masukan.csv")

header("💬 Tentang & Masukan", "GoGreen AI adalah media edukasi pemilahan sampah berbasis AI, dikembangkan untuk tugas UTS Sistem Multimedia.")
st.markdown("**Tim:** (isi nama anggota kelompok)")

with st.form("form_masukan", clear_on_submit=True):
    nama = st.text_input("Nama (opsional)")
    kemudahan = st.slider("Kemudahan penggunaan", 1, 5, 4)
    kemanfaatan = st.slider("Kebermanfaatan sebagai media edukasi", 1, 5, 4)
    tampilan = st.slider("Daya tarik tampilan", 1, 5, 4)
    saran = st.text_area("Saran atau kritik")
    kirim = st.form_submit_button("Kirim")

if kirim:
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    baru = not os.path.exists(DATA)
    with open(DATA, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if baru:
            w.writerow(["waktu", "nama", "kemudahan", "kemanfaatan", "tampilan", "saran"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), nama, kemudahan, kemanfaatan, tampilan, saran])
    st.success("Terima kasih atas masukanmu! 🌱")

if os.path.exists(DATA):
    with st.expander("Rekap masukan (untuk tim)"):
        with open(DATA, encoding="utf-8") as f:
            isi = f.read()
        st.text(isi)
        st.download_button("Unduh CSV", isi, file_name="masukan.csv", mime="text/csv")
