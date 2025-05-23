import json
from random import randint, shuffle
from datetime import datetime
import os



print("Hello there! Please select a file to use in the study quiz!")

folder_path = "./"

json_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]

for idx, filename in enumerate(json_files, start=1):
    print(f"{idx}. {filename}")

choice = int(input("Select a file number: "))
selected_file = json_files[choice - 1]

print(f"You selected: {selected_file}")

file_path = f"{folder_path}/{selected_file}"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        if isinstance(data, list) and all("question" in item and "answer" in item for item in data):
            questions = data
        else:
            print("Error: Unexpected JSON format. Expected a list of objects with 'question' and 'answer' keys.")
            questions = []
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
    questions = []
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON from {file_path}.")
    questions = []

choice = 0
correct = 0 
asked = 0
practice_more = []
user_answers = []
results = "0/0"


while choice != "2":
    choice = input("1) Ask a question\n2) Quit\n")
    print("----------------------------------------")
    if choice == "1":
        if questions:
            shuffle(questions)  # Shuffle the questions list to randomize the order
            question_start = 0
            question_end = len(questions) - 1
            select_question = randint(question_start, question_end)
            selected = questions[select_question]  # Access the dictionary at the selected index
            print(f"Question: {selected['question']}")
            print("----------------------------------------")
            user_answer = input("Enter the answer below:\n")
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
                practice_more.append({"question":selected['question'], "answer":selected['answer'], "user_answer":user_answer})
                
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
            f.write(f"- **Question**: {item['question']}\n")
            f.write(f"  **Answer**: {item['answer']}\n")
            f.write(f"  **Your Answer**: {item['user_answer']}\n\n")
        