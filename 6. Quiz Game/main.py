import json

try:
# Loading our questions from the JSON file
    with open('questions.json', "r") as json_data:
        all_questions = json.load(json_data)
except FileNotFoundError:
    print("File not found")
    exit()

CATEGORIES = list(all_questions.keys())


def ask_for_category():
    while True:
        category = input(f'What category? {'/'.join(CATEGORIES)}: ').strip().title()
        if category not in (CATEGORIES):
            print("Invalid asnwer!")
        else:
            break
    return category
    

def ask_question(number, question):
    print(f"{number+1}. {question['question']}")
    for option in question["options"]:
            print(option)


def get_answer():
    while True:
        answer = input('Enter the answer: ').lower()
        if answer not in ('a', 'b', 'c', 'd'):
            print("Invalid Answer! Enter (a/b/c/d)")
        else:
            break
    return answer


def display_user_answer(answer):
    print(f"Your answer: {answer}")


def validate_answer(question, answer):
    if answer == question["answer"]:
        print("Correct!\n")
    else:
        print("Wrong!\n")



def calculate_score(score, question, answer):
    if answer == question["answer"]:
        score += 1 
    return score



def main():
    score = 0
    category = ask_for_category()
    for number, question in enumerate(all_questions[category]):
        ask_question(number, question)
        answer = get_answer()
        display_user_answer(answer)
        validate_answer(question, answer)
        score = calculate_score(score, question, answer)    
    print(f"Your final score: {score}/{len(all_questions[category])}")


if __name__ == "__main__":
    main() 
