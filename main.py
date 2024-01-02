from Board import Board

class Main:
    
    def __init__(self):
        self.gameBoard = Board()

    def run(self):
        end = False
        while(not end):
            end = self.doGame()
            
            
        
    
    
    def doGame(self):
        self.displayBoard(self.gameBoard)
        
        if(self.gameBoard.checkWinningCondition()):
            return True
        
        
        
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
