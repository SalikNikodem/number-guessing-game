from helpers import starting_message, difficulty_select
from functions import start, calculate_chances, guessing


def main():
    difficulty = start(starting_message,difficulty_select)
    chances = calculate_chances(difficulty)
    guessing(chances)

if __name__ == "__main__":
    flag = True
    while flag:
        main()
        a = input("\nDo you want to play again?(y/n): ")
        if a != "y": flag = False