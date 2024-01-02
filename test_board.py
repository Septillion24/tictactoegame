import pytest
from Board import Board

@pytest.fixture
def board():
    return Board()

def test_initialization(board):
    assert board.getBoardRows() == [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

def test_setRowColumn(board):
    board.setRowColumn(0, 0, 1)
    assert board.getRowColumn(0, 0) == 1
    with pytest.raises(Exception):
        board.setRowColumn(0, 0, 2)

def test_checkWinningCondition(board):
    assert board.checkWinningCondition() == False

def test_getWinningPlayer(board):
    assert board.getWinningPlayer() == -1

def test_checkRows(board):
    board.setRowColumn(0, 0, 1)
    board.setRowColumn(1, 0, 1)
    board.setRowColumn(2, 0, 1)
    assert board.checkRows() == 1

def test_checkColumns(board):
    board.setRowColumn(0, 0, 1)
    board.setRowColumn(0, 1, 1)
    board.setRowColumn(0, 2, 1)
    assert board.checkColumns() == 1

def test_checkValuesForWin(board):
    assert board.checkValuesForWin([1, 1, 1]) == 1
    assert board.checkValuesForWin([0, 0, 0]) == 0
    assert board.checkValuesForWin([-1, -1, -1]) == -1