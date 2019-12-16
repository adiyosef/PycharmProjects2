import random
import Utils
import Score
import time

# generate a random list of numbers in size of difficulty
def generate_sequence(difficulty):
    list_of_random_numbers = random.sample(range(1,101),difficulty)
    print(list_of_random_numbers)
    time.sleep(0.7)
    Utils.screen_cleaner()
    return list_of_random_numbers

# getting the user's guessed list of numbers
def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    user_list = []
    for i in range(difficulty):
        number = int(input())
        user_list.append(number)
    return user_list

# comparing user's list of numbers and generated list of numbers
def is_list_equal(list_a, list_b):
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        return True
    else:
        return False

# playing the game
def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    result = is_list_equal(list_a,list_b)
    if result == True:
        print("you got it right!")
        Score.add_score(difficulty)
    else:
        print("no points for you")




