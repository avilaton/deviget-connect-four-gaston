import random


class ConnectFourException(Exception):
    pass


class ConnectFour:
    players = ['RED', 'YELLOW']

    def __init__ (self, cols = 7, rows = 6):
        self.cols = cols
        self.rows = rows
        self.board = [[None] * cols for _ in range(rows)]
        self.turn = random.choice(self.players)

    def print_board(self):
        print('\nBoard: next turn {0}'.format(self.turn))
        for row in self.board:
            print row

    def next_turn(self):
        self.turn = 'RED' if self.turn == 'YELLOW' else 'YELLOW'
        return self.turn

    def move(self, col):
        for row in self.board:
            if row[col]:
                continue
            else:
                row[col] = self.turn
                self.next_turn()
                return
        else:
            raise ConnectFourException('Column is full')
