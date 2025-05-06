import json
from random import randint
from datetime import datetime

path = "./questions_eda.json"

try:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
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
correct = 0 
asked = 0
practice_more = []
results = "0/0"

while choice != "2":
    choice = input("1) Ask a question\n2) Quit\n")
    print("----------------------------------------")
    if choice == "1":
        if questions:
            question_start = 0
            question_end = len(questions) - 1
            select_question = randint(question_start, question_end)
            selected = questions[select_question]  # Access the dictionary at the selected index
            print(f"Question: {selected['question']}")
            print("----------------------------------------")
            answer = input("Want to see the answer? y/n\n")
            print("----------------------------------------")
            if answer.lower() == "y":
                print(f"Answer: {selected['answer']}")
            print("----------------------------------------")
            answered_correctly = input("Did you answer correctly? y/n\n")
            print("----------------------------------------")
            if answered_correctly.lower() == "y":
                correct += 1
                asked += 1
            else:
                asked += 1
                practice_more.append(selected)
            results = f"Results: {correct}/{asked}"
            print(results)
            print("----------------------------------------")
            answer_again = input("Do you want to see this question again? y/n\n")
            if answer_again.lower() == "n":
                questions.remove(selected)
            print(f"Questions left: {len(questions)}")
        else:
            print("No questions available.")
            
print_input = input("Would you like to save your results? y/n\n")
if print_input.lower() == "y":
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"  # Format datetime to exclude invalid characters
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"## Results\n")
        f.write(f"Questions answered: {results}\n")
        f.write("## Hard Questions\n")
        for item in practice_more:
            f.write(f"- Question: {item['question']}\n")
            f.write(f"  Answer: {item['answer']}\n\n")
        