import streamlit as st
from utils.db_utils import create_user, check_user_exists

def register_page():
    st.title("Register")

    # User input fields
    email = st.text_input("Email")
    username = st.text_input("Username")
    phone_number = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match!")
            return

        if check_user_exists(username, email):
            st.success("User already exists. Redirecting to login...")
            st.session_state.page = "login"
            return

        # Store the registration data in session state
        st.session_state.registration_data = {
            "email": email,
            "username": username,
            "password": password,
            "phone_number": phone_number,
        }

        # Go to OTP verification page
        st.session_state.page = "otp_verification"
