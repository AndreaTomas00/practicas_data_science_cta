import streamlit as st
import base64
from pathlib import Path
from navigation import make_sidebar

make_sidebar()
# Configure the page to use wide layout
st.set_page_config(page_title="Creación base de datos DTX - Clinic", layout="wide")
# Add a hyperlink
# Page title
st.title("Creación base de datos DTX - Clinic")

st.markdown("[Ver documentación completa del proyecto](https://github.com/AndreaTomas00/donor_db/tree/main)", unsafe_allow_html=True)


# Function to display image with error handling
def display_image(image_name):
    image_path = Path(__file__).parent / image_name
    if image_path.exists():
        _, col1, _ = st.columns([1, 8, 1])  # 80% for the image, 20% empty
        with col1:
            st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"Image {image_name} not found")


st.subheader("Diseño inicial de la base de datos. Conexión base de datos con registros de los equipos")
display_image("BDD.png")
# Display ETL.png
st.subheader("Proceso ETL (extracción, transformación, carga)")
display_image("ETL.png")

# Add some spacing
st.write("")

# Display db_dense.png
st.subheader("Esquema de la Base de Datos")
display_image("db_dense.png")
