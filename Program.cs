using System;
using System.Text.RegularExpressions;


class Program
{

    static void parseUserInput(string input)
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
            int x = int.Parse(match.Groups[1].Value);
            int y = int.Parse(match.Groups[2].Value);
        }

    }



    static void Main()
    {
        Board board = new();
        Console.WriteLine(board);
    }
}