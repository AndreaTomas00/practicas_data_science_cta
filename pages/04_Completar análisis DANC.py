import streamlit as st
import base64
from pathlib import Path
from navigation import make_sidebar
make_sidebar()

# Configure the page to use wide layout
st.set_page_config(page_title="Completar análisis DANC", layout="wide")

# Page title
st.title("Completar análisis DANC")
st.write("Partiendo del análisis realizado para el TFG de Laura, se añadieron a la base de datos los donantes del 2024 y se volvió a realizar todo el estudio con algunos cambios en el tratamiento de los missing values y elaborando dos modelos, uno para predicción de efectividad previo a entrada en ECMO y otro con todas las variables hasta la extracción.")
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

display_pdf("./pages/DANC_2.pdf")