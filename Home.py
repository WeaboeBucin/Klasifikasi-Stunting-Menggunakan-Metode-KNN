import streamlit as st

#background putih
st.set_page_config(
    page_title="Klasifikasi Stunting KNN",
    layout="wide"
)

st.markdown(
    """
    <h2 style="text-align:center;">
        KLASIFIKASI STUNTING MENGGUNAKAN METODE K-NEAREST NEIGHBORS (KNN)
    </h2>

    <h4 style="text-align:center;">
        (Studi Kasus: Puskesmas Tegalsiwalan Probolinggo)
    </h4>

    <h5 style="text-align:center;">
        Nuriyah Amelia Febrianti - 210411100168
    </h5>

    <hr style="height:3px;border:none;color:black;background-color:black;" />
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
        ### Tentang Aplikasi

        Aplikasi ini digunakan untuk memprediksi status **Stunting** atau **Tidak Stunting**
        menggunakan algoritma **K-Nearest Neighbors (KNN)** berdasarkan data:

        - Jenis Kelamin
        - Umur (bulan)
        - Berat Badan (kg)
        - Tinggi Badan (cm)
    """)

