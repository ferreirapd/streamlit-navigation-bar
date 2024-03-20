import os

import streamlit as st

from streamlit_navigation_bar import st_navbar
from streamlit_theme import st_theme

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Documentation", "Examples", "Community", "GitHub"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "logo.svg")
urls = {"GitHub": "https://github.com"}
styles = {
    "nav": {"background-color": "black"},
    "span": {"color": "white"},
}
adjust = {"show_sidebar": False}

page = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    adjust=adjust,
)
st.write(page)

with st.sidebar:
    st.write("The sidebar button will not be shown.")
