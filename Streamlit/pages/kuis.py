import random
import streamlit as st
from tema import terapkan_tema, header

terapkan_tema()

KUIS = [
    ("Kulit pisang termasuk jenis sampah apa?", ["Organik", "Anorganik", "B3"], "Organik"),
    ("Botol plastik bekas minuman termasuk...", ["Organik", "Anorganik", "B3"], "Anorganik"),
    ("Baterai bekas harus dibuang ke...", ["Tempat sampah biasa", "Titik pengumpulan B3", "Sungai"], "Titik pengumpulan B3"),
    ("Warna tempat sampah untuk sampah organik umumnya...", ["Hijau", "Kuning", "Merah"], "Hijau"),
    ("Lampu neon bekas termasuk...", ["Organik", "Anorganik", "B3"], "B3"),
    ("Sisa nasi dan sayur sebaiknya diolah menjadi...", ["Kompos", "Plastik daur ulang", "Bahan bakar kendaraan"], "Kompos"),
    ("Kardus bekas sebaiknya...", ["Dibakar", "Disetor ke bank sampah", "Dibuang ke selokan"], "Disetor ke bank sampah"),
    ("Gas yang dihasilkan sampah organik yang menumpuk di TPA adalah...", ["Metana", "Oksigen", "Helium"], "Metana"),
    ("Obat kedaluwarsa termasuk sampah...", ["Organik", "Anorganik", "B3"], "B3"),
    ("Prinsip 3R adalah...", ["Reduce, Reuse, Recycle", "Read, Run, Repeat", "Rest, Relax, Repeat"], "Reduce, Reuse, Recycle"),
]

def reset():
    st.session_state.q_soal = random.sample(KUIS, len(KUIS))
    st.session_state.q_i = 0
    st.session_state.q_skor = 0
    st.session_state.q_jawab = None

if "q_soal" not in st.session_state:
    reset()

header("🎯 Kuis Pilah Sampah", "Uji pemahamanmu tentang jenis sampah dan cara menanganinya.")
soal, i = st.session_state.q_soal, st.session_state.q_i

if i >= len(soal):
    skor = st.session_state.q_skor
    st.balloons()
    st.markdown(f'<div class="skor-box">Skor kamu<div class="skor-angka">{skor} / {len(soal)}</div></div>',
                unsafe_allow_html=True)
    st.write("")
    if skor >= 8:
        st.success("🌟 Hebat! Kamu sudah jago memilah sampah.")
    elif skor >= 5:
        st.info("👍 Lumayan! Pelajari lagi halaman Info Sampah untuk hasil lebih baik.")
    else:
        st.warning("🌱 Yuk belajar lagi di halaman Info Sampah dan Video Edukasi.")
    if st.button("Main lagi", type="primary"):
        reset()
        st.rerun()
else:
    tanya, opsi, benar = soal[i]
    st.progress(i / len(soal), text=f"Soal {i + 1} dari {len(soal)}")
    st.markdown(f"### {tanya}")
    if st.session_state.q_jawab is None:
        with st.container(key="kuis_opsi"):
            for o in opsi:
                if st.button(o, key=f"q{i}-{o}", use_container_width=True):
                    st.session_state.q_jawab = o
                    if o == benar:
                        st.session_state.q_skor += 1
                    st.rerun()
    else:
        if st.session_state.q_jawab == benar:
            st.success("✅ Benar!")
        else:
            st.error(f"❌ Salah. Jawaban yang benar: **{benar}**")
        if st.button("Lanjut ➡️", type="primary"):
            st.session_state.q_i += 1
            st.session_state.q_jawab = None
            st.rerun()
