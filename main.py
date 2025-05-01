import json
from random import randint

path = "./questions_eda.json"

try:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Ensure the JSON is a list of dictionaries with "question" and "answer" keys
        if isinstance(data, list) and all("question" in item and "answer" in item for item in data):
            questions = data
        else:
            print("Error: Unexpected JSON format. Expected a list of objects with 'question' and 'answer' keys.")
            questions = []
except FileNotFoundError:
    print(f"Error: File {path} not found.")
    questions = []
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from {path}.")
    questions = []

choice = 0

while choice != "2":
    choice = input("1) Ask a question\n2) Quit\n")
    if choice == "1":
        if questions:
            question_start = 0
            question_end = len(questions) - 1
            select_question = randint(question_start, question_end)
            selected = questions[select_question]  # Access the dictionary at the selected index
            print(f"Question: {selected['question']}")
            answer = input("Want to see the answer? y/n\n")
            if answer.lower() == "y":
                print(f"Answer: {selected['answer']}")
        else:
            print("No questions available.")