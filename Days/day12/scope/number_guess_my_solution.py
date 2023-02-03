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


def play_game(target_number, difficulty):
    for i in range(difficulty):
        print(f'You have {i + 1} attempts remaining to guess the number.')
        guess = int(input("Take a guess: "))
        if guess < target_number:
            print("Too low. Guess again")
        if guess > target_number:
            print("Too high. Guess again")
        else:
            print("Spot on. You win!")
            return True
    print('You lose (ran out of tries).')
   

def main():
    print(logo)
    greet()
    target_number = pick_number()
    if(is_easy()):
        play_game(target_number, EASY)   
    else:
        play_game(target_number, HARD)

if __name__== '__main__':
    main()