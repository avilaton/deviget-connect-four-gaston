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

    @staticmethod
    def diagonals(board, anti=False):
        """
        Compute all board diagonals.
        Use anti=True to get backward running diagonals
        Source is http://stackoverflow.com/a/23069625/1282324
        """
        forward = lambda h, p, q: h - p + q -1
        backward = lambda h, p, q: p - q
        diag = backward if anti else forward

        h, w = len(board), len(board[0])
        return [[board[diag(h, p, q)][q]
                 for q in range(max(p-h+1, 0), min(p+1, w))]
                for p in range(h + w - 1)]
