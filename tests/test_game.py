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

