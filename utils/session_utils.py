import streamlit as st

def initialize_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def save_chat_history(question, answer):
    initialize_chat_history()
    st.session_state.chat_history.append((question, answer))

def get_chat_history():
    initialize_chat_history()
    return st.session_state.chat_history
