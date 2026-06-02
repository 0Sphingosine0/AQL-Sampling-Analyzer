import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Aplikasi Analisis AQL - Kelompok 7",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────────
st.sidebar.title("📌 Navigasi")
menu = st.sidebar.radio("Pilih Halaman:", ["🏠 Opening & Profil", "📊 Dashboard & Analisis Data"])

# ─────────────────────────────────────────────
# HALAMAN 1: OPENING & PROFIL
# ─────────────────────────────────────────────
if menu == "🏠 Opening & Profil":
    
    # Header Utama
    st.title("📊 Aplikasi Sistem Analisis & Pengambilan Keputusan AQL")
    st.subheader("Optimasi Kontrol Kualitas Berdasarkan Standar Sampling")
    st.markdown("---")
    
    # 1. Pengenalan & Kegunaan Website
    st.header("✨ Tentang Website")
    st.write(
        """
        Website ini dirancang sebagai alat bantu digital untuk melakukan analisis kualitas produk menggunakan 
        metode **AQL (Acceptable Quality Limit)**. Aplikasi ini membantu industri atau tim *Quality Control (QC)* dalam menentukan apakah sebuah batch produksi layak diterima (*Accept*) atau harus ditolak (*Reject*) 
        berdasarkan sampel acak yang diambil.
        
        **Kegunaan Utama:**
        * 📉 **Otomatisasi Perhitungan:** Menghitung batas penerimaan tanpa harus melihat tabel fisik secara manual.
        * 📊 **Visualisasi Data:** Menampilkan tren kecacatan produk dalam bentuk grafik yang interaktif.
        * 💡 **Efisiensi Keputusan:** Mempercepat proses penentuan status *batch* produksi secara akurat.
        """
    )
    
    # 2. Tujuan Proyek
    st.info(
        """
        🎯 **Tujuan Pembuatan Aplikasi:**
        1. Memenuhi tugas kolaborasi kelompok pada mata kuliah terkait.
        2. Menyediakan perangkat lunak berbasis web yang intuitif untuk simulasi batas toleransi cacat produk.
        3. Mempermudah pemahaman metrik kualitas melalui visualisasi data statistik yang dinamis.
        """
    )
    
    st.markdown("---")
    
    # 3. Sumber Data (Source Data Tabel AQL)
    st.header("📂 Sumber Data (AQL Table Source)")
    st.markdown(
        """
        Data acuan Standar AQL yang digunakan dalam aplikasi ini disadur dari standar internasional:
        * **ISO 2859-1 / ANSI/ASQ Z1.4** (*Sampling Procedures and Tables for Inspection by Attributes*).
        * Tabel ini menentukan **Kode Huruf Ukuran Sampel** (Sample Size Code Letters) berdasarkan jumlah populasi (*Lot Size*) dan Tingkat Inspeksi (General/Special Inspection Levels).
        """
    )
    
    # Contoh visualisasi mini tabel referensi AQL (Bisa disesuaikan dengan isi dataframe aslimu)
    with st.expander("🔍 Lihat Referensi Ringkas Tabel Kode Huruf AQL"):
        sample_aql_data = pd.DataFrame({
            "Ukuran Lot (Populasi)": ["1 s/d 8", "9 s/d 15", "16 s/d 25", "26 s/d 50", "51 s/d 90", "91 s/d 150"],
            "Level I": ["A", "A", "B", "C", "C", "D"],
            "Level II (Standar)": ["A", "B", "C", "D", "E", "F"],
            "Level III": ["B", "C", "D", "E", "F", "G"]
        })
        st.table(sample_aql_data)

    st.markdown("---")
    
    # 4. Memperkenalkan Anggota Kelompok 7
    st.header("👥 Anggota Kelompok 7")
    st.write("Aplikasi ini dikembangkan dengan bangga oleh:")
    
    # Membuat tampilan grid/kolom yang rapi untuk nama anggota
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("👤 **1. Iren Nethania Rifai** (NPM: 2560644)")
        st.success("👤 **2. Mayang Devani Dwi Nanda** (NPM: 2560669)")
        st.success("👤 **3. Putri Anisa** (NPM: 2560737)")
        
    with col2:
        st.success("👤 **4. Shally Ardhany** (NPM: 2560778)")
        st.success("👤 **5. Shiela Feriska Demayanti** (NPM: 2560779)")

# ─────────────────────────────────────────────
# HALAMAN 2: DASHBOARD & ANALISIS (KODE LAMA ANDA)
# ─────────────────────────────────────────────
elif menu == "📊 Dashboard & Analisis Data":
    st.title("📊 Dashboard Analisis Data AQL")
    st.write("Silakan lanjutkan pengolahan data atau perhitungan grafik Anda di sini.")
    
    # --- TEMPATKAN KODE GRAFIK / DATA ANDA DI BAWAH INI ---
    # Tips Warna Kontras: Gunakan tema plotly yang aman untuk light/dark mode
    # Contoh:
    # fig = px.bar(df, x='x', y='y', template='plotly_dark' (jika ingin selalu gelap) atau biarkan default agar adaptif)
    
    st.warning("Silakan satukan fungsi visualisasi data Plotly dan DataFrame Anda pada bagian ini.")
