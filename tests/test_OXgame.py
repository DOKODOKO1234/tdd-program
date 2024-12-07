from unittest.mock import patch
import pytest
from game.OX_game import OXGame

def test_init_board():
    game = OXGame()
    #配列の初期化
    expected_board = [['-','-','-'] for _ in range(3)]
    assert game.board == expected_board

def test_display_board(capsys):
    game = OXGame()
    #表示が正しくできているか？
    game.display_board()
    captured = capsys.readouterr()
    expected_output = "- - -\n- - -\n- - -\n"
    assert captured.out == expected_output

def test_turn():
    game = OXGame()
    #初期条件　必ずXから始まる
    assert game.current_player == 'X'
    #配列の空きにXを代入してターン変更できるか？
    assert game.make_move(0,0) == True  
    assert game.board[0][0] == 'X'
    assert game.current_player == 'O'
    #同じところには入力できない、ターンも変わらない
    assert game.make_move(0,0) == False
    assert game.current_player == 'O'
    #ゲームの範囲外には入力できない、ターンも変わらない
    assert game.make_move(3,3) == False
    assert game.current_player == 'O'


def test_status():
    game = OXGame()
    #縦が揃って勝利
    game.board = [['X','-','-'],['X','-','-'],['X','-','-']]
    assert game.check_game_status() == "X Wins"
    game.board = [['-','X','-'],['-','X','-'],['-','X','-']]
    assert game.check_game_status() == "X Wins"
    game.board = [['-','-','X'],['-','-','X'],['-','-','X']]
    assert game.check_game_status() == "X Wins"
    #横が揃って勝利
    game.board = [['X','X','X'],['-','-','-'],['-','-','-']]
    assert game.check_game_status() == "X Wins"
    game.board = [['-','-','-'],['X','X','X'],['-','-','-']]
    assert game.check_game_status() == "X Wins"
    game.board = [['-','-','-'],['-','-','-'],['X','X','X']]
    assert game.check_game_status() == "X Wins"
    #斜めが揃って勝利
    game.board = [['X','-','-'],['-','X','-'],['-','-','X']]
    assert game.check_game_status() == "X Wins"
    game.board = [['-','-','X'],['-','X','-'],['X','-','-']]
    assert game.check_game_status() == "X Wins"
    #引き分け
    game.board = [['X','O','X'],['X','X','O'],['O','X','O']]
    assert game.check_game_status() == "DRAW"
    #継続
    game.board = [['X','-','X'],['X','X','O'],['O','X','O']]
    assert game.check_game_status() == 'Continue'


def test_reset_game():
    #引き分けの状態
    game = OXGame()
    game.board = [['X','O','X'],['X','X','O'],['O','X','O']]
    game.current_player = 'O'
    game.check_status = "DRAW"
    game.game_over = True

    #勝敗結果を表示
def test_game_status_display(capfd):
    game = OXGame()
    game.board = [['X','X','-'],['O','O','-'],['X','X','O']]
    game.make_move(0,2)
    captured = capfd.readouterr()
    assert "X Wins" in captured.out
    assert game.check_status == "X Wins"
    assert game.game_over == True

    #リセットできているか確認
    with patch('builtins.input', return_value='reset'):
        game.reset_or_exit()
        expected_board = [['-']*3 for _ in range (3)]
        assert game.board == expected_board
        assert game.current_player  == 'X'
        assert game.check_status == "Continue"
        assert game.game_over == False

    #引き分けの状態
def test_exit_game():
    game = OXGame()
    game.board = [['X','O','X'],['X','X','O'],['O','X','O']]
    game.current_player = 'O'
    game.check_status = "DRAW"
    game.game_over = True
    
    #正常に終了するか
    with patch('builtins.input', return_value='exit'):
        with pytest.raises(SystemExit):
            game.reset_or_exit()

