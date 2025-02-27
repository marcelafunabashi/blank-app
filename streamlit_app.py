import streamlit as st
import pandas as pd
import openpyxl

# Function to load the Excel file (cache-friendly)
@st.cache_data
def load_excel(file_path):
    return pd.read_excel(file_path, sheet_name=None)  # ✅ Loads all sheets as a dictionary

# Apply custom CSS styling
st.markdown(
    """
    <style>
    /* Set background colors */
    .stApp {
        background-color: #F5F5F5;
    }
    .css-18e3th9 {
        background-color: #FF5733 !important;  /* Sidebar background */
    }
    .css-1d391kg {
        background-color: #E0E0E0 !important;  /* Main container background */
    }

    /* Customize the title */
    .stMarkdown h1 {
        color: #FF5733;
        text-align: center;
        font-size: 36px;
    }

    /* Style the dropdown */
    .stSelectbox div {
        background-color: #fff !important;
        border: 2px solid #FF5733 !important;
        border-radius: 8px;
    }

    /* Style the data table */
    .stDataFrame {
        border: 2px solid #FF5733 !important;
        border-radius: 8px;
    }

    /* Style buttons */
    .stButton > button {
        background-color: #FF5733;
        color: white;
        border-radius: 8px;
        padding: 10px 16px;
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

# Sidebar for additional controls
st.sidebar.header("Navigation")
st.sidebar.write("Choose a company to view its interview questions.")

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
st.markdown("💡 *Built with ❤️ in Streamlit*")





