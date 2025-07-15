import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from pathlib import Path 

def get_current_page_name():
    ctx = get_script_run_ctx()

    # we can local info like timezone froom ctx object.
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    page_name = Path(ctx.main_script_path).stem
    # logger.info(f"Current page name: {page_name}")

    return page_name

def make_sidebar():
    with st.sidebar:
        st.title("Prácticas DATA SCIENCE - CTA 2025")
        st.write("")
        st.write("")
        if st.session_state.get("logged_in", False):
            pages = {"Base de datos DTX - HCP": "pages/01_Base de datos DTX.py",
            "Conectar SAP con DTX": "pages/02_Conectar SAP con DTX.py",
            "Análisis ECMO-RCP Badajoz": "pages/03_Análisis_ECMO_RCP_Badajoz.py",
            "Completar análisis DANC": "pages/04_Completar análisis DANC.py",
            "Resumen mensual": "pages/05_Resumen mensual.py", }

            selected_page = st.selectbox("Cambia la página:", list(pages.keys()), index=None, placeholder="")
            if st.button("Log out"):
                logout()
            if selected_page is not None and selected_page != get_current_page_name():
                st.write()
                st.switch_page(pages[selected_page])

        elif get_current_page_name() != "login":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("login.py")

def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("login.py")