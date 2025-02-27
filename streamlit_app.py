import streamlit as st
import pandas as pd
import openpyxl

# Function to load the Excel file (cache-friendly)
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path, sheet_name=None)  # ✅ Loads all sheets as a dictionary

# Improved CSS styling
st.markdown(
    """
    <style>
    /* General page styling */
    .stApp {
        background-color: #F5F5F5;
    }

    /* Title styling */
    .stMarkdown h1 {
        color: #FF5733;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }

    /* Fix overlapping border issue */
    .stSelectbox div {
        background-color: #fff !important;
        border: 1px solid #FF5733 !important;
        border-radius: 6px;
        padding: 5px;
    }

    /* Improve table styling */
    .stDataFrame {
        border: 1px solid #FF5733 !important;
        border-radius: 6px;
        overflow: hidden;
    }

    /* Fix button padding */
    .stButton > button {
        background-color: #FF5733;
        color: white;
        border-radius: 6px;
        padding: 8px 14px;
        font-size: 16px;
        border: none;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #E04B25;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set the correct file path
file_path = "CATEGORIZED QUESTIONS.xlsx"

# Load the Excel file and get sheet names
try:
    excel_data = load_excel(file_path)
    sheet_names = list(excel_data.keys())  # ✅ Gets all sheet names
except FileNotFoundError:
    st.error("File not found. Please check the file path and try again.")
    st.stop()

st.title("📋 Interview Questions Data")

# Dropdown to select sheet
selected_sheet = st.selectbox("Select a company", sheet_names)

# Load and display the selected sheet
if selected_sheet:
    df = excel_data[selected_sheet]  # ✅ Retrieve DataFrame from dictionary
    st.write(f"### {selected_sheet} Questions")
    st.dataframe(df, use_container_width=True)

# Add a button for exporting data
if st.button("Download as CSV"):
    df.to_csv(f"{selected_sheet}.csv", index=False)
    st.success(f"File '{selected_sheet}.csv' is ready for download! ✅")

# Footer
st.markdown("---")






