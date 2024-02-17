import json
from difflib import get_close_matches

def load_autolearn(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_autolearn(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
     matches: list = get_close_matches(user_question, questions, n = 1, cutoff= 0.6)
     return matches[0] if matches else None

def get_answer_for_question(question: str, autolearn: dict) -> str | None:
    for q in autolearn['questions']:
        if q["question"] == question:
            return q["answer"]

         

def chat_bot():
    autolearn: dict  = load_autolearn('autolearn.json')
    
    while True:
        user_input: str = input('You:')

        if user_input.lower() == 'quit':
            break

        best_match: str | None= find_best_match(user_input, [q["question"] for q in autolearn["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, autolearn)
            print(f'Bot: {answer}')

        else:
            print('Bot: I don\'t know the answer. Can you teach me')
            new_answer: str = input('Type the answer or "skip" to skip:')

            if new_answer.lower() != 'skip':
                autolearn["questions"].append({"question": user_input, "answer": new_answer})
                save_autolearn('autolearn.json', autolearn)
                print('Bot: Thank you! I learned a new response!')

def load_autolearn(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {"questions": []}



if __name__ == '__main__':
    chat_bot()
