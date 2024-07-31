# # import streamlit as st

# # class MultiApp:
# #     def __init__(self):
# #         self.apps = []

# #     def add_app(self, title, func):
# #         self.apps.append({
# #             "title": title,
# #             "function": func
# #         })

# #     def run(self):
# #         app = st.sidebar.selectbox(
# #             'Navigation',
# #             self.apps,
# #             format_func=lambda app: app['title']
# #         )
# #         app['function']()
# import streamlit as st
# from Pages import home, generate_questions, about, welcome, question_bank
# class MultiApp:
#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run(self):
#         # Add navigation bar to select different pages
#         app = st.sidebar.selectbox(
#             'Navigation',
#             self.apps,
#             format_func=lambda app: app['title']
#         )
#         # Execute the selected app function
#         if app:  # Check if an app was selected
#             app['function']()
#         if st.session_state.page == "Welcome":
#             welcome.app()
#         elif st.session_state.page == "Home":
#             home.app()
#         elif st.session_state.page == "Generate Questions":
#             generate_questions.app()
#         elif st.session_state.page == "Question Bank":
#             question_bank.app()
#         elif st.session_state.page == "About":
#             about.app()
# utils/multiapp.py
# import streamlit as st
# class MultiApp:
#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run(self):
#         app_titles = [app['title'] for app in self.apps]

#         # Handle navigation through sidebar and session state
#         if 'selected_app' not in st.session_state:
#             st.session_state.selected_app = app_titles[0]

#         st.sidebar.title('Navigation')
#         st.session_state.selected_app = st.sidebar.radio(
#             'Go to',
#             app_titles,
#             index=app_titles.index(st.session_state.selected_app)
#         )

#         # Run the selected app
#         for app in self.apps:
#             if app['title'] == st.session_state.selected_app:
#                 app['function']()

#     def set_page(self, page_title):
#         app_titles = [app['title'] for app in self.apps]
#         if page_title in app_titles:
#             st.session_state.selected_app = page_title
#             st.experimental_rerun()

import streamlit as st
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app_titles = [app['title'] for app in self.apps]

        # Handle navigation through sidebar and session state
        if 'selected_app' not in st.session_state:
            st.session_state.selected_app = app_titles[0]

        st.sidebar.title('Navigation')
        st.session_state.selected_app = st.sidebar.radio(
            'Go to',
            app_titles,
            index=app_titles.index(st.session_state.selected_app)
        )

        # Run the selected app
        for app in self.apps:
            if app['title'] == st.session_state.selected_app:
                app['function']()

    def set_page(self, page_title):
        app_titles = [app['title'] for app in self.apps]
        if page_title in app_titles:
            st.session_state.selected_app = page_title
            st.experimental_rerun()
