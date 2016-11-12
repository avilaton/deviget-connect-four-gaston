from connect_four import ConnectFour


def test_game():
    a_game = ConnectFour()
    assert a_game.rows == 6
    assert a_game.cols == 7
    assert a_game.turn in ['RED', 'YELLOW']
