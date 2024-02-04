using System.Data;

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
            outputString+="\n[";
            outputString += string.Join(",", board[y]);
            outputString+="]";
        }

        return outputString;
    }

}