import streamlit as st
import pandas as pd
import base64
from datetime import datetime

# Sistem poin daur ulang
POINTS_TABLE = {
    "plastik": 10,
    "kertas": 5,
    "logam": 15,
    "kaca": 7,
    "elektronik": 20
}

# Load data dari URL GitHub
DATA_URL = "https://raw.githubusercontent.com/{username}/{repo}/main/waste_data.csv"  # Ganti!

def load_data():
    try:
        df = pd.read_csv(DATA_URL)
        return df
    except:
        return pd.DataFrame(columns=["timestamp", "username", "jenis", "berat", "poin"])

def save_data(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="waste_data.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
    return df

# Tampilan Streamlit
st.title("♻️ Bank Sampah Digital (GitHub Mode)")

# Input data
with st.form("input_form"):
    username = st.text_input("Nama Anda")
    jenis = st.selectbox("Jenis Sampah", list(POINTS_TABLE.keys()))
    berat = st.number_input("Berat (kg)", min_value=0.1, step=0.1)
    submitted = st.form_submit_button("Submit")

if submitted:
    if not username:
        st.error("Nama wajib diisi!")
    else:
        poin = berat * POINTS_TABLE[jenis]
        new_data = pd.DataFrame([{
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "username": username,
            "jenis": jenis,
            "berat": berat,
            "poin": poin
        }])
        
        df = pd.concat([load_data(), new_data])
        st.success(f"✅ Poin Anda: {poin}")
        save_data(df)

# Tampilkan data
st.header("Data Komunitas")
df = load_data()

if not df.empty:
    st.write(f"Total Sampah: {df['berat'].sum():.1f} kg")
    st.write(f"Total Poin: {df['poin'].sum():,}")
    
    st.subheader("Leaderboard")
    st.bar_chart(df.groupby("username")["poin"].sum().sort_values(ascending=False).head(5))
    
    st.write("5 Transaksi Terakhir:")
    st.table(df.tail(5))
else:
    st.info("Belum ada data")
