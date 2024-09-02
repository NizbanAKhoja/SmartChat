import streamlit as st
from utils.db_utils import create_user
from utils.email_utils import send_api_key

def otp_verification_page():
    st.title("OTP Verification")

    if "registration_data" not in st.session_state:
        st.error("Please complete registration first.")
        return

    otp = "1234"  # In real scenarios, generate a random OTP and send via SMS
    entered_otp = st.text_input("Enter OTP sent to your phone", max_chars=4)

    if st.button("Verify"):
        if entered_otp == otp:
            # Create the user and send API key via email
            reg_data = st.session_state.registration_data
            api_key = create_user(
                reg_data["email"], 
                reg_data["username"], 
                reg_data["password"], 
                reg_data["phone_number"]
            )
            send_api_key(reg_data["email"], api_key)
            st.success("OTP verified! Registered successfully. Check your email for the API key.")
            
            # Move to login page
            st.session_state.page = "login"
        else:
            st.error("Invalid OTP!")
