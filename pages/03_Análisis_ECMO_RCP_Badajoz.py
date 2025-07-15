import streamlit as st
import base64
from pathlib import Path
from navigation import make_sidebar
make_sidebar()

# Configure the page to use wide layout
st.set_page_config(page_title="Análisis ECMO RCP Badajoz", layout="wide")

# Page title
st.title("Análisis ECMO RCP Badajoz")

# Function to display PDF
def display_pdf(file_path):
    # Get the filename from the path
    pdf_filename = Path(file_path).name
    
    # Open file and encode in base64
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_data = f.read()  # Reset file pointer
        f.seek(0)
        pdf_data = f.read()
    
    # Embed PDF in HTML with title attribute
    pdf_display = f'''
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="800" 
            type="application/pdf"
            title="{pdf_filename}">
        </iframe>
    '''
    # Display the PDF
    st.markdown(pdf_display, unsafe_allow_html=True)

# Create PDF options dictionary
pdf_options = {
    "Documento análisis descriptivo + univariante": "./pages/ecmo_def_amarillo.pdf",
    "Poster": "./pages/POSTER.pdf"
}

# Add selectbox for user to choose which PDF to display
selected_option = st.selectbox("Seleccione el documento a visualizar:", 
                               options=list(pdf_options.keys()))

# Display the selected PDF with appropriate subheader
st.subheader(selected_option)
display_pdf(pdf_options[selected_option])
