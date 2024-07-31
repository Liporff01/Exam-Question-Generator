# # import streamlit as st
# # from utils.app import MultiApp
# # from Pages import home, generate_questions, about, welcome

# # # Initialize session state for page
# # if 'page' not in st.session_state:
# #     st.session_state.page = 'Welcome'

# # # MultiApp instance
# # app = MultiApp()

# # # Add all your applications here
# # app.add_app("Welcome", welcome.app)
# # app.add_app("Home", home.app)
# # app.add_app("Generate Questions", generate_questions.app)
# # app.add_app("About", about.app)

# # # Run the current page
# # if st.session_state.page == 'Welcome':
# #     welcome.app()
# # elif st.session_state.page == 'Home':
# #     home.app()
# # elif st.session_state.page == 'Generate Questions':
# #     generate_questions.app()
# # elif st.session_state.page == 'About':
# #     about.app()
# import streamlit as st
# from utils.multiapp import MultiApp
# from Pages import home, generate_questions, about, welcome, question_bank

# # Initialize the MultiApp
# app = MultiApp()

# # Add all your application pages here
# app.add_app("Welcome", welcome.app)
# app.add_app("Home", home.app)
# app.add_app("Generate Questions", generate_questions.app)
# app.add_app("Question Bank", question_bank.app)
# app.add_app("About", about.app)

# # The main app
# app.run()
# import streamlit as st
# from utils.multiapp import MultiApp
# from Pages import home, generate_questions, about, welcome, question_bank

# # Initialize session state if not already done
# if 'page' not in st.session_state:
#     st.session_state.page = "Welcome"

# # Initialize the MultiApp
# app = MultiApp()

# # Add all your application pages here
# app.add_app("Welcome", welcome.app)
# app.add_app("Home", home.app)
# app.add_app("Generate Questions", generate_questions.app)
# app.add_app("Question Bank", question_bank.app)
# app.add_app("About", about.app)

# # Function to navigate based on session state
# # def navigate_to_page():

#     # if st.session_state.page == "Welcome":
#     #     welcome.app()
#     # elif st.session_state.page == "Home":
#     #     home.app()
#     # elif st.session_state.page == "Generate Questions":
#     #     generate_questions.app()
#     # elif st.session_state.page == "Question Bank":
#     #     question_bank.app()
#     # elif st.session_state.page == "About":
#     #     about.app()
 
# app.run()
# # navigate_to_page()

import streamlit as st
from utils.multiapp import MultiApp
from Pages import home, generate_questions, about, welcome, question_bank

# Initialize session state if not already done
if 'page' not in st.session_state:
    st.session_state.page = "Welcome"

# Initialize the MultiApp
app = MultiApp()

# Add all your application pages here
app.add_app("Welcome", welcome.app)
app.add_app("Home", home.app)
app.add_app("Generate Questions", generate_questions.app)
app.add_app("Question Bank", question_bank.app)
app.add_app("About", about.app)

app.run()
