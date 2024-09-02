import streamlit as st
from auth import register, login, otp_verification
from models import qamodel

# Streamlit page configuration
st.set_page_config(page_title="Q&A LLM Model", layout="centered")

# Initialize session state if not already done
if "page" not in st.session_state:
    st.session_state.page = "register"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Page Navigation Logic
if st.session_state.page == "register":
    register.register_page()
elif st.session_state.page == "otp_verification":
    otp_verification.otp_verification_page()
elif st.session_state.page == "login":
    login.login_page()
elif st.session_state.page == "qamodel":
    qamodel.qa_page()

# Display Login button if the user is not logged in
if not st.session_state.logged_in:
    if st.session_state.page != "login":
        if st.button("Login"):
            st.session_state.page = "login"
