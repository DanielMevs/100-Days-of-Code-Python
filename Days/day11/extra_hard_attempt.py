# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# 52 card deck
# author: Daniel Mevs

from random import shuffle
from art import logo

SCORE_LIMIT = 21
HAND_LIMIT = 17


class BlackJack:
    
    def __init__(self):
        self.deck, self.your_hand, self.dealers_hand = [], [], []
        self.your_total = 0
        self.dealer_total = 0
        self.get_deck()

    def play_round(self):
        self.deal_both_hands()
        print('Cards left in deck: ' + str(len(self.deck)))
        print('Your hand: ' + str(self.your_hand) + '\n\n')
        print('Dealers hand: ' + '[X, ' + str(self.dealers_hand[0]) + ']')

        self.place_wager()


    def deal_both_hands(self):
        for _ in range(2):
            if (len(self.deck) != 0):
                self.get_deck()
            self.your_hand.append(self.deck.pop())
            self.dealers_hand.append(self.deck.pop())

        self.evaluate_your_hand()
        

    def get_deck(self):
        numbered_cards = [i for i in range(2, 11)]
        special_cards = 3*[10]
        aces = (1, 11)
        self.deck = numbered_cards + special_cards
        del numbered_cards, special_cards
        self.deck.append(aces) 
        self.deck *= 4
        shuffle(self.deck)
        # print(deck)
        # print(len(deck))


    def evaluate_game(self):
        print('Dealers hand: ' + str(self.dealers_hand[::-1]))
        # self.dealers_total = sum(self.dealers_hand)
        self.evaluate_dealers_hand()
        if (self.dealer_total <= SCORE_LIMIT):
            if self.dealer_total < HAND_LIMIT:
                self.dealer_hits()
                self.evaluate_game()
            else:
                if self.dealer_total > self.your_total:
                    print("You lost this round.")
                elif self.dealer_total < self.your_total:
                    print("You won this round.")
                else:
                    print("This round was a draw.")
                    
                self.clear_table()
        else:
            self.dealer_busts()

        return


    def place_wager(self):
        if (self.your_total <= SCORE_LIMIT):
            if self.your_total < HAND_LIMIT:
                self.hit()
            elif self.your_total >= HAND_LIMIT:
                willHit = input('Hit? ("y" for yes and anything else for "no"): ')
                if willHit == 'y' or willHit == 'Y':
                    self.hit()
                    self.place_wager()
                else:
                    self.evaluate_game()           
        else:
            self.bust()

        return

        
    def dealer_hits(self):
        if (len(self.deck) != 0):
            self.get_deck()
        self.dealers_hand.append(self.deck.pop())
        print(f"Dealer's new hand: {str(self.dealers_hand)}")


    def you_bust(self):
        print('\nBUST. Your hand was greater that 21. You lose.')
        self.clear_table()

    def dealer_busts(self):
        print("\nBUST. Your dealer's hand was greater that 21. You win!")
        self.clear_table()
        


    def hit(self):
        if (len(self.deck) != 0):
            self.get_deck()
        self.my_hand.append(self.deck.pop())
        print('Your new hand: ' + str(self.your_hand) + '\n')


    def clear_table(self):
        self.your_hand = []
        self.your_total = 0
        self.dealers_hand = []
        self.dealer_total = 0


    def evaluate_dealers_hand(self):
        ace_index = None
        dealer_aces = 0
        for index, card in enumerate(self.dealers_hand):
            if isinstance(card, tuple):
                dealer_aces += 1
                ace_index = index
        if dealer_aces == 2:
            print('The dealer has two aces.')
            answer = input("Enter '2' to consider their aces as 1 for total of 2 or any other key to consider it 1 and 11 for a total of 12: ")
            if answer=='2':
                self.dealers_hand[ace_index] = 1
                self.dealers_hand[ace_index-1] = 1
                self.dealer_total= int(answer)
            else:
                self.dealers_hand[ace_index] = 1
                self.dealers_hand[ace_index-1] = 11
                self.dealer_total = 12
        elif dealer_aces == 1:
            if self.your_hand[ace_index][1] + self.your_hand[ace_index-1] < SCORE_LIMIT:
                print('The dealer has one ace.')
                answer = input("Enter 'y' to consider their ace as 11 or any other key for 1")
                if answer == 'y' or answer == 'Y':
                    self.dealer_total = self.dealers_hand[ace_index][1] + self.dealers_hand[ace_index-1]
                else:
                    self.dealer_total = self.dealers_hand[ace_index][0] + self.dealers_hand[ace_index-1]
            else:
                self.dealer_total = self.your_hand[ace_index][0] + self.your_hand[ace_index-1]
        else:
            self.dealer_total = sum(self.dealers_hand)


    def evaluate_your_hand(self):
        ace_index = None
        your_aces = 0
        for index, card in enumerate(self.your_hand):
            if isinstance(card, tuple):
                your_aces += 1
                ace_index = index
        if your_aces == 2:
            print('You have two aces.')
            answer = input("Enter '2' to consider each ace as 1 for a count of 2 or any other key to consider it  as a 1 and 11 for a count of 12: ")
            if answer=='2':
                self.your_hand[ace_index] = 1
                self.your_hand[ace_index-1] = 1
                self.your_total = int(answer)
            else:
                self.your_hand[ace_index] = 1
                self.your_hand[ace_index-1] = 11
                self.your_total = 12
        elif your_aces == 1:
            if self.your_hand[ace_index][1] + self.your_hand[ace_index-1] < SCORE_LIMIT:
                print('You have one ace.')
                answer = input("Enter 'y' to consider your ace as 11 or any other key for 1")
                if answer == 'y' or answer == 'Y':
                    self.your_total = self.your_hand[ace_index][1] + self.your_hand[ace_index-1]
                else:
                    self.your_total = self.your_hand[ace_index][0] + self.your_hand[ace_index-1]
            else:
                self.your_total = self.your_hand[ace_index][0] + self.your_hand[ace_index-1]
        else:
            self.your_total = sum(self.your_hand)
                


def main():
    print(logo)
    new_game = BlackJack()
    is_interested = True

    while(is_interested):
        new_game.play_round()
        answer = input("Are you still interested in this game? 'y' for yes and any other answer for no: ")
        if answer != 'y' or answer != 'Y':
            is_interested = False


if __name__ == '__main__':
    main()