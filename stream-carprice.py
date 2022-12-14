import pickle
import streamlit as st

car_model = pickle.load(open('carprice_model2.sav', 'rb'))

st.title('Prediksi Harga Mobil Data Mining')

year = st.number_input('Masukan Tahun Mobil')
mileage = st.number_input('Masukan Mileage')
tax = st.number_input('Masukan Pajak Mobil')
mpg = st.number_input('Masukan rata rata kebutuhan bahan bakar')
engineSize = st.number_input('Masukan ukuran mesin')

car_predict = ''

if st.button('Prediksi'):
    car_predict = car_model.predict(
        [[year, mileage, tax, mpg, engineSize]])
    st.write('Predicted Car Price in EUR : ', car_predict)
