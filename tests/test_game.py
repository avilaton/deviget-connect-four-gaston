import pytest
from connect_four import ConnectFour, ConnectFourException


def test_game():
    game = ConnectFour()
    assert game.rows == 6
    assert game.cols == 7
    assert game.turn in ['RED', 'YELLOW']


def test_next_turn():
    game = ConnectFour()
    first_turn = game.turn
    game.next_turn()
    assert game.turn is not first_turn
    game.next_turn()
    assert game.turn is first_turn


def test_move():
    game = ConnectFour()
    current_turn = game.turn
    game.move(2)
    assert game.board[0][2] == current_turn
    assert game.board[0][5] == None
    assert game.turn is not current_turn
    current_turn = game.turn
    game.move(1)
    assert game.board[0][1] == current_turn
    assert game.board[0][5] == None
    game.move(2)
    game.move(2)
    game.move(2)
    game.move(2)
    game.move(2)
    with pytest.raises(ConnectFourException) as excinfo:
        game.move(2)
    assert 'Column is full' in str(excinfo.value), 'Column 2 is full'


def test_diagonals():
    diagonals = ConnectFour.diagonals([[1,2,3],
                                       [4,5,6],
                                       [7,8,9]])
    assert [7] in diagonals
    assert [4,8] in diagonals
    assert [1,5,9] in diagonals
    assert [2,6] in diagonals
    assert [3] in diagonals
    anti_diagonals = ConnectFour.diagonals([[1,2,3],
                                            [4,5,6],
                                            [7,8,9]], anti=True)
    assert [1] in anti_diagonals
    assert [4,2] in anti_diagonals
    assert [7,5,3] in anti_diagonals
    assert [8,6] in anti_diagonals
    assert [9] in anti_diagonals


def test_get_winner():
    w = ConnectFour.get_winner([
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'YELLOW', None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])
    assert not w
    w = ConnectFour.get_winner([
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])
    assert w is 'RED'
    w = ConnectFour.get_winner([
        [None, None, None, 'YELLOW', None, None, None],
        [None, None, 'YELLOW', 'RED', None, None, None],
        [None, 'YELLOW', None, 'RED', None, None, None],
        ['YELLOW', None, None, 'YELLOW', None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ])
    assert w is 'YELLOW'
    w = ConnectFour.get_winner([
        [None, None, None, 'RED', None, None, None],
        [None, None, None, 'RED', None, None, None],
        ['RED', None, None, 'RED', None, None, None],
        [None, 'RED', None, 'YELLOW', None, None, None],
        [None, None, 'RED', None, None, None, None],
        [None, None, None, 'RED', None, None, None]
    ])
    assert w is 'RED'
