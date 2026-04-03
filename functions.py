from helpers import difficulties, chance
from random import randint

def start(starting_message,difficulty_select):
    print(starting_message)
    print()
    print(difficulty_select)
    difficulty = int(input("Enter your choice: "))
    if difficulty in [1,2,3]:
        return difficulty

    return None

def calculate_chances(difficulty):
    print(f"Great! You have selected the {difficulties[difficulty]} difficulty level.\nLet's start the game!")

    chances = chance[difficulty]

    return chances

def guessing(chances):
    tries = 1
    number = randint(1,100)
    while tries <= chances:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print(f"Congratulations! You guessed the correct number in {tries} attempts.")
            break
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")
        tries += 1

