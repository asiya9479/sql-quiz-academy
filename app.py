"""Streamlit Community Cloud entrypoint: app.py."""
import streamlit as st

from academy import views
from academy.ui import footer, load_style, sidebar, topbar

st.set_page_config(page_title="SQL Quiz Academy", page_icon="📚", layout="wide", initial_sidebar_state="expanded")
if "page" not in st.session_state:
    st.session_state.page = "home"
load_style()
sidebar()
topbar()
{"home": views.home, "tests": views.tests, "login": views.login, "results": views.results}.get(st.session_state.page, views.home)()
footer()
