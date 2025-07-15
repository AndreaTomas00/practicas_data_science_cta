import streamlit as st
import base64
from pathlib import Path
from navigation import make_sidebar

make_sidebar()

# Configure the page to use wide layout
st.set_page_config(page_title="Conexión SAP con DTX", layout="wide")
# Add a hyperlink
st.markdown("[Ver documentación completa del proyecto](https://github.com/AndreaTomas00/donor_db/tree/main)", unsafe_allow_html=True)

# Page title
st.title("Conexión SAP con DTX")

st.write("Se planteo crear formularios en SAP con la información de los donantes para que se rellenen ahí y poder nutrir los formularios de otros ya presentes en el programa, hechos por otros equipos.")
# Creating a numbered list
st.write("""
1. Estudio de la documentación de la API de DTX para establecer la conexión y estudiar el envio de datos.
2. Creación de donantes de prueba en DTX a través de la API para verificar la correcta recepción de los datos básicos.
3. Pruebas para envío de documentos PDF.
4. Reunión con DSI.
""")

def display_image(image_name):
    image_path = Path(__file__).parent / image_name
    if image_path.exists():
        _, col1, _ = st.columns([1, 8, 1])  # 80% for the image, 20% empty
        with col1:
            st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"Image {image_name} not found")
display_image("sap_dtx.png")