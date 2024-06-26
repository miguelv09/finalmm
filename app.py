import pandas as pd
import streamlit as st
from PIL import Image


st.title('Muestreo de Graficos')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    st.subheader('Gráfica de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)

    # Remove text input sections for temperature filtering
    # Delete the following lines:
    # min_temp_str = st.text_input('Enter minimum temperature filter (optional):', key='min_temp')
    # max_temp_str = st.text_input('Enter maximum temperature filter (optional):', key='max_temp')

    # Show the DataFrame
    st.write(df1)  # Display the entire DataFrame

else:
    st.warning('Carga un archivo CSV')
