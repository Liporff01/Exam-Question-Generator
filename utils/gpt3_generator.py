
# # import openai
# # import os
# # from dotenv import load_dotenv
# # from openai import OpenAI



# # # Load environment variables from .env file
# # load_dotenv()

# # # Get the OpenAI API key from the environment variable
# # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # # Set the API key for OpenAI
# # openai.api_key = OPENAI_API_KEY

# # # def generate_questions(course, difficulty, num_questions, generate_answers, question_types, topics):
# # #     """
# # #     Generates questions using GPT-3.5 Turbo.

# # #     Parameters:
# # #     - course: str, the course for which questions are being generated
# # #     - difficulty: str, difficulty level of the questions
# # #     - num_questions: int, number of questions to generate
# # #     - generate_answers: bool, whether to generate answers as well
# # #     - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
# # #     - topics: list, specific topics within the course

# # #     Returns:
# # #     - list of dictionaries, each containing a question and optionally an answer
# # #     """
# # #     # Ensure the number of questions does not exceed a practical limit
# # #     num_questions = min(num_questions, 2048)  # set max tokens to 2048

# # #     # Construct the prompt based on the input parameters
# # #     prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
# # #               f"for the course {course}. Question types should include {', '.join(question_types)}. ")

# # #     if generate_answers:
# # #         prompt += "Please provide the correct answers as well."

# # #     # Call the OpenAI API to generate the questions
# # #     try:
# # #         response = openai.ChatCompletion.create(
# # #             model="gpt-3.5-turbo",
# # #             messages=[{"role": "system", "content": "You are an expert in generating educational questions."},
# # #                       {"role": "user", "content": prompt}],
# # #             max_tokens=2048,
# # #             temperature=0.7,
# # #         )
# # #         generated_questions = response['choices'][0]['message']['content'].strip().split("\n")

# # #         # Process the response into a list of questions (and answers if included)
# # #         questions = []
# # #         for q in generated_questions:
# # #             if generate_answers:
# # #                 question, answer = q.split("Answer:", 1)
# # #                 questions.append({"question": question.strip(), "answer": answer.strip()})
# # #             else:
# # #                 questions.append({"question": q.strip(), "answer": None})

# # #         return questions

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #         return []

# # # def generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers):
# # #     """
# # #     Generates questions using GPT-3.5 Turbo.

# # #     Parameters:
# # #     - course: str, the course for which questions are being generated
# # #     - difficulty: str, difficulty level of the questions
# # #     - num_questions: int, number of questions to generate
# # #     - generate_answers: bool, whether to generate answers as well
# # #     - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
# # #     - topics: list, specific topics within the course

# # #     Returns:
# # #     - list of dictionaries, each containing a question and optionally an answer
# # #     """
# # #     # Ensure num_questions is an integer
# # #     num_questions = int(num_questions)  # Convert to integer if needed

# # #     # Ensure the number of questions does not exceed a practical limit
# # #     num_questions = min(num_questions, 2048)  # set max tokens to 2048

# # #     # Construct the prompt based on the input parameters
# # #     prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
# # #               f"for the course {course}. Question types should include {', '.join(question_types)}. ")

# # #     if generate_answers:
# # #         prompt += "Please provide the correct answers as well."

# # #     # Call the OpenAI API to generate the questions
# # #     try:
# # #         response = openai.ChatCompletion.create(
# # #             model="gpt-3.5-turbo",
# # #             messages=[{"role": "system", "content": "You are an expert in generating educational questions."},
# # #                       {"role": "user", "content": prompt}],
# # #             max_tokens=2048,
# # #             temperature=0.7,
# # #         )
# # #         generated_questions = response['choices'][0]['message']['content'].strip().split("\n")

# # #         # Process the response into a list of questions (and answers if included)
# # #         questions = []
# # #         for q in generated_questions:
# # #             if generate_answers:
# # #                 question, answer = q.split("Answer:", 1)
# # #                 questions.append({"question": question.strip(), "answer": answer.strip()})
# # #             else:
# # #                 questions.append({"question": q.strip(), "answer": None})

# # #         return questions

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #         return []
# # def generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers):
# #     """
# #     Generates questions using GPT-3.5 Turbo.

# #     Parameters:
# #     - course: str, the course for which questions are being generated
# #     - difficulty: str, difficulty level of the questions
# #     - num_questions: int, number of questions to generate
# #     - generate_answers: bool, whether to generate answers as well
# #     - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
# #     - topics: list, specific topics within the course

# #     Returns:
# #     - list of dictionaries, each containing a question and optionally an answer
# #     """
# #     # Ensure num_questions is an integer
# #     num_questions = int(num_questions)

# #     # Construct the prompt based on the input parameters
# #     prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
# #               f"for the course {course}. Question types should include {', '.join(question_types)}. ")

# #     if generate_answers:
# #         prompt += "Please provide the correct answers as well."

# #     # Call the OpenAI API to generate the questions
# #     try:
# #         response = openai.ChatCompletion.create(
# #             model="gpt-3.5-turbo",
# #             messages=[{"role": "system", "content": "You are an expert in generating educational questions."},
# #                       {"role": "user", "content": prompt}],
# #             max_tokens=2048,
# #             temperature=0.7,
# #         )
# #         generated_content = response['choices'][0]['message']['content'].strip()

# #         # Process the response into a list of questions (and answers if included)
# #         questions = []
# #         for entry in generated_content.split("\n\n"):
# #             parts = entry.split("Answer:", 1)
# #             question = parts[0].strip()
# #             answer = parts[1].strip() if len(parts) > 1 else None
# #             questions.append({"question": question, "answer": answer})

# #         return questions

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return []


# # utils/gpt3_generation.py

# import os
# from openai import OpenAI

# # Initialize OpenAI with API key
# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY")
# )

# def generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers):
#     """
#     Generates questions using GPT-3.5 Turbo.

#     Parameters:
#     - course: str, the course for which questions are being generated
#     - difficulty: str, difficulty level of the questions
#     - num_questions: int, number of questions to generate
#     - generate_answers: bool, whether to generate answers as well
#     - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
#     - topics: list, specific topics within the course

#     Returns:
#     - list of dictionaries, each containing a question and optionally an answer
#     """
#     # Ensure num_questions is an integer
#     num_questions = int(num_questions)

#     # Construct the prompt based on the input parameters
#     prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
#               f"for the course {course}. Question types should include {', '.join(question_types)}. ")

#     if generate_answers:
#         prompt += "Please provide the correct answers as well."

#     # Call the OpenAI API to generate the questions
#     try:
#         response = client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": "You are an expert in generating educational questions."},
#                 {"role": "user", "content": prompt}
#             ],
#             model="gpt-3.5-turbo",
#             max_tokens=2048,
#             temperature=0.7,
#         )

#         generated_content = response['choices'][0]['message']['content'].strip()

#         # Process the response into a list of questions (and answers if included)
#         questions = []
#         for entry in generated_content.split("\n\n"):
#             parts = entry.split("Answer:", 1)
#             question = parts[0].strip()
#             answer = parts[1].strip() if len(parts) > 1 else None
#             questions.append({"question": question, "answer": answer})

#         return questions

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# # Usage example
# if __name__ == "__main__":
#     course = "Biology"
#     topics = ["Genetics", "Evolution"]
#     question_types = ["MCQ", "SAQ"]
#     difficulty = "medium"
#     num_questions = 5
#     generate_answers = True

#     questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
#     for q in questions:
#         print(q)

# utils/gpt3_generation.py
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise ValueError("OPENAI_API_KEY environment variable is not set")

# import os
from openai import OpenAI

# Initialize OpenAI with API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
    # Or use direct key for testing:
    # api_key="your-api-key-here"
)

# def generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers):
#     """
#     Generates questions using GPT-3.5 Turbo.

#     Parameters:
#     - course: str, the course for which questions are being generated
#     - difficulty: str, difficulty level of the questions
#     - num_questions: int, number of questions to generate
#     - generate_answers: bool, whether to generate answers as well
#     - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
#     - topics: list, specific topics within the course

#     Returns:
#     - list of dictionaries, each containing a question and optionally an answer
#     """
#     # Ensure num_questions is an integer
#     num_questions = int(num_questions)

#     # Construct the prompt based on the input parameters
#     prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
#               f"for the course {course}. Question types should include {', '.join(question_types)}. ")

#     if generate_answers:
#         prompt += "Please provide the correct answers as well."

#     # Call the OpenAI API to generate the questions
#     try:
#         response = client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": "You are an expert in generating educational questions."},
#                 {"role": "user", "content": prompt}
#             ],
#             model="gpt-3.5-turbo",
#             max_tokens=2048,
#             temperature=0.7,
#         )

#         # Extract the response from the completion
#         generated_content = response.choices[0].message.content.strip()

#         # Process the response into a list of questions (and answers if included)
#         questions = []
#         for entry in generated_content.split("\n\n"):
#             parts = entry.split("Answer:", 1)
#             question = parts[0].strip()
#             answer = parts[1].strip() if len(parts) > 1 else None
#             questions.append({"question": question, "answer": answer})

#         return questions

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# # Usage example
# if __name__ == "__main__":
#     course = "Biology"
#     topics = ["Genetics", "Evolution"]
#     question_types = ["MCQ", "SAQ"]
#     difficulty = "medium"
#     num_questions = 5
#     generate_answers = True

#     questions = generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers)
#     for q in questions:
#         print(q)
# utils/gpt3_generator.py

def generate_questions(course, topics, question_types, difficulty, num_questions, generate_answers):
    """
    Generates questions using GPT-3.5 Turbo.

    Parameters:
    - course: str, the course for which questions are being generated
    - difficulty: str, difficulty level of the questions
    - num_questions: int, number of questions to generate
    - generate_answers: bool, whether to generate answers as well
    - question_types: list, types of questions to generate (e.g., MCQ, SAQ, WH)
    - topics: list, specific topics within the course

    Returns:
    - list of dictionaries, each containing a question and optionally an answer
    """
    # Ensure num_questions is an integer
    num_questions = int(num_questions)

    # Construct the prompt based on the input parameters
    prompt = (f"Generate {num_questions} {difficulty} questions on the topics {', '.join(topics)} "
              f"for the course {course}. Question types should include {', '.join(question_types)}. ")

    if generate_answers:
        prompt += "Please provide the correct answers as well."

    # Call the OpenAI API to generate the questions
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert in generating educational questions."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo",
            max_tokens=2048,
            temperature=0.7,
        )

        # Extract the response from the completion
        generated_content = response.choices[0].message.content.strip()

        # Process the response into a list of questions (and answers if included)
        questions = []
        for entry in generated_content.split("\n\n"):
            parts = entry.split("Answer:", 1)
            question = parts[0].strip()
            answer = parts[1].strip() if len(parts) > 1 else None
            # Assuming each entry should have a type; you may need to adjust this based on your prompt format
            q_type = "MCQ" if "multiple choice" in question.lower() else "SAQ"
            questions.append({"question": question, "answer": answer, "type": q_type})

        print("Generated Questions:", questions)  # Debug print

        return questions

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
