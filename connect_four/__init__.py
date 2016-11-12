import random


class ConnectFour:
    players = ['RED', 'YELLOW']

    def __init__ (self, cols = 7, rows = 6):
        self.cols = cols
        self.rows = rows
        self.board = [[None] * cols for _ in range(rows)]
        self.turn = random.choice(self.players)

    def print_board(self):
        print('Board')
        for row in self.board:
            print row

    def next_turn(self):
        self.turn = 'RED' if self.turn == 'YELLOW' else 'YELLOW'
        return self.turn
