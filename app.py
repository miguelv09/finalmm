import pandas as pd
import streamlit as st
from PIL import Image


st.title('Muestre de Graficos')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    st.subheader('Perfil gráfico de la variable medida.')
    df1 = df1.set_index('Time')
    st.line_chart(df1)
else:
    st.warning('Necesitas cargar un archivo csv excel.')
