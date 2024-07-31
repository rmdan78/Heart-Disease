import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title("Form Input Prediksi Penyakit Jantung")

# Form for input
with st.form(key='heart_disease_form'):
    # Age of the patient
    age = st.number_input("Usia Pasien (tahun)", min_value=0, max_value=120, value=25, step=1)

    # Gender of the patient
    sex = st.selectbox("Jenis Kelamin Pasien", options=[0, 1], format_func=lambda x: 'Perempuan' if x == 0 else 'Laki-laki')

    # Chest pain type
    cp = st.selectbox("Tipe Nyeri Dada", options=[1, 2, 3, 4], format_func=lambda x: 
                      "Angina Tipikal" if x == 1 else 
                      "Angina Atypikal" if x == 2 else 
                      "Nyeri Non-anginal" if x == 3 else 
                      "Asimtomatik")

    # Resting blood pressure
    trestbps = st.number_input("Tekanan Darah Istirahat (mm Hg)", min_value=0, max_value=300, value=120, step=1)

    # Serum cholesterol level
    chol = st.number_input("Kadar Kolesterol Serum (mg/dl)", min_value=0, max_value=600, value=200, step=1)

    # Fasting blood sugar > 120 mg/dl
    fbs = st.selectbox("Gula Darah Puasa > 120 mg/dl", options=[0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya')

    # Resting electrocardiographic results
    restecg = st.selectbox("Hasil Elektrokardiografi Istirahat", options=[0, 1, 2], format_func=lambda x: 
                           "Normal" if x == 0 else 
                           "Abnormalitas Gelombang ST-T" if x == 1 else 
                           "Menunjukkan Probabilitas atau Definisi Hipertrofi Ventrikel Kiri")

    # Maximum heart rate achieved
    thalach = st.number_input("Detak Jantung Maksimum Tercapai", min_value=0, max_value=250, value=150, step=1)

    # Exercise induced angina
    exang = st.selectbox("Angina yang Dipicu oleh Latihan", options=[0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya')

    # Depression induced by exercise relative to rest
    oldpeak = st.number_input("Depresi yang Dipicu oleh Latihan (Relatif terhadap Istirahat)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

    # Slope of the peak exercise ST segment
    slope = st.selectbox("Kemiringan Segmen ST pada Puncak Latihan", options=[1, 2, 3], format_func=lambda x: 
                         "Meningkat" if x == 1 else 
                         "Datar" if x == 2 else 
                         "Menurun")

    # Number of major vessels colored by fluoroscopy
    ca = st.number_input("Jumlah Pembuluh Darah Utama yang Diwarnai oleh Fluoroskopi", min_value=0.0, max_value=4.0, value=0.0, step=0.1)

    # Thalassemia
    thal = st.selectbox("Thalasemia", options=[3, 6, 7], format_func=lambda x: 
                        "Normal" if x == 3 else 
                        "Cacat Tetap" if x == 6 else 
                        "Cacat Reversibel")

    # Heart disease diagnosis
    num = st.selectbox("Diagnosa Penyakit Jantung", options=[0, 1, 2, 3, 4], format_func=lambda x: 
                       "Tidak Ada Penyakit" if x == 0 else 
                       f"Penyakit Ada (Tingkat Keparahan: {x})")

    # Submit button
    submit_button = st.form_submit_button(label='Kirim')

# Handling form submission
if submit_button:
    # Create DataFrame from form input
    data = {
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal],
        'num': [num]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.write("Data yang Dimasukkan:")
    st.write(df)

    # Prediction using the loaded model
    prediction = model.predict(df)

    # Display the prediction
    st.write(f"Hasil Prediksi: {'Penyakit Jantung Ditemukan' if prediction[0] > 0 else 'Tidak Ada Penyakit Jantung'}")
