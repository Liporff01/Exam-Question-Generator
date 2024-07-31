# import streamlit as st
# from utils.database import get_all_questions, save_question

# def app():
#     st.title("Question Bank")

#     st.write("## Saved Questions")
#     all_questions = get_all_questions()
#     for question in all_questions:
#         st.write(f"Course: {question[1]}, Topic: {question[2]}, Type: {question[3]}, Difficulty: {question[4]}")
#         st.write(f"Question: {question[5]}")
#         if question[6]:
#             st.write(f"Answer: {question[6]}")
#         if st.button(f"Copy Question {question[0]}", key=f"copy_{question[0]}"):
#             st.write(f"Copied question: {question[5]}")
#         if st.button(f"Edit Question {question[0]}", key=f"edit_{question[0]}"):
#             new_question = st.text_area("Edit Question", value=question[5], key=f"edit_area_{question[0]}")
#             new_answer = st.text_area("Edit Answer", value=question[6], key=f"edit_answer_{question[0]}")
#             if st.button(f"Save Changes {question[0]}", key=f"save_{question[0]}"):
#                 save_question(question[1], question[2], question[3], question[4], new_question, new_answer, question[0])
#                 st.success(f"Question {question[0]} updated successfully!")

import streamlit as st
from utils.database import get_all_questions, save_question, delete_question

def app():
    st.title("Question Bank")

    st.write("## Saved Questions")
    all_questions = get_all_questions()
    for question in all_questions:
        st.write(f"Course: {question[1]}, Topic: {question[2]}, Type: {question[3]}, Difficulty: {question[4]}")
        st.write(f"Question: {question[5]}")
        if question[6]:
            st.write(f"Answer: {question[6]}")
        if st.button(f"Copy Question {question[0]}", key=f"copy_{question[0]}"):
            st.write(f"Copied question: {question[5]}")
        if st.button(f"Edit Question {question[0]}", key=f"edit_{question[0]}"):
            new_question = st.text_area("Edit Question", value=question[5], key=f"edit_area_{question[0]}")
            new_answer = st.text_area("Edit Answer", value=question[6], key=f"edit_answer_{question[0]}")
            if st.button(f"Save Changes {question[0]}", key=f"save_{question[0]}"):
                save_question(question[1], question[2], question[3], question[4], new_question, new_answer, question[0])
                st.success(f"Question {question[0]} updated successfully!")
        if st.button(f"Delete Question {question[0]}", key=f"delete_{question[0]}"):
            delete_question(question[0])
            st.success(f"Question {question[0]} deleted successfully!")
