import streamlit as st

def app():
    st.title("Exam Question Generator")
    st.write("Welcome to the Exam Question Generator for General Studies courses: Use of English, Entrepreneurship and Philosophy.")
    st.write("""
    This tool helps educators generate exam questions for their courses. You can:
    - Select the course (Use of English, Entrepreneurship or Philosophy)
    - Select the Question type
    - Choose the difficulty level (Easy, Medium, Hard)
    - Specify the number of questions to generate
    - Optionally, generate answers for the questions
    """)
    if st.button("Continue to Generate Questions"):
    # Use session state to navigate to the Generate Questions page
        st.session_state.selected_app = "Generate Questions"
        st.experimental_rerun()
