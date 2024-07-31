
# import sqlite3

# def get_connection():
#     """
#     Create a new SQLite database connection.
#     """
#     return sqlite3.connect('questions.db')

# def initialize_db():
#     """
#     Function to create the questions table if it doesn't exist
#     """
#     conn = get_connection()
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS questions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             course TEXT NOT NULL,
#             topic TEXT NOT NULL,
#             question_type TEXT NOT NULL,
#             difficulty TEXT NOT NULL,
#             question TEXT NOT NULL,
#             answer TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def save_question(course, topics, question_type, difficulty, question_text, answer_text, question_id=None):
#     """
#     Function to save a question to the database
#     """
#     conn = get_connection()
#     c = conn.cursor()
#     topics_str = ', '.join(topics)
#     if question_id:
#         c.execute('''
#             UPDATE questions 
#             SET course=?, topic=?, question_type=?, difficulty=?, question=?, answer=? 
#             WHERE id=?
#         ''', (course, topics_str, question_type, difficulty, question_text, answer_text, question_id))
#     else:
#         c.execute('''
#             INSERT INTO questions (course, topic, question_type, difficulty, question, answer) 
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (course, topics_str, question_type, difficulty, question_text, answer_text))
#     conn.commit()
#     conn.close()

# def get_all_questions():
#     """
#     Function to get all questions from the database
#     """
#     conn = get_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM questions')
#     results = c.fetchall()
#     conn.close()
#     return results

# # Initialize the database
# initialize_db()

import sqlite3

def get_connection():
    """
    Create a new SQLite database connection.
    """
    return sqlite3.connect('questions.db')

def initialize_db():
    """
    Function to create the questions table if it doesn't exist
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course TEXT NOT NULL,
            topic TEXT NOT NULL,
            question_type TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_question(course, topics, question_type, difficulty, question_text, answer_text, question_id=None):
    """
    Function to save a question to the database
    """
    conn = get_connection()
    c = conn.cursor()
    topics_str = ', '.join(topics)
    if question_id:
        c.execute('''
            UPDATE questions 
            SET course=?, topic=?, question_type=?, difficulty=?, question=?, answer=? 
            WHERE id=?
        ''', (course, topics_str, question_type, difficulty, question_text, answer_text, question_id))
    else:
        c.execute('''
            INSERT INTO questions (course, topic, question_type, difficulty, question, answer) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (course, topics_str, question_type, difficulty, question_text, answer_text))
    conn.commit()
    conn.close()

def get_all_questions():
    """
    Function to get all questions from the database
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM questions')
    results = c.fetchall()
    conn.close()
    return results

def delete_question(question_id):
    """
    Function to delete a question from the database
    """
    conn = get_connection()
    c = conn.cursor()
    c.execute('DELETE FROM questions WHERE id=?', (question_id,))
    conn.commit()
    conn.close()

# Initialize the database
initialize_db()
