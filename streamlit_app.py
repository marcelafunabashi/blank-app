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
    /* Fix overlapping border issue for selectbox */
    div[data-baseweb="select"] > div {
        border: 1px solid #FF5733 !important;
        border-radius: 6px !important;
        box-shadow: none !important;
    }

    /* Remove unnecessary outlines */
    div[data-baseweb="select"] > div:focus-within {
        outline: none !important;
        border: 1px solid #E04B25 !important;
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

st.title("Sample Interview Questions")

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






