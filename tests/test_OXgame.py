import pytest
from game.OX_game import OXGame

def test_init_board():
    game = OXGame()
    expected_board = [['-','-','-'] for _ in range(3)]
    assert game.board == expected_board

def test_display_board(capsys):
    game = OXGame()
    game.display_board()
    captured = capsys.readouterr()
    expected_output = "- - -\n- - -\n- - -\n"
    assert captured.out == expected_output

def test_turn():
    game = OXGame()

    assert game.current_player == 'X'

    assert game.make_move(0,0) == True  
    assert game.board[0][0] == 'X'
    assert game.current_player == 'O'

    assert game.make_move(0,0) == False
    assert game.current_player == 'O'

    assert game.make_move(3,3) == False
    assert game.current_player == 'O'

