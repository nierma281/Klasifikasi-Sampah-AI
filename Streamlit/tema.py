"""Tema bersama GoGreen AI (teal/emerald, sama dengan dashboard_page.py).
Dipakai oleh halaman baru: from tema import terapkan_tema, header
"""
import streamlit as st

CSS = """
<style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] li,
    div[data-testid="stCaptionContainer"] { color: #1E293B !important; }

    .page-head { margin: 0.5rem 0 1.5rem 0; }
    .page-title { font-size: 2.2rem; font-weight: 800; color: #14B8A6 !important; margin-bottom: .3rem; }
    .page-sub { font-size: 1rem; color: #64748B !important; }

    .stButton > button, .stDownloadButton > button, div[data-testid="stFormSubmitButton"] > button {
        border: none !important; box-shadow: none !important;
        font-weight: 600 !important; border-radius: 8px !important;
    }
    .stButton > button[kind="primary"], .stButton > button[data-testid="stBaseButton-primary"],
    div[data-testid="stFormSubmitButton"] > button, .stDownloadButton > button {
        background-color: #14B8A6 !important; color: white !important;
    }
    .stButton > button[kind="primary"]:hover, .stButton > button[data-testid="stBaseButton-primary"]:hover,
    div[data-testid="stFormSubmitButton"] > button:hover, .stDownloadButton > button:hover {
        background-color: #0F766E !important; color: white !important;
    }


    /* teks tombol utama putih (menimpa aturan warna paragraf) */
    .stButton > button[kind="primary"] p, .stButton > button[data-testid="stBaseButton-primary"] p,
    div[data-testid="stFormSubmitButton"] > button p, .stDownloadButton > button p { color: white !important; }

    .section-title { font-size: 1.5rem; font-weight: 800; color: #1E293B !important; margin: 2rem 0 1rem 0; }

    .feature-box {
        border: 1.5px solid #99F6E4; border-radius: 14px; padding: 1.5rem; height: 100%;
        background: #FFFFFF; transition: transform .2s, box-shadow .2s;
    }
    .feature-box:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(20,184,166,.18); }
    .feature-icon { font-size: 2.2rem; margin-bottom: .6rem; }
    .feature-title { font-weight: 700; font-size: 1.1rem; color: #1E293B !important; margin-bottom: .4rem; }
    .feature-desc { color: #64748B !important; font-size: .93rem; line-height: 1.5; }

    .step-icon-box { background:#99F6E4; border-radius:16px; width:90px; height:90px;
        display:flex; align-items:center; justify-content:center; font-size:2.2rem; margin-bottom:1rem; }

    .poin-box { background:#F0FDFA; border-left:6px solid #14B8A6; border-radius:10px;
        padding: 1rem 1.2rem; margin: .5rem 0 1rem 0; }

    /* Pilihan jawaban kuis: tombol outline teal */
    .st-key-kuis_opsi .stButton > button {
        background: #F0FDFA !important; color: #1E293B !important;
        border: 1.5px solid #99F6E4 !important; padding: .7rem 1rem !important; text-align: left;
    }
    .st-key-kuis_opsi .stButton > button:hover {
        border-color: #14B8A6 !important; background: #CCFBF1 !important; color: #0F766E !important;
    }
    .skor-box { text-align:center; background:#F0FDFA; border:2px solid #99F6E4; border-radius:20px; padding:2rem; }
    .skor-angka { font-size:3.5rem; font-weight:800; color:#14B8A6 !important; }
</style>
"""

def terapkan_tema():
    st.markdown(CSS, unsafe_allow_html=True)

def header(judul: str, sub: str = ""):
    st.markdown(
        f'<div class="page-head"><div class="page-title">{judul}</div>'
        f'<div class="page-sub">{sub}</div></div>', unsafe_allow_html=True)
