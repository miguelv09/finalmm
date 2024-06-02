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
    filtered_df = df1.copy()  # Avoid modifying original DataFrame
    if min_temp_str:
        try:
            min_temp = float(min_temp_str)
            filtered_df = filtered_df.query(f"`temperatura ESP32` > {min_temp}")
        except ValueError:
            st.error('Invalid minimum temperature value. Please enter a number.')
    if max_temp_str:
        try:
            max_temp = float(max_temp_str)
            filtered_df = filtered_df.query(f"`temperatura ESP32` < {max_temp}")
        except ValueError:
            st.error('Invalid maximum temperature value. Please enter a number.')

    # Optional filtering using dropdown menus (uncomment and adjust):
    # if selected_range[0] != 'All Data':
    #     min_temp, max_temp = selected_range[1:]
    #     filtered_df = filtered_df.query(f"`temperatura ESP32` > {min_temp} & `temperatura ESP32` < {max_temp}")

    if not filtered_df.empty:  # Check if any data remains after filtering
        st.subheader("Filtered Temperatures")
        st.write(filtered_df)
    else:
        st.warning("No data matches the specified filters.")

else:
    st.warning('Necesitas cargar un archivo csv excel.')
