# # # #  # import streamlit as st
# # # # # from utils.gpt3_generator import generate_questions
# # # # # from utils.database import save_question, get_all_questions
# # # # # from utils.document_export import export_to_docx

# # # # # def app():
# # # # #     st.title("GST Question Generator")

# # # # #     st.write("Select the course and difficulty level to generate questions.")

# # # # #     course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])
# # # # #     topic = st.multiselect("Select Topic (Optional)", ["Topic 1", "Topic 2", "Topic 3"])
# # # # #     question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
# # # # #     difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
# # # # #     num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
# # # # #     generate_answers = st.checkbox("Generate Answers")

# # # # #     if st.button("Generate"):
# # # # #         with st.spinner('Generating questions...'):
# # # # #             questions = generate_questions(course, topic, question_types, difficulty, num_questions, generate_answers)
# # # # #         st.success('Questions generated successfully!')

# # # # #         for i, question in enumerate(questions):
# # # # #             st.write(f"Q{i+1}: {question['question']}")
# # # # #             if generate_answers and question['answer']:
# # # # #                 st.write(f"Answer: {question['answer']}")
# # # # #             # Save each question to the database
# # # # #             save_question(course, topic, question['type'], difficulty, question['question'], question.get('answer'))

# # # # #     if st.button("Export to Document"):
# # # # #         export_to_docx(questions, course, topic, question_types, difficulty)
# # # # #         st.success('Questions exported successfully!')

# # # # #     st.write("## Saved Questions")
# # # # #     all_questions = get_all_questions()
# # # # #     for question in all_questions:
# # # # #         st.write(f"Course: {question[1]}, Topic: {question[2]}, Type: {question[3]}, Difficulty: {question[4]}")
# # # # #         st.write(f"Question: {question[5]}")
# # # # #         if question[6]:
# # # # #             st.write(f"Answer: {question[6]}")
# # # # #         if st.button(f"Copy Question {question[0]}", key=f"copy_{question[0]}"):
# # # # #             st.write(f"Copied question: {question[5]}")
# # # # #         if st.button(f"Edit Question {question[0]}", key=f"edit_{question[0]}"):
# # # # #             new_question = st.text_area("Edit Question", value=question[5], key=f"edit_area_{question[0]}")
# # # # #             new_answer = st.text_area("Edit Answer", value=question[6], key=f"edit_answer_{question[0]}")
# # # # #             if st.button(f"Save Changes {question[0]}", key=f"save_{question[0]}"):
# # # # #                 save_question(course, topic, question['type'], difficulty, new_question, new_answer, question[0])
# # # # #                 st.success(f"Question {question[0]} updated successfully!")
# # # # # # if __name__ == "__main__":
# # # # # #     app()
# # # # #newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
# # # # import streamlit as st
# # # # from utils.gpt3_generator import generate_questions
# # # # from utils.database import save_question, get_all_questions
# # # # from utils.document_export import export_to_docx

# # # # def app():
# # # #     st.title("GST Question Generator")

# # # #     st.write("Select the course and difficulty level to generate questions.")

# # # #     course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])

# # # #     if course == "Use of English":
# # # #         topics = st.multiselect("Select Topic(s)", [
# # # #             "Sound patterns in English Language (vowels and consonants. Phonetics and phonology).",
# # # #             "English word classes (lexical and grammatical words, definitions, forms, functions, usages, collocations).",
# # # #             "Sentence in English (types: structural and functional, simple and complex).",
# # # #             "Grammar and Usage (tense, mood, modality and concord, aspects of language use in everyday life).",
# # # #             "Logical and Critical Thinking and Reasoning Methods (Logic and Syllogism, Inductive and Deductive Argument and Reasoning Methods, Analogy, Generalisation and Explanations).",
# # # #             "Ethical considerations, Copyright Rules and Infringements. Writing Activities: (Pre-writing, Writing, Post-writing, Editing and Proofreading; Brainstorming, outlining, Paragraphing, Types of writing, Summary, Essays, Letter, Curriculum Vitae, Report writing, Note making, etc. Mechanics of writing).",
# # # #             "Comprehension Strategies: (Reading and types of Reading, Comprehension Skills, 3RsQ). Information and Communication Technology in Modern Language Learning. Language skills for effective communication.",
# # # #             "Major word formation processes. Writing and reading comprehension strategies. Logical and critical reasoning for meaningful presentations. Art of public speaking and listening. Report writing."
# # # #         ])
# # # #     elif course == "Philosophy":
# # # #         topics = st.multiselect("Select Topic(s)", [
# # # #             "Scope of philosophy; notions, meanings, branches and problems of philosophy. Logic as an indispensable tool of philosophy.",
# # # #             "Elements of syllogism, symbolic logic— the first nine rules of inference. Informal fallacies, laws of thought, nature of arguments.",
# # # #             "Valid and invalid arguments, logic of form and logic of content — deduction, induction and inferences.",
# # # #             "Creative and critical thinking. Impact of philosophy on human existence.",
# # # #             "Philosophy and politics, philosophy and human conduct, philosophy and religion, philosophy and human values, philosophy and character molding, etc."
# # # #         ])
# # # #     elif course == "Entrepreneurship":
# # # #         topics = st.multiselect("Select Topic(s)", [
# # # #             "Concept of Entrepreneurship (Entrepreneurship, Intrapreneurship/Corporate Entrepreneurship).",
# # # #             "Theories, Rationale, and relevance of Entrepreneurship (Schumpeterian and other perspectives, Risk-Taking, Necessity, and opportunity-based entrepreneurship and Creative destruction).",
# # # #             "Characteristics of Entrepreneurs (Opportunity seeker, Risk-taker, Natural and Nurtured, Problem solver and change agent, innovator and creative thinker).",
# # # #             "Entrepreneurial thinking (Critical thinking, Reflective Thinking, and Creative thinking).",
# # # #             "Innovation (Concept of innovation, Dimensions of innovation, Change, and innovation, Knowledge and innovation).",
# # # #             "Enterprise formation, partnership, and networking (Basics of Business Plan, Forms of business ownership, Business registration, and Forming alliances and joint ventures).",
# # # #             "Contemporary Entrepreneurship Issues (Knowledge, Skills and Technology, Intellectual property, Virtual office, Networking).",
# # # #             "Entrepreneurship in Nigeria (Biography of inspirational Entrepreneurs, Youth and women entrepreneurship, Entrepreneurship support institutions, Youth enterprise networks, and Environmental and cultural barriers to entrepreneurship).",
# # # #             "Basic principles of e-commerce."
# # # #         ])

# # # #     question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
# # # #     difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
# # # #     num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
# # # #     generate_answers = st.checkbox("Generate Answers")

# # # #     if st.button("Generate"):
# # # #         with st.spinner('Generating questions...'):
# # # #             questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
# # # #         st.success('Questions generated successfully!')

# # # #         for i, question in enumerate(questions):
# # # #             st.write(f"Q{i+1}: {question['question']}")
# # # #             if generate_answers and question['answer']:
# # # #                 st.write(f"Answer: {question['answer']}")
# # # #             # Save each question to the database
# # # #             save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))

# # # #     if st.button("Export to Document"):
# # # #         export_to_docx(questions, course, topics, question_types, difficulty)
# # # #         st.success('Questions exported successfully!')

# # # import streamlit as st
# # # from utils.gpt3_generator import generate_questions
# # # from utils.database import save_question
# # # from utils.document_export import export_to_docx

# # # def app():
# # #     st.title("GST Question Generator")

# # #     st.write("Select the course and difficulty level to generate questions.")

# # #     course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])

# # #     if course == "Use of English":
# # #         topics = st.multiselect("Select Topic(s)", [
# # #             "Sound patterns in English Language (vowels and consonants. Phonetics and phonology).",
# # #             "English word classes (lexical and grammatical words, definitions, forms, functions, usages, collocations).",
# # #             "Sentence in English (types: structural and functional, simple and complex).",
# # #             "Grammar and Usage (tense, mood, modality and concord, aspects of language use in everyday life).",
# # #             "Logical and Critical Thinking and Reasoning Methods (Logic and Syllogism, Inductive and Deductive Argument and Reasoning Methods, Analogy, Generalisation and Explanations).",
# # #             "Ethical considerations, Copyright Rules and Infringements. Writing Activities: (Pre-writing, Writing, Post-writing, Editing and Proofreading; Brainstorming, outlining, Paragraphing, Types of writing, Summary, Essays, Letter, Curriculum Vitae, Report writing, Note making, etc. Mechanics of writing).",
# # #             "Comprehension Strategies: (Reading and types of Reading, Comprehension Skills, 3RsQ). Information and Communication Technology in Modern Language Learning. Language skills for effective communication.",
# # #             "Major word formation processes. Writing and reading comprehension strategies. Logical and critical reasoning for meaningful presentations. Art of public speaking and listening. Report writing."
# # #         ])
# # #     elif course == "Philosophy":
# # #         topics = st.multiselect("Select Topic(s)", [
# # #             "Scope of philosophy; notions, meanings, branches and problems of philosophy. Logic as an indispensable tool of philosophy.",
# # #             "Elements of syllogism, symbolic logic— the first nine rules of inference. Informal fallacies, laws of thought, nature of arguments.",
# # #             "Valid and invalid arguments, logic of form and logic of content — deduction, induction and inferences.",
# # #             "Creative and critical thinking. Impact of philosophy on human existence.",
# # #             "Philosophy and politics, philosophy and human conduct, philosophy and religion, philosophy and human values, philosophy and character molding, etc."
# # #         ])
# # #     elif course == "Entrepreneurship":
# # #         topics = st.multiselect("Select Topic(s)", [
# # #             "Concept of Entrepreneurship (Entrepreneurship, Intrapreneurship/Corporate Entrepreneurship).",
# # #             "Theories, Rationale, and relevance of Entrepreneurship (Schumpeterian and other perspectives, Risk-Taking, Necessity, and opportunity-based entrepreneurship and Creative destruction).",
# # #             "Characteristics of Entrepreneurs (Opportunity seeker, Risk-taker, Natural and Nurtured, Problem solver and change agent, innovator and creative thinker).",
# # #             "Entrepreneurial thinking (Critical thinking, Reflective Thinking, and Creative thinking).",
# # #             "Innovation (Concept of innovation, Dimensions of innovation, Change, and innovation, Knowledge and innovation).",
# # #             "Enterprise formation, partnership, and networking (Basics of Business Plan, Forms of business ownership, Business registration, and Forming alliances and joint ventures).",
# # #             "Contemporary Entrepreneurship Issues (Knowledge, Skills and Technology, Intellectual property, Virtual office, Networking).",
# # #             "Entrepreneurship in Nigeria (Biography of inspirational Entrepreneurs, Youth and women entrepreneurship, Entrepreneurship support institutions, Youth enterprise networks, and Environmental and cultural barriers to entrepreneurship).",
# # #             "Basic principles of e-commerce."
# # #         ])

# # #     question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
# # #     difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
# # #     num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
# # #     generate_answers = st.checkbox("Generate Answers")

# # #     if st.button("Generate"):
# # #         with st.spinner('Generating questions...'):
# # #             questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
# # #         st.success('Questions generated successfully!')

# # #         for i, question in enumerate(questions):
# # #             st.write(f"Q{i+1}: {question['question']}")
# # #             if generate_answers and question['answer']:
# # #                 st.write(f"Answer: {question['answer']}")
# # #             save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))

# # #     if st.button("Save to Question Bank"):
# # #         st.success('Questions saved successfully!')

# # #     if st.button("Export to Document"):
# # #         export_to_docx(questions, course, topics, question_types, difficulty)
# # #         st.success('Questions exported successfully!')

# # # Pages/generate_questions.py

# # import streamlit as st
# # from utils.gpt3_generator import generate_questions
# # from utils.database import save_question, get_all_questions
# # from utils.document_export import export_to_docx

# # def app():
# #     st.title("GST Question Generator")

# #     st.write("Select the course and difficulty level to generate questions.")

# #     course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])

# #     if course == "Use of English":
# #         topics = st.multiselect("Select Topic(s)", [
# #             "Sound patterns in English Language (vowels and consonants. Phonetics and phonology).",
# #             "English word classes (lexical and grammatical words, definitions, forms, functions, usages, collocations).",
# #             "Sentence in English (types: structural and functional, simple and complex).",
# #             "Grammar and Usage (tense, mood, modality and concord, aspects of language use in everyday life).",
# #             "Logical and Critical Thinking and Reasoning Methods (Logic and Syllogism, Inductive and Deductive Argument and Reasoning Methods, Analogy, Generalisation and Explanations).",
# #             "Ethical considerations, Copyright Rules and Infringements. Writing Activities: (Pre-writing, Writing, Post-writing, Editing and Proofreading; Brainstorming, outlining, Paragraphing, Types of writing, Summary, Essays, Letter, Curriculum Vitae, Report writing, Note making, etc. Mechanics of writing).",
# #             "Comprehension Strategies: (Reading and types of Reading, Comprehension Skills, 3RsQ). Information and Communication Technology in Modern Language Learning. Language skills for effective communication.",
# #             "Major word formation processes. Writing and reading comprehension strategies. Logical and critical reasoning for meaningful presentations. Art of public speaking and listening. Report writing."
# #         ])
# #     elif course == "Philosophy":
# #         topics = st.multiselect("Select Topic(s)", [
# #             "Scope of philosophy; notions, meanings, branches and problems of philosophy. Logic as an indispensable tool of philosophy.",
# #             "Elements of syllogism, symbolic logic— the first nine rules of inference. Informal fallacies, laws of thought, nature of arguments.",
# #             "Valid and invalid arguments, logic of form and logic of content — deduction, induction and inferences.",
# #             "Creative and critical thinking. Impact of philosophy on human existence.",
# #             "Philosophy and politics, philosophy and human conduct, philosophy and religion, philosophy and human values, philosophy and character molding, etc."
# #         ])
# #     elif course == "Entrepreneurship":
# #         topics = st.multiselect("Select Topic(s)", [
# #             "Concept of Entrepreneurship (Entrepreneurship, Intrapreneurship/Corporate Entrepreneurship).",
# #             "Theories, Rationale, and relevance of Entrepreneurship (Schumpeterian and other perspectives, Risk-Taking, Necessity, and opportunity-based entrepreneurship and Creative destruction).",
# #             "Characteristics of Entrepreneurs (Opportunity seeker, Risk-taker, Natural and Nurtured, Problem solver and change agent, innovator and creative thinker).",
# #             "Entrepreneurial thinking (Critical thinking, Reflective Thinking, and Creative thinking).",
# #             "Innovation (Concept of innovation, Dimensions of innovation, Change, and innovation, Knowledge and innovation).",
# #             "Enterprise formation, partnership, and networking (Basics of Business Plan, Forms of business ownership, Business registration, and Forming alliances and joint ventures).",
# #             "Contemporary Entrepreneurship Issues (Knowledge, Skills and Technology, Intellectual property, Virtual office, Networking).",
# #             "Entrepreneurship in Nigeria (Biography of inspirational Entrepreneurs, Youth and women entrepreneurship, Entrepreneurship support institutions, Youth enterprise networks, and Environmental and cultural barriers to entrepreneurship).",
# #             "Basic principles of e-commerce."
# #         ])

# #     question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
# #     difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
# #     num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
# #     generate_answers = st.checkbox("Generate Answers")

# #     if st.button("Generate"):
# #         with st.spinner('Generating questions...'):
# #             questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
# #         st.success('Questions generated successfully!')

# #         for i, question in enumerate(questions):
# #             st.write(f"Q{i+1}: {question['question']}")
# #             if generate_answers and question['answer']:
# #                 st.write(f"Answer: {question['answer']}")
# #             # Save each question to the database
# #             save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))

# #     if st.button("Export to Document"):
# #         export_to_docx(questions, course, topics, question_types, difficulty)
# #         st.success('Questions exported successfully!')

# #     if st.button("Save to Question Bank"):
# #         st.success('Questions saved successfully!')                        

# # if __name__ == "__main__":
# #     app()
# # Pages/generate_questions.py

# import streamlit as st
# from utils.gpt3_generator import generate_questions
# from utils.database import save_question, get_all_questions
# from utils.document_export import export_to_docx

# def app():
#     st.title("GST Question Generator")

#     st.write("Select the course and difficulty level to generate questions.")

#     course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])

#     if course == "Use of English":
#         topics = st.multiselect("Select Topic(s)", [
#             "Sound patterns in English Language (vowels and consonants. Phonetics and phonology).",
#             "English word classes (lexical and grammatical words, definitions, forms, functions, usages, collocations).",
#             "Sentence in English (types: structural and functional, simple and complex).",
#             "Grammar and Usage (tense, mood, modality and concord, aspects of language use in everyday life).",
#             "Logical and Critical Thinking and Reasoning Methods (Logic and Syllogism, Inductive and Deductive Argument and Reasoning Methods, Analogy, Generalisation and Explanations).",
#             "Ethical considerations, Copyright Rules and Infringements. Writing Activities: (Pre-writing, Writing, Post-writing, Editing and Proofreading; Brainstorming, outlining, Paragraphing, Types of writing, Summary, Essays, Letter, Curriculum Vitae, Report writing, Note making, etc. Mechanics of writing).",
#             "Comprehension Strategies: (Reading and types of Reading, Comprehension Skills, 3RsQ). Information and Communication Technology in Modern Language Learning. Language skills for effective communication.",
#             "Major word formation processes. Writing and reading comprehension strategies. Logical and critical reasoning for meaningful presentations. Art of public speaking and listening. Report writing."
#         ])
#     elif course == "Philosophy":
#         topics = st.multiselect("Select Topic(s)", [
#             "Scope of philosophy; notions, meanings, branches and problems of philosophy. Logic as an indispensable tool of philosophy.",
#             "Elements of syllogism, symbolic logic— the first nine rules of inference. Informal fallacies, laws of thought, nature of arguments.",
#             "Valid and invalid arguments, logic of form and logic of content — deduction, induction and inferences.",
#             "Creative and critical thinking. Impact of philosophy on human existence.",
#             "Philosophy and politics, philosophy and human conduct, philosophy and religion, philosophy and human values, philosophy and character molding, etc."
#         ])
#     elif course == "Entrepreneurship":
#         topics = st.multiselect("Select Topic(s)", [
#             "Concept of Entrepreneurship (Entrepreneurship, Intrapreneurship/Corporate Entrepreneurship).",
#             "Theories, Rationale, and relevance of Entrepreneurship (Schumpeterian and other perspectives, Risk-Taking, Necessity, and opportunity-based entrepreneurship and Creative destruction).",
#             "Characteristics of Entrepreneurs (Opportunity seeker, Risk-taker, Natural and Nurtured, Problem solver and change agent, innovator and creative thinker).",
#             "Entrepreneurial thinking (Critical thinking, Reflective Thinking, and Creative thinking).",
#             "Innovation (Concept of innovation, Dimensions of innovation, Change, and innovation, Knowledge and innovation).",
#             "Enterprise formation, partnership, and networking (Basics of Business Plan, Forms of business ownership, Business registration, and Forming alliances and joint ventures).",
#             "Contemporary Entrepreneurship Issues (Knowledge, Skills and Technology, Intellectual property, Virtual office, Networking).",
#             "Entrepreneurship in Nigeria (Biography of inspirational Entrepreneurs, Youth and women entrepreneurship, Entrepreneurship support institutions, Youth enterprise networks, and Environmental and cultural barriers to entrepreneurship).",
#             "Basic principles of e-commerce."
#         ])

#     question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
#     difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
#     num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
#     generate_answers = st.checkbox("Generate Answers")

#     questions = []

#     if st.button("Generate"):
#         with st.spinner('Generating questions...'):
#             questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
#         st.success('Questions generated successfully!')

#         for i, question in enumerate(questions):
#             st.write(f"Q{i+1}: {question['question']}")
#             if generate_answers and question['answer']:
#                 st.write(f"Answer: {question['answer']}")
#             # Save each question to the database
#             save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))

#     if questions and st.button("Export to Document"):
#         export_to_docx(questions, course, topics, question_types, difficulty)
#         st.success('Questions exported successfully!')
#     elif not questions:
#         st.warning('No questions to export. Please generate questions first.')

# Pages/generate_questions.py

import streamlit as st
from utils.gpt3_generator import generate_questions
from utils.database import save_question, get_all_questions
from utils.document_export import export_to_docx
import pyperclip

def app():
    st.title("GST Question Generator")

    st.write("Select the course and difficulty level to generate questions.")

    course = st.selectbox("Select Course", ["Use of English", "Philosophy", "Entrepreneurship"])

    if course == "Use of English":
        topics = st.multiselect("Select Topic(s)", [
            "Sound patterns in English Language (vowels and consonants. Phonetics and phonology).",
            "English word classes (lexical and grammatical words, definitions, forms, functions, usages, collocations).",
            "Sentence in English (types: structural and functional, simple and complex).",
            "Grammar and Usage (tense, mood, modality and concord, aspects of language use in everyday life).",
            "Logical and Critical Thinking and Reasoning Methods (Logic and Syllogism, Inductive and Deductive Argument and Reasoning Methods, Analogy, Generalisation and Explanations).",
            "Ethical considerations, Copyright Rules and Infringements. Writing Activities: (Pre-writing, Writing, Post-writing, Editing and Proofreading; Brainstorming, outlining, Paragraphing, Types of writing, Summary, Essays, Letter, Curriculum Vitae, Report writing, Note making, etc. Mechanics of writing).",
            "Comprehension Strategies: (Reading and types of Reading, Comprehension Skills, 3RsQ). Information and Communication Technology in Modern Language Learning. Language skills for effective communication.",
            "Major word formation processes. Writing and reading comprehension strategies. Logical and critical reasoning for meaningful presentations. Art of public speaking and listening. Report writing."
        ])
    elif course == "Philosophy":
        topics = st.multiselect("Select Topic(s)", [
            "Scope of philosophy; notions, meanings, branches and problems of philosophy. Logic as an indispensable tool of philosophy.",
            "Elements of syllogism, symbolic logic— the first nine rules of inference. Informal fallacies, laws of thought, nature of arguments.",
            "Valid and invalid arguments, logic of form and logic of content — deduction, induction and inferences.",
            "Creative and critical thinking. Impact of philosophy on human existence.",
            "Philosophy and politics, philosophy and human conduct, philosophy and religion, philosophy and human values, philosophy and character molding, etc."
        ])
    elif course == "Entrepreneurship":
        topics = st.multiselect("Select Topic(s)", [
            "Concept of Entrepreneurship (Entrepreneurship, Intrapreneurship/Corporate Entrepreneurship).",
            "Theories, Rationale, and relevance of Entrepreneurship (Schumpeterian and other perspectives, Risk-Taking, Necessity, and opportunity-based entrepreneurship and Creative destruction).",
            "Characteristics of Entrepreneurs (Opportunity seeker, Risk-taker, Natural and Nurtured, Problem solver and change agent, innovator and creative thinker).",
            "Entrepreneurial thinking (Critical thinking, Reflective Thinking, and Creative thinking).",
            "Innovation (Concept of innovation, Dimensions of innovation, Change, and innovation, Knowledge and innovation).",
            "Enterprise formation, partnership, and networking (Basics of Business Plan, Forms of business ownership, Business registration, and Forming alliances and joint ventures).",
            "Contemporary Entrepreneurship Issues (Knowledge, Skills and Technology, Intellectual property, Virtual office, Networking).",
            "Entrepreneurship in Nigeria (Biography of inspirational Entrepreneurs, Youth and women entrepreneurship, Entrepreneurship support institutions, Youth enterprise networks, and Environmental and cultural barriers to entrepreneurship).",
            "Basic principles of e-commerce."
        ])

    question_types = st.multiselect("Select Question Type(s)", ["MCQ", "SAQ", "WH"])
    difficulty = st.radio("Select Difficulty Level", ["Easy", "Medium", "Hard"])
    num_questions = st.number_input("Number of Questions", min_value=10, max_value=60, value=15)
    generate_answers = st.checkbox("Generate Answers")

    questions = st.session_state.get('generated_questions', [])

    if st.button("Generate"):
        with st.spinner('Generating questions...'):
            questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
            st.session_state.generated_questions = questions
        st.success('Questions generated successfully!')

        for i, question in enumerate(questions):
            st.write(f"Q{i+1}: {question['question']}")
            if generate_answers and question['answer']:
                st.write(f"Answer: {question['answer']}")
            # Save each question to the database
            save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))

    if questions:
        if st.button("Save to Question Bank"):
            for question in questions:
                save_question(course, topics, question['type'], difficulty, question['question'], question.get('answer'))
            st.success('Questions saved to question bank successfully!')

        if st.button("Copy to Clipboard"):
            clipboard_content = "\n\n".join([f"Q{i+1}: {q['question']}\nAnswer: {q['answer']}" if q['answer'] else f"Q{i+1}: {q['question']}" for i, q in enumerate(questions)])
            pyperclip.copy(clipboard_content)
            st.success('Questions copied to clipboard!')

        if st.button("Export to Document"):
            export_to_docx(questions, course, topics, question_types, difficulty)
            st.success('Questions exported successfully!')
    else:
        st.warning('No questions to export. Please generate questions first.')
