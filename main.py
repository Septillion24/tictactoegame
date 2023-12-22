from Board import Board

class Main:
    
    def __init__(self):
        self.gameBoard = Board()

    def run(self):
        self.doGame()
    
    
    def doGame(self):
        self.gameBoard.setRowColumn(1,1,1)
        self.displayBoard(self.gameBoard)
        
        
    def displayBoard(self, board:Board) -> None:
        text = ""
        for row in board.getBoardRows():
            text += "| "
            for value in row:
                if value == 1:
                    text += "x | "
                elif value == 0:
                    text += "o | "
                elif value == None:
                    text +="  | "
            text += "\n"
        print(text)
        pass

        

if __name__ == "__main__":
    main = Main()
    main.run()
