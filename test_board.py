import pytest
from Board import Board

def test_board_initialization():
    board = Board()
    assert board.getBoardRows() == [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

def test_set_row_column():
    board = Board()
    board.setRowColumn(0, 0, 1)
    assert board.getRowColumn(0, 0) == 1

def test_set_row_column_invalid_value():
    board = Board()
    with pytest.raises(Exception):
        board.setRowColumn(0, 0, 2)

def test_check_winning_condition_no_win():
    board = Board()
    assert board.checkWinningCondition() == False

def test_check_winning_condition_win_row():
    board = Board()
    for i in range(3):
        board.setRowColumn(0, i, 1)
    assert board.checkWinningCondition() == True

def test_check_winning_condition_win_column():
    board = Board()
    for i in range(3):
        board.setRowColumn(i, 0, 0)
    assert board.checkWinningCondition() == True

def test_check_winning_condition_win_diagonal():
    board = Board()
    for i in range(3):
        board.setRowColumn(i, i, 1)
    assert board.checkWinningCondition() == True

def test_get_winning_player_no_winner():
    board = Board()
    assert board.getWinningPlayer() == -1

def test_get_winning_player_winner():
    board = Board()
    for i in range(3):
        board.setRowColumn(i, i, 1)
    assert board.getWinningPlayer() == 1

def test_check_rows_no_winner():
    board = Board()
    assert board.checkRows() == -1

def test_check_rows_winner():
    board = Board()
    for i in range(3):
        board.setRowColumn(0, i, 1)
    assert board.checkRows() == 1

def test_check_columns_no_winner():
    board = Board()
    assert board.checkColumns() == -1

def test_check_columns_winner():
    board = Board()
    for i in range(3):
        board.setRowColumn(i, 0, 0)
    assert board.checkColumns() == 0

def test_check_diagonals_no_winner():
    board = Board()
    assert board.checkDiagonals() == -1

def test_check_diagonals_winner():
    board = Board()
    for i in range(3):
        board.setRowColumn(i, i, 1)
    assert board.checkDiagonals() == 1

def test_check_values_for_win_no_winner():
    board = Board()
    assert board.checkValuesForWin([-1, 0, 1]) == -1

def test_check_values_for_win_winner():
    board = Board()
    assert board.checkValuesForWin([1, 1, 1]) == 1
    assert board.checkValuesForWin([0, 0, 0]) == 0