using System.Data;
using System.Security.Cryptography.X509Certificates;

class Board
{
    private int[][] board = new int[3][];
    // 0 is no one
    // 1 is x
    // 2 is o

    public Board()
    {
        reset();
    }

    public void reset()
    {
        for (int x = 0; x < 3; x++)
        {
            board[x] = new int[3];
            for (int y = 0; y < 3; y++)
            {
                board[x][y] = 0;
            }
        }
    }

    public int setRowColumns(int row, int column, int value)
    {
        if (value > 2 || value < 0)
        {
            throw new ArgumentException();
        }
        int previousValue = board[row][column];
        board[row][column] = value;
        return previousValue;
    }

    public int getRowColumn(int row, int column)
    {
        return board[row][column];
    }

    public override string ToString()
    {
        string outputString = "";
        for (int y = 0; y < 3; y++)
        {
            outputString += "\n[";
            outputString += string.Join(",", board[y]);
            outputString += "]";
        }
        return outputString;
    }

    public int checkWinner()
    {
        int winner = 0;
        //0 is no winner
        // 1 is X
        // 2 is O

        for (int i = 0; i < 3; i++)
        {
            winner = checkHorizontal(i);
            if (winner != 0)
            {
                return winner;
            }
        }
        for (int i = 0; i < 3; i++)
        {
            winner = checkVertical(i);
            if (winner != 0)
            {
                return winner;
            }
        }
        winner = checkDiagonal();
        return winner;

        int checkDiagonal()
        {
            winner = 0;
            int[] ascendingDiagonal = new int[3];
            for (int i = 0; i < 3; i++)
            {
                ascendingDiagonal[i] = getRowColumn(i, i);
            }
            winner = getWinnerFromArray(ascendingDiagonal);
            if (winner != 0)
            {
                return winner;
            }
            int[] descendingDiagonal = new int[3];
            for (int i = 0; i < 3; i++)
            {
                descendingDiagonal[i] = getRowColumn(i, 2 - i);
            }
            winner = getWinnerFromArray(descendingDiagonal);


            return winner;
        }
        int checkHorizontal(int row)
        {
            winner = 0;
            int[] rowArray = board[row];
            winner = getWinnerFromArray(rowArray);

            return winner;
        }
        int checkVertical(int column)
        {
            winner = 0;
            int[] columnArray = new int[3];
            for (int row = 0; row < 3; row++)
            {
                columnArray[row] = board[column][row];
            }
            winner = getWinnerFromArray(columnArray);
            return winner;
        }
        int getWinnerFromArray(int[] array)
        {
            if (array.Contains(0))
            {
                return 0;
            }
            else if (array.Contains(1) && array.Contains(2))
            {
                return 0;
            }
            else
            {
                return array[0];
            }
        }

    }



}