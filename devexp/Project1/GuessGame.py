from random import randint
import Score

# generate a random number between 1 and the difficulty the user entered
def generate_number(difficulty):
    secret_number = randint(1,difficulty)
    return secret_number

# getting the user guess
def get_guess_from_user(difficulty):
    number_guessed = int(input("Please guess a number between 1 to " + str(difficulty) + ":"))
    return number_guessed

# comparing user guess and random generated number
def compare_results(difficulty, secret_number):
    if secret_number == get_guess_from_user(difficulty):
        print("your guessed number", str(secret_number), "is correct")
        return True
    else:
        print("you guessed it wrong")
        return False

# running the game
def play(difficulty):
    if compare_results(difficulty,generate_number(difficulty)):
        Score.add_score(difficulty)




