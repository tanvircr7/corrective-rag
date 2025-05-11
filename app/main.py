import streamlit as st
import os
from PyPDF2 import PdfReader

# Set the path for the data directory
DATA_DIR = "data"

# Create data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_uploaded_file(uploaded_file):
    try:
        file_path = os.path.join(DATA_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def main():
    st.title("PDF File Upload and Reader")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save button
        if st.button("Save PDF"):
            file_path = save_uploaded_file(uploaded_file)
            if file_path:
                st.success(f"File saved successfully to {file_path}")
        
        # Read button
        if st.button("Read PDF"):
            file_path = os.path.join(DATA_DIR, uploaded_file.name)
            if os.path.exists(file_path):
                text_content = read_pdf(file_path)
                if text_content:
                    st.subheader("PDF Content:")
                    st.text_area("", text_content, height=300)
            else:
                st.warning("Please save the file first before reading")

if __name__ == "__main__":
    main()
