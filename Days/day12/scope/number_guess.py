from art import logo
from random import choice

EASY = 10
HARD = 5


def greet():
    print("Welcome to the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
def pick_number():
    return choice(list(_ for _ in range(100)))

def is_easy():
    answer = input('Type "e" for easy and any other key for hard')
    if answer == 'e' or answer == 'E':
        return True
    else:
        return False

def play_game(attempt, target_number):
    won = False
    print(f'You have {attempt} attempts remaining to guess the number.')
   
def start_game():
    print(logo)
    greet()
    target_number = pick_number()
    if(is_easy()):
        for i in range(EASY):
            play_game(i + 1, target_number)
    else:
        for i in range(HARD):
            play_game(i + 1, target_number)