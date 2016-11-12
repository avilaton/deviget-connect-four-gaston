from connect_four import ConnectFour


def test_game():
    a_game = ConnectFour()
    assert a_game.rows == 6
    assert a_game.cols == 7
    assert a_game.turn in ['RED', 'YELLOW']

def test_next_turn():
    a_game = ConnectFour()
    first_turn = a_game.turn
    a_game.next_turn()
    assert a_game.turn is not first_turn
    a_game.next_turn()
    assert a_game.turn is first_turn
