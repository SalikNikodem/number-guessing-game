from helpers import starting_message, difficulty_select
from functions import start, calculate_chances, guessing


def main():
    difficulty = start(starting_message,difficulty_select)
    chances = calculate_chances(difficulty)
    guessing(chances)

if __name__ == "__main__":
    main()