import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()


st.title("Portfolio prácticas DATA SCIENCE - CTA 2025")

st.write("Inicia sesión")

username = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Log in", type="primary"):
    if username == "angel" and password == "123":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/gantt.py")
    else:
        st.error("Incorrect username or password")