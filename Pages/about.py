import streamlit as st

def app():
    st.title("About")
    st.write("This application generates exam questions for General Studies courses using GPT-3.5.")
    st.write("""
    The Exam Question Generator leverages OpenAI's GPT-3.5 to create customized questions for different difficulty levels.
    This tool is designed to assist educators in quickly creating diverse and challenging questions for their students.
    """)
    st.write("""
        ## Exam Question Generator
        
        ### Developer
        - Name: SHOLARIN SAMUEL AYOMIDE
        - Email: ayomidesholarin13@gmail.com
        - GitHub: [Your GitHub Profile]
    """)
    if st.button("Back to Welcome"):
        st.session_state.selected_app = 'Welcome'
        st.experimental_rerun()