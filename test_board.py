import pytest
from Board import Board

def test_board_initialization():
    board = Board()
    assert board.getBoardRows() == [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

def test_set_row_column():
    board = Board()
    board.setRowColumn(0, 0, 1)  # Set 'x' at (0, 0)
    assert board.getRowColumn(0, 0) == 1

def test_set_row_column_invalid_value():
    board = Board()
    with pytest.raises(Exception):
        board.setRowColumn(0, 0, 2)  # Invalid value

def test_check_winning_condition():
    board = Board()
    assert board.checkWinningCondition() == False

def test_get_winning_player_no_winner():
    board = Board()
    assert board.getWinningPlayer() == -1

def test_check_rows_no_winner():
    board = Board()
    assert board.checkRows() == -1

def test_check_columns_no_winner():
    board = Board()
    assert board.checkColumns() == -1

def test_check_diagonals_no_winner():
    board = Board()
    assert board.checkDiagonals() == -1

def test_check_values_for_win_no_winner():
    board = Board()
    assert board.checkValuesForWin([-1, 0, 1]) == -1

# Add more tests to check the game logic
def test_check_rows_winner():
    board = Board()
    board.setRowColumn(0, 0, 1)  # Set 'x' at (0, 0)
    board.setRowColumn(1, 0, 1)  # Set 'x' at (1, 0)
    board.setRowColumn(2, 0, 1)  # Set 'x' at (2, 0)
    assert board.checkRows() == 1

def test_check_columns_winner():
    board = Board()
    board.setRowColumn(0, 0, 0)  # Set 'o' at (0, 0)
    board.setRowColumn(0, 1, 0)  # Set 'o' at (0, 1)
    board.setRowColumn(0, 2, 0)  # Set 'o' at (0, 2)
    assert board.checkColumns() == 0

def test_check_values_for_win_winner():
    board = Board()
    assert board.checkValuesForWin([1, 1, 1]) == 1  # 'x' wins
    assert board.checkValuesForWin([0, 0, 0]) == 0  # 'o' wins
    
def test_check_diagonals_winner():
    board = Board()
    board.setRowColumn(0, 0, 1)  # Set 'x' at (0, 0)
    board.setRowColumn(1, 1, 1)  # Set 'x' at (1, 1)
    board.setRowColumn(2, 2, 1)  # Set 'x' at (2, 2)
    assert board.checkDiagonals() == 1