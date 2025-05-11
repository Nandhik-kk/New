import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Pengaturan halaman
st.set_page_config(
    page_title="Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS untuk tampilan cerah
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #0066cc;
    }
    .stButton button {
        background-color: #0066cc;
        color: white;
    }
    .info-box {
        background-color: #e6f2ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        margin-bottom: 20px;
    }
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi untuk setiap halaman
def homepage():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.title('Aplikasi Perhitungan Kadar Metode Spektrofotometri UV-Vis')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gambar dan penjelasan dalam layout kolom
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Placeholder untuk gambar spektro GC
        st.image("https://lsi.fleischhacker-asia.biz/wp-content/uploads/2022/05/Spektrofotometer-UV-VIS-Fungsi-Prinsip-Kerja-dan-Cara-Kerjanya.jpg", 
                 caption="Alat Spektrofotometer", use_container_width=True)
        st.info("Gambar di atas adalah alat Spektrofotometer yang digunakan untuk analisis.")
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Tentang Spektrofotometri UV-Vis")
        st.write("""
        Spektrofotometri UV-Vis adalah teknik analisis yang digunakan untuk mengukur absorbansi suatu senyawa
        terhadap cahaya ultraviolet (UV) dan cahaya tampak (visible/Vis). Teknik ini dimanfaatkan secara luas
        untuk analisis kualitatif dan kuantitatif senyawa berdasarkan interaksi cahaya dengan molekul dalam sampel.
        
        Komponen utama dalam sistem Spektrofotometer UV-Vis:
        - Sumber cahaya: menghasilkan cahaya UV dan Vis (biasanya deuterium untuk UV dan tungsten untuk Vis)
        - Monokromator: memisahkan panjang gelombang cahaya agar hanya satu panjang gelombang yang mengenai sampel
        - Kuvet: wadah tempat sampel diletakkan
        - Detektor: menangkap cahaya yang keluar dari sampel dan mengubahnya menjadi sinyal listrik
        
        Aplikasi ini membantu dalam menentukan konsentrasi senyawa berdasarkan hukum Lambert-Beer menggunakan data absorbansi yang diperoleh dari hasil analisis UV-Vis.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Informasi tambahan
    st.subheader("Fitur Aplikasi")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('**Perhitungan Kadar**')
        st.write("Perhitungan otomatis berdasarkan nilai absorbansinya")
    
    with col2:
        st.markdown('**Visualisasi Data**')
        st.write("Grafik dan visualisasi hasil analisis")
    
    with col3:
        st.markdown('**Laporan Hasil**')
        st.write("Eksport hasil analisis dalam berbagai format")
    
    # Footer
    st.markdown("---")
    st.markdown("© 2025 Aplikasi Perhitungan Kadar Metode Kromatografi Gas")

def blank_page(title):
    st.title(title)
    st.write("Halaman ini masih dalam pengembangan.")
    st.write("Silakan kembali ke halaman utama.")

# Sidebar untuk navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Homepage", "C Terukur", "kadar", "%RPD", "%REC"])

# Tampilkan halaman yang dipilih
if page == "Homepage":
    homepage()
elif page == "C Terukur":
    blank_page("C Terukur")
elif page == "kadar":
    blank_page("Kadar")
elif page == "%RPD":
    blank_page("%RPD")
elif page == "%REC":
    blank_page("%REC")

