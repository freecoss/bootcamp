data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def tell_wrong_answers(wrong_answers_nb, right_answers_nb):
    print(f"You got {right_answers_nb} right answers and {wrong_answers_nb} wrong answers")

def quiz():
    wrong_answers = []
    correct_answers = []
    for x in data:
        print(x["question"])
        answer = input("Enter your answer: ")
        if answer.lower() == x["answer"].lower():
            print("Correct!")
        else:
            print(f"Incorrect!")
            wrong_answers.append(answer)
            correct_answers.append(x["answer"])
        wrong_answers_nb = len(wrong_answers)
        right_answers_nb = len(data) - len(wrong_answers)
    tell_wrong_answers(wrong_answers_nb, right_answers_nb)
    if wrong_answers_nb == 0:
        print("Congratulations! You got all the answers right!")

    print("Thanks for playing!")
    for i in range(len(wrong_answers)):
        print(f"{i+1}- your answer for the question {i+1}:  {wrong_answers[i]} and the correct answer: {correct_answers[i]}")
    
    if wrong_answers_nb > 3:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            quiz()
        else:
            print("Thanks for playing!")
quiz()