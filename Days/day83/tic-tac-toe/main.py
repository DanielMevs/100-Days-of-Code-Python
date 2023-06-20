import random
import numpy as np


class TicTacToe:

    def __init__(self):
        self.board = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])


    def get_random_first_player(self):
        return random.randint(1, 2)


    def mark_spot(self, row, col, player):
        self.board[row][col] = player


    def row_win(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        return False
    

    def col_win(self, player):
        for row in self.board.T:
            if all([cell == player for cell in row]):
                return True
        return False
    

    def diag_win(self, player):
        if all([diag == player for diag in self.board.diagonal()]):
            return True
        if all([reverse_diag == player for reverse_diag in np.fliplr(self.board).diagonal()]):
            return True
        return False


    def is_player_win(self, player):
        if (self.row_win(player) or
                self.col_win(player) or
                self.diag_win(player)):
            return True
        return False


    def is_board_filled(self):
        return np.all(self.board != 0)


    def swap_player_turn(self, player):
        return 1 if player == 2 else 2


    def show_board(self):
        print(self.board)


    def start(self):

        player = self.get_random_first_player()

        while True:
            print(f"Player {player} turn")

            self.show_board()
            prompt = "Enter row and column numbers (separated by a space) to mark your spot: "
            # taking user input
            row, col = list(
                map(int, input(prompt).split(' ')))

            # marking the chosen spot
            self.mark_spot(row - 1, col - 1, player)


            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()