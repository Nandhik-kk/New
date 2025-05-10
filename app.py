import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Pengaturan halaman
st.set_page_config(
    page_title="Aplikasi Perhitungan Kadar GC",
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
    st.title('Aplikasi Perhitungan Kadar Metode Kromatografi Gas (GC)')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gambar dan penjelasan dalam layout kolom
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Placeholder untuk gambar spektro GC
        st.image("https://via.placeholder.com/500x300?text=Gambar+Alat+Spektro+GC", 
                 caption="Alat Kromatografi Gas", use_column_width=True)
        st.info("Gambar di atas adalah alat Kromatografi Gas yang digunakan untuk analisis.")
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("Tentang Kromatografi Gas (GC)")
        st.write("""
        Kromatografi Gas adalah teknik analisis yang memisahkan senyawa berdasarkan volatilitas dan interaksi 
        dengan fase diam dan fase gerak. Metode ini digunakan secara luas untuk analisis kualitatif dan kuantitatif
        campuran senyawa yang dapat diuapkan.
        
        Komponen utama dalam sistem GC:
        - Injektor: tempat sampel dimasukkan
        - Kolom: tempat pemisahan terjadi
        - Detektor: mengukur komponen yang keluar dari kolom
        - Sistem pengolah data: merekam dan menganalisis sinyal
        
        Aplikasi ini membantu dalam perhitungan kadar berbagai senyawa menggunakan data yang diperoleh dari analisis GC.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Informasi tambahan
    st.subheader("Fitur Aplikasi")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('**Perhitungan Kadar**')
        st.write("Perhitungan otomatis berdasarkan area peak dan faktor respons")
    
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

