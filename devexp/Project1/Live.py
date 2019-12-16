
import Utils
import MemoryGame
import GuessGame

# an intro message
def welcome(name):
    return "Hello " + name +" and welcome to the World of Games (WOG).\nHere you can find many cool games to play.\n"

# Choosing a game to load and difficulty
def load_game():
        game_number = input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer")
        game_difficulty = input("Please choose game difficulty from 1 to 5:")

# verifying legal input
        if game_number.isdigit() and game_difficulty.isdigit():
            game_number = int(game_number)
            game_difficulty = int(game_difficulty)

# verifying game number and difficulty in valid
            if game_number in range(1,3) and game_difficulty in range(1,6):
                if game_number == 1:
                    MemoryGame.play(game_difficulty)
                else:
                    GuessGame.play(game_difficulty)

# printing error and loop back to choose the correct game and difficulty
            else:
                print(Utils.ERROR_MESSAGE)
                load_game()
        else:
            print(Utils.ERROR_MESSAGE)
            load_game()

