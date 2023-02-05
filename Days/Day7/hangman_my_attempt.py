from random_word import RandomWords
from collections import deque
from art import logo


ATTEMPTS = 7

def ask_user_for_letter(guessed_letters):
    alread_guessed = False
    guess_length = 0
    while not alread_guessed:
        user_letter = input("Please enter a letter: ").lower()
        guess_length = len(user_letter)
        if guess_length > 1:
            print("You put in too many letters at once. Please try again.")
        elif user_letter in guessed_letters:
            print("You have already guessed that letter. Please try again.")
        else:
            alread_guessed = True
    
    return user_letter


def letter_is_in_word(target_word, letter_guess):
    return letter_guess in target_word
    
def get_random_word():
    r = RandomWords()
    # Return a single random word
    return r.get_random_word()

def get_letter_indices(guess, target_word):
    letter_indices = []
    for idx, letter in enumerate(target_word):
        if letter == guess:
            letter_indices.append(idx)

    return letter_indices


# is not the most efficient solution
def update_blank_list(blanks, guess, target_word):
    indices_to_update = get_letter_indices(guess, target_word)

    for index in indices_to_update:
        blanks = blanks[:index] + guess + blanks[index+1:]

    return blanks

def game_is_finished(blanks):
    if '_' not in blanks:
        return True



def play_hangman(random_word, blanks):
    words_guessed = []
    hang_man_figure = deque()
    body_parts = deque(['O', 'i', '|', '/', "\\", '/', "\\"])
    
    while(len(hang_man_figure) < ATTEMPTS):
        guess = ask_user_for_letter(words_guessed)
        if(letter_is_in_word(random_word, guess)):
            print("Successfully guessed a letter")
            blanks = update_blank_list(blanks, guess, random_word)
            print(f'New slot: {str(blanks)}')
            if game_is_finished(blanks):
                print('Congrats, you won Hangman')
                return
        else:
            print("Sorry, that letter is not in the word. Try again")
            hang_man_figure.appendleft(body_parts.popleft())
            print(str(blanks))
            print('Your hangman figure: ' + str(list(hang_man_figure)))

    print("Sorry you lose.")
    return


def main():
    print(logo)
    random_word = get_random_word()
    print(random_word)
    blanks = '_'*len(random_word)
    is_interested = True
    while(is_interested):
        play_hangman(random_word, blanks)
        answer = input('Do you want to play another game? Type "y/Y" for yes or any other key for no: ')
        if answer != 'y' or answer != 'Y':
            is_interested = False
            print("Good bye!")
        
    
    


if __name__ == '__main__':
    main()


