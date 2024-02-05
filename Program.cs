using System;
using System.Diagnostics;
using System.Text.RegularExpressions;


class Program
{

    static Board board;
    static void parseUserInput(out int x, out int y, string input)
    {
        string pattern = @".*([0-2]).*([0-2]).*";
        Regex regex = new Regex(pattern);
        Match match = regex.Match(input);
        if(!match.Success)
        {
            throw new ArgumentException();
        }
        else
        {
            x = int.Parse(match.Groups[1].Value);
            y = int.Parse(match.Groups[2].Value);
        }

    }

    static void doTurn()
    {
        //X
        Console.Write(board + "Input move for X: ");
        int x;
        int y;
        parseUserInput(out x,out y,Console.ReadLine());
        board.setRowColumns(x,y,1);

        //O
        Console.Write(board + "Input move for O: ");
        parseUserInput(out x,out y,Console.ReadLine());
        board.setRowColumns(x,y,2);
    }




    static void Main()
    {
        board = new();
        Console.WriteLine(board);
    }
}