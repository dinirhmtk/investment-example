import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Viewer', page_icon='📊')
st.title('📊 Interactive Data Viewer')
# Load data
def load_data(file_path):
    return pd.read_excel(file_path)

# Memuat data pertama
st.header("Investment Sum_AJ Data")
file_path_1 = st.file_uploader("Upload the first Excel file", type=["xlsx"])
if file_path_1 is not None:
    data1 = load_data(file_path_1)
    st.write(data1)

# Memuat data kedua
st.header("Investment Sum_AJ - Additional Data")
file_path_2 = st.file_uploader("Upload the second Excel file", type=["xlsx"], key="second_file")
if file_path_2 is not None:
    data2 = load_data(file_path_2)
    st.write(data2)

# Analisis Deskriptif
if file_path_1 is not None and file_path_2 is not None:
    st.header("Descriptive Statistics for Both Datasets")
    
    st.subheader("Descriptive Statistics for First Dataset")
    st.write(data1.describe())
    
    st.subheader("Descriptive Statistics for Second Dataset")
    st.write(data2.describe())

# Visualisasi Time Series
if file_path_1 is not None:
    st.header("Time Series Analysis for First Dataset")
    data1['REPORT_DATE'] = pd.to_datetime(data1['REPORT_DATE'])
    grouped_data1 = data1.groupby('NAMA_PERUSAHAAN')
    
    st.subheader("Total Investment Over Time for Each Company (First Dataset)")
    for name, group in grouped_data1:
        st.line_chart(group.set_index('REPORT_DATE')['TOTAL KESELURUHAN INVESTASI'], width=0, height=0, use_container_width=True)

if file_path_2 is not None:
    st.header("Time Series Analysis for Second Dataset")
    data2['REPORT_DATE'] = pd.to_datetime(data2['REPORT_DATE'])
    grouped_data2 = data2.groupby('NAMA_PERUSAHAAN')
    
    st.subheader("Total Investment Over Time for Each Company (Second Dataset)")
    for name, group in grouped_data2:
        st.line_chart(group.set_index('REPORT_DATE')['TOTAL KESELURUHAN INVESTASI'], width=0, height=0, use_container_width=True)
