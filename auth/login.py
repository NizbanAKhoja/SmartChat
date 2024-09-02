import streamlit as st
from utils.db_utils import authenticate_user

def login_page():
    st.title("Login")

    # User input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.session_state["logged_in"] = True
            
            # Go to Q&A model page
            st.session_state.page = "qamodel"
        else:
            st.error("Invalid credentials!")
