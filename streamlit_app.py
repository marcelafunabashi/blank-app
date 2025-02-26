import streamlit as st
import pandas as pd
pip install openpyxl
import openpyxl


# Load the Excel file once
@st.cache_data
def load_excel(file_path):
    return pd.ExcelFile(file_path)

# Define your file path here
file_path = 'Questions Data Wizco.xlsx'  # Update this with your actual file path

st.title("Excel Sheet Viewer")

# Load Excel file
excel_data = pd.read_excel(file_path)
sheet_names = excel_data.sheet_names  # Get all sheet names

# Dropdown to select sheet
selected_sheet = st.selectbox("Select a company", sheet_names)

# Load and display the selected sheet
if selected_sheet:
    df = pd.read_excel(file_path, sheet_name=selected_sheet)
    st.write(f"### {selected_sheet} Data")
    st.dataframe(df, use_container_width=True)



