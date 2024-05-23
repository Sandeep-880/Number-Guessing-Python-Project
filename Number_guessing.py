# Number Guessing Python Project

import random
import logo_art

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5 

def set_difficulty(level_choosen):
    if level_choosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_choosen == 'hard':
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number , answer , attempts):
    if guessed_number < answer:
        print("your Guess is to Low")
        return attempts - 1
    elif guessed_number > answer:
        print("Your Guess is to High")
        return attempts - 1
    else:
        print(f"your answer is right....... the answer was {answer} ")

def game():
    print(logo_art.logo)
    print("let me think the number between 1 to 50 ")
    answer = random.randint(1 , 50)

    level = input("Choose the level of difficluty .... type easy or hard : ")
    attempts = set_difficulty(level)
    guessed_number = 0

    while guessed_number != answer:
        print(f"Have {attempts} attempts remaining to guess the number ")
        guessed_number = int(input("Guess a Number : "))

        attempts = check_answer(guessed_number , answer , attempts)
        if attempts == 0:
            print("You are out of the Guess..... You Lose")
            return
        elif guessed_number != answer:
            print("Guess Again")
game()

