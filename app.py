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
                 caption="Alat Spektrofotometer(PT. Laboratorium Solusi Indonesia)", use_container_width=True)
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
        st.markdown('**Perhitungan %RPD**')
        st.write("Perhitungan otomatis berdasarkan nilai kadarnya")
    
    with col3:
        st.markdown('**Perhitungan %Rec**')
        st.write("Perhitungan otomatis berdasarkan nilai kadarnya")
    
    # Footer
    st.markdown("---")
    st.markdown("© 2025 Aplikasi Perhitungan Kadar Metode Spektrofotometri UV-Vis")
# Fungsi c terukur
def c_terukur():
    st.title("Perhitungan C Terukur (UV-Vis)")

    # Pilih jumlah perhitungan
    n = st.slider("Jumlah perhitungan sampel", min_value=1, max_value=3, value=1, help="Pilih 1–3 sampel sekaligus")

    # Tempat menyimpan hasil
    results = []

    for i in range(1, n+1):
        st.markdown(f"### Sampel #{i}")
        nama = st.text_input(f"Nama Sampel #{i}", value=f"Sample {i}", key=f"nama_{i}")
        absorban = st.number_input(f"Absorbansi (A) Sampel #{i}", format="%.4f",
                                   min_value=0.0, step=0.0001, key=f"a_{i}")
        intercept = st.number_input(f"Intercept (b) Sampel #{i}", format="%.4f",
                                    min_value=0.0, step=0.0001, key=f"b_{i}")
        slope = st.number_input(f"Slope (m) Sampel #{i}", format="%.4f",
                                min_value=0.0001, step=0.0001, key=f"m_{i}")

        # Hitung segera, tapi tampilin nanti
        c_ukur = (absorban - intercept) / slope
        # Simpan nama + hasil rounded 4 desimal
        results.append((nama, round(c_ukur, 4)))

        st.markdown("---")

    # Tampilkan semua hasil
    if st.button("Hitung Semua C Terukur"):
        for nama, nilai in results:
            st.success(f"Konsentrasi/C terukur pada '{nama}' = {nilai:.4f} mg/L (ppm)")
# Fungsi Kadar
def kadar():
    st.title("Perhitungan Kadar")

    # Pilih tipe perhitungan
    tipe = st.radio("Pilih jenis perhitungan:",
                    ("A. Tanpa Bobot Sample (ppm/mg·L⁻¹)",
                     "B. Dengan Bobot Sample (mg·kg⁻¹)"))

    # Jumlah sampel (1–3)
    n = st.slider("Jumlah sampel", 1, 3, 1)

    results = []

    for i in range(1, n+1):
        st.markdown(f"---\n### Sampel #{i}")
        nama = st.text_input(f"Nama Sampel #{i}", f"Sample {i}", key=f"k_nama_{i}")

        if tipe.startswith("A"):
            # A: tanpa bobot sample
            c_ukur = st.number_input(
                f"C terukur (mg/L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_c_{i}"
            )
            blanko = st.number_input(
                f"C terukur blanko (mg/L)(koreksi) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_b_{i}"
            )
            faktor = st.number_input(
                f"Faktor Pengenceran #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_f_{i}"
            )

            nilai = (c_ukur - blanko) * faktor
            satuan = "mg/L (ppm)"

        else:
            # B: dengan bobot sample
            c_ukur = st.number_input(
                f"C terukur (mg/L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_c_{i}"
            )
            vol = st.number_input(
                f"Volume labu takar awal (L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_v_{i}"
            )
            bobot = st.number_input(
                f"Bobot sample (kg) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_w_{i}"
            )

            nilai = (c_ukur * vol) / bobot if bobot != 0 else 0.0
            satuan = "mg/kg"

        # simpan tanpa membulatkan—kita bulatkan saat tampil
        results.append((nama, nilai, satuan))

    # tombol hitung
    if st.button("Hitung Kadar"):
        st.markdown("## Hasil Perhitungan")
        for nama, nilai, satuan in results:
            st.success(f"Kadar pada '{nama}' = {nilai:.7f} {satuan}")
            
# Fungsi RPD
def rpd():
    st.title("% RPD")

    # Keterangan sebelum input
    st.markdown(
        "C1 dan C2 setiap perhitungan suatu kadar berbeda-beda, "
        "tergantung metode yang digunakan saat preparasi."
    )

    # Input C1 & C2
    c1 = st.number_input(
        "Masukkan C1", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c1"
    )
    c2 = st.number_input(
        "Masukkan C2", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c2"
    )

    # Hitung
    if st.button("Hitung %RPD"):
        # Numerator = |C1 - C2|
        num = abs(c1 - c2)
        # Denominator = rata-rata (C1 + C2)/2
        den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1  # hindari div/0
        rpd_val = num / den * 100

        # Tampilkan hasil dengan 7 desimal
        st.success(f"%RPD = {rpd_val:.7f} %")

        # Keterangan batas 5%
        if rpd_val < 5:
            st.info("Hasil oke")
        else:
            st.warning("Hasil tidak oke")
# Fungsi REC
def rec():
    st.title("% REC")

    # Keterangan sebelum input
    st.markdown(
        "C1, C2, dan C3 setiap perhitungan suatu kadar berbeda-beda, "
        "tergantung metode yang digunakan saat preparasi!"
    )

    # Input C1, C2 & C3
    c1 = st.number_input(
        "Masukkan C1", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c1"
    )
    c2 = st.number_input(
        "Masukkan C2", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c2"
    )
    c3 = st.number_input(
        "Masukkan C3", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c3"
    )

    # Hitung
    if st.button("Hitung %REC"):
        # Rumus: (C3 - C1) / C2 * 100
        den = c2 if c2 != 0 else 1
        rec_val = (c3 - c1) / den * 100

        # Tampilkan hasil dengan 7 desimal
        st.success(f"%REC = {rec_val:.7f} %")

        # Keterangan rentang 80–120%
        if 80 <= rec_val <= 120:
            st.info("Hasil oke")
        else:
            st.warning("Hasil tidak oke")


# fungsi contoh
def contoh():
    st.title("Contoh Nilai C1, C2, dan C3")

    st.markdown("""
    ### Penjelasan Singkat:
    - **C1**: Konsentrasi awal sebelum proses preparasi/pelarutan.
    - **C2**: Konsentrasi target/teoritis yang ingin dicapai.
    - **C3**: Hasil pengukuran dari sampel setelah diproses/preparasi.

    Setiap nilai bisa berbeda tergantung jenis sampel, metode preparasi, dan tahap pengujian.
    """)

    contoh_opsi = st.selectbox(
        "Pilih jenis contoh perhitungan",
        ("Pilih", "Contoh %RPD", "Contoh %REC")
    )

    if contoh_opsi == "Contoh %RPD":
        st.subheader("Contoh Nilai untuk %RPD")
        st.code("""
Misal:
C1 = 5.0000000
C2 = 4.9000000

%RPD = |5 - 4.9| / ((5 + 4.9)/2) × 100
     = 0.1 / 4.95 × 100 = 2.0202%

Hasil oke karena < 5%
        """, language="text")

    elif contoh_opsi == "Contoh %REC":
        st.subheader("Contoh Nilai untuk %REC")
        st.code("""
Misal:
C1 = 2.0000000
C2 = 2.0000000
C3 = 3.8000000

%REC = (C3 - C1) / C2 × 100
     = (3.8 - 2) / 2 × 100 = 90.0000%

Hasil oke karena berada dalam rentang 80–120%
        """, language="text")

# --- Fungsi placeholder ---
def blank_page(title):
    st.title(title)
    st.write("Sedang dikembangkan…")

# --- Sidebar & Routing ---
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Homepage", "C Terukur", "kadar", "%RPD", "%REC","CONTOH"])

if page == "Homepage":
    homepage()
elif page == "C Terukur":
    c_terukur()
elif page == "kadar":
    kadar()
elif page == "%RPD":
    rpd()
elif page == "%REC":
    rec()
elif page == "CONTOH:
    contoh()

