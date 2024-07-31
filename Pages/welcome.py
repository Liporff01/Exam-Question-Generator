import streamlit as st

def app():
    st.title("Welcome to the Exam Question Generator")
    
    st.write("This app helps you generate exam questions.")
    st.write("Please select your role:")

    role = st.radio(" ", ["Student", "Instructor"])
    if role == "Student":
        if st.button("Continue"):
            st.session_state.selected_app = 'Home'
            st.experimental_rerun()
    else:
        if st.button("Continue"):
            st.session_state.selected_app = 'Home'
            st.experimental_rerun()
        