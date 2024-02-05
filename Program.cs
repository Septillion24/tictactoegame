using System;
using System.Diagnostics;
using System.Text.RegularExpressions;


class Program
{

    static void parseUserInput(out int x, out int y, string input)
    {
        string pattern = @".*([0-2]).*([0-2]).*";
        Regex regex = new Regex(pattern);
        Match match = regex.Match(input);
        if (!match.Success)
        {
            throw new ArgumentException();
        }
        else
        {
            y = int.Parse(match.Groups[1].Value);
            x = int.Parse(match.Groups[2].Value);
        }

    }

    static int doTurn()
    {
        int winner;
        //X
        Console.Write(board + "\nInput move for X: ");
        int x;
        int y;
        parseUserInput(out x, out y, Console.ReadLine());
        board.setRowColumns(x, y, 1);
        winner = board.checkWinner();
        if(winner != 0)
        {
            return winner;
        }

        //O
        Console.Write(board + "\nInput move for O: ");
        parseUserInput(out x, out y, Console.ReadLine());
        board.setRowColumns(x, y, 2);
        winner = board.checkWinner();
        return winner;
    }


    static Board board;
    
    static void Main()
    {
        board = new Board();
        int winner = 0;
        // Console.WriteLine(board);
        while (winner == 0)
        {
            winner = doTurn();
        }
        Console.WriteLine(board);
        if(winner == 1)
        {
            Console.WriteLine("X wins!");
        }
        else
        {
            Console.WriteLine("O wins!");
        }
    }
}