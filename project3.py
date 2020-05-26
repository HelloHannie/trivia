""" Write a project that we learned from  Stanford-CS 106A: Code in Place. A multiple choice
  questionnaire that would ask the user to select an answer. If the user answers the question, correctly.
  They will achieve (1) point. If their answer is incorrect, the questionnaire will repeat. A total of 20 questions.



"""

import random
import csv
import time

def load_questions():  # interpreter import cvs file
    questions = []
    with open("trivia.csv") as csv_file:
        csv_data = csv.reader(csv_file)
        next(csv_data)  # skip first line
        for line in csv_data: # import cvs file and execute question, correct, and answers on excel position
            question = {
                "question": line[0],
                "correct": int(line[1]),
                "answers": line[2:6]
            }
            questions.append(question)
    return questions


def ask_question(question):
    choice = ["a", "b", "c", "d"]
    print(question["question"])
    i = 0 # counting position for interpreter
    for j in question["answers"]: # multiple choice answers
        print(choice[i] + ") "+ j) # print out choice and answers selections
        i += 1
    user_answer = input("Select Your Choice:")
    print("") # blank space to separate question and user answer
    if user_answer == choice[question["correct"]]:
        return True
    else:
        print("Incorrect. The expected answer is " + question["answers"][question["correct"]] + ".")
        return False


def run_trivia(questions):
    num_questions = len(questions) # numbers of questions in cvs file
    i = 0
    start = time.time()
    while len(questions) > 0:
        # Interpreter will go into while loop when user answer is incorrect.
        question = random.choice(questions) # interpreter select question from cvs
        correct = ask_question(question) # user select correct answer
        if correct:
            questions.remove(question)  # remove question that has already been asked
            i = i + 1 # add point to score
            print("Correct! You've achieved " + str(i) + " point(s)" + " out of " + str(num_questions) + ".")
        print("") # blank line to separate the questions
    stop = time.time()
    #  congratulatory message
    print("Congratulations! You have completed this trivia in " + str(stop - start) + " seconds!")


def main():
    print("Welcome to my Trivia!")
    print("How fast can you answer these questions, correctly?")
    print("Hope you learned something new today!")
    print("Have FUN!")
    print("")
    questions = load_questions()
    run_trivia(questions)

if __name__ == "__main__":
    main()