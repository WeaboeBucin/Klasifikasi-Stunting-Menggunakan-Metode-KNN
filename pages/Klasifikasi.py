import streamlit as st
import pandas as pd
import joblib

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






# LOAD MODEL
model = joblib.load("model/model_knn.pkl")
scaler = joblib.load("model/scaler.pkl")


#INPUT
st.header("Input Data Balita")
st.write("Silakan masukkan data balita kemudian klik **Prediksi**.")
col1, col2 = st.columns(2)
with col1:
    jk = st.selectbox(
        "Jenis Kelamin",
        ["Laki-laki", "Perempuan"]
    )

    umur = st.number_input(
        "Umur (bulan)",
        min_value=0,
        max_value=60,
        value=24
    )

with col2:
    berat = st.number_input(
        "Berat Badan (kg)",
        min_value=1.0,
        max_value=40.0,
        value=10.0
    )

    tinggi = st.number_input(
        "Tinggi Badan (cm)",
        min_value=30.0,
        max_value=150.0,
        value=80.0
    )

# PREDIKSI
if st.button("Prediksi"):

    # Encoding JK
    jk = 1 if jk == "Laki-laki" else 0
    data = pd.DataFrame({
        "JK":[jk],
        "Umur_Bulan":[umur],
        "Berat":[berat],
        "Tinggi":[tinggi]
    })

    data_scaled = scaler.transform(data)
    hasil = model.predict(data_scaled)[0]

    st.divider()
    st.subheader("Hasil Prediksi")

    if hasil == 1:
        st.error("Balita diprediksi mengalami **Stunting**")
    else:
        st.success("Balita diprediksi **Tidak Stunting**")

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(data_scaled)[0]
        st.write("### Probabilitas")
        st.progress(float(max(prob)))
        st.write(f"Tidak Stunting : **{prob[0]*100:.2f}%**")
        st.write(f"Stunting : **{prob[1]*100:.2f}%**")
