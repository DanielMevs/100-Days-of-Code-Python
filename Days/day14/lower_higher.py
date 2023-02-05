from art import logo, vs
from game_data import data
from random import choice
from os import system

class LowerHigher:
    def __init__(self):
        self.celeb_one = {}
        self.celeb_two = {}
        self.winner = ''
        self.loser = ''


    def match_celebs(self):
        self.celeb_one = choice(data)
        self.celeb_two = choice(data)
        self.avoid_duplicates


    def avoid_duplicates(self):
        while self.celeb_one['name'] == self.celeb_two['name']:
            self.celeb_one = choice(data)

    def get_winner(self):
        if self.celeb_one['follower_count'] > self.celeb_two['follower_count']:
            self.winner = self.celeb_one['name']
            self.loser = self.celeb_two['name']
            return '1'
        else:
            self.winner = self.celeb_two['name']
            self.winner = self.celeb_one['name']
            return '2'
    

    def clear_round(self):
        self.celeb_one = {}
        self.celeb_two = {}
        self.winner = ''
        self.loser = ''
        system('clear')
        #system('cls')


    def play_round(self):
        print("Which celebrity has more Followers?")
        self.match_celebs()

        celeb_one_name = self.celeb_one['name']
        print("Celebrity 1: ")
        print(celeb_one_name)
        print(self.celeb_one['description'])
        print(self.celeb_one['country'])

        print(vs)

        celeb_two_name = self.celeb_two['name']
        print("Celebrity 2: ")
        print(celeb_two_name)
        print(self.celeb_two['description'])
        print(self.celeb_two['country'])



        answer = input(f"Enter 1 for {self.celeb_one['name']} or 2 for {self.celeb_two['name']}: ")
        while answer != '1' and answer != '2':
            answer = input("Invalid input. Renter guess: ")
        if answer == self.get_winner():
            print(f"Congratulations you were right! {self.winner} does have more followers than {self.loser}")
        else:
            print(f"You were wrong! {self.loser} does not have more followers than {self.winner}")
        

def main():
    game = LowerHigher()
    play = 'y'
    while(play == 'y'):
        game.play_round()
        play = input('New game? "Y/y" for yes and any other key for no: ').lower()
        game.clear_round()




if __name__=='__main__':
    main()