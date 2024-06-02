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

    # Remove "Estadísticos básicos de los sensores" section
    # Comment out or delete the following lines:
    # st.subheader('Estadísticos básicos de los sensores.')
    # st.dataframe(df1["temperatura ESP32"].describe())

    # Alternative filtering methods (consider user feedback):
    # 1. Text input for specific temperature values:
    min_temp_str = st.text_input('Enter minimum temperature filter (optional):', key='min_temp')
    max_temp_str = st.text_input('Enter maximum temperature filter (optional):', key='max_temp')

    # 2. Dropdown menus for pre-defined temperature ranges (optional):
    # temperature_ranges = [('All Data', None, None), ('Low (-10°C to 15°C)', -10, 15), ('Medium (15°C to 30°C)', 15, 30), ('High (30°C to 45°C)', 30, 45)]
    # selected_range = st.selectbox('Select temperature range (optional):', temperature_ranges)
    # min_temp, max_temp = selected_range[1:]  # Extract min/max from selected tuple

    # Apply filters based on user input:
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
