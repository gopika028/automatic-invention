import random
def math_quiz_game():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    correct_answer=num1+num2
    print(f"What is{num1}+{num2}?")
    guess=int(input("your answer:"))
    if guess==correct_answer:
        print("correct!well done")
    else:
        print(f"oops!The correct answer is{correct_answer}.")
def colour_guessing_game():
                