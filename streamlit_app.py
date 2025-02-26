import streamlit as st
import pandas as pd
import openpyxl

# Function to load the Excel file (cache-friendly)
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path, sheet_name=None)  # ✅ Loads all sheets as a dictionary

# Set the correct file path
file_path = "Questions Data Wizco.xlsx"

# Load the Excel file and get sheet names
try:
    excel_data = load_excel(file_path)
    sheet_names = list(excel_data.keys())  # ✅ Gets all sheet names
except FileNotFoundError:
    st.error("File not found. Please check the file path and try again.")
    st.stop()

st.title("Excel Sheet Viewer")

# Dropdown to select sheet
selected_sheet = st.selectbox("Select a company", sheet_names)

# Load and display the selected sheet
if selected_sheet:
    df = excel_data[selected_sheet]  # ✅ Retrieve DataFrame from dictionary
    st.write(f"### {selected_sheet} Data")
    st.dataframe(df, use_container_width=True)



