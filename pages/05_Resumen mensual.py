import streamlit as st
import base64
from pathlib import Path
from navigation import make_sidebar
make_sidebar()

# Configure the page to use wide layout
st.set_page_config(page_title="Resumen mensual", layout="wide")

st.title("Elaboración de una visualización del resumen mensual de actividad de donación y trasplante")

def display_image(image_name):
    image_path = Path(__file__).parent / image_name
    if image_path.exists():
        _, col1, _ = st.columns([1, 8, 1])  # 80% for the image, 20% empty
        with col1:
            st.image(str(image_path), use_container_width=True)
    else:
        st.error(f"Image {image_name} not found")
display_image("resumen_mensual.png")

st.markdown("[Ver visualización](https://app.powerbi.com/view?r=eyJrIjoiN2Y3MjI0ZjItYzNiMy00NmM1LWIzY2EtZGI0ZjhjOWQ5MGIxIiwidCI6Ijc4ZmMzMGFhLThmMjEtNGE3ZC05ZjFhLWEzOTkzZTIyOTM0OSIsImMiOjl9)", unsafe_allow_html=True)

