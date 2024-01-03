from Board import Board
import re

class Main:
    
    def __init__(self):
        self.gameBoard = Board()

    def run(self):
        end = False
        while(not end):
            end = self.doGame()
            
            
        
    
    
    def doGame(self):
        winningPlayer = -1
        currentPlayer = 1
        while(winningPlayer == -1):

            self.promptUserInput(currentPlayer)
            # print(self.gameBoard.checkWinningCondition())
            winningPlayer = self.gameBoard.getWinningPlayer()
            
            currentPlayer = (0 if currentPlayer == 1 else 1)
        if(winningPlayer == -2):
            print("There was a tie!\n")
        else:
            winningPlayerText = "x" if winningPlayer == 1 else "o"
            print("Winner: " + winningPlayerText)
        print("Would you like to play again? (y/n)")
        if(input("> ") != "y"):
            return False
        
    def promptUserInput(self, currentPlayer:int):
        self.displayBoard()
        currenPlayerText = ("x" if currentPlayer == 1 else "o")
        validInput = False
        while(not validInput):
            print("---\nEnter the coordinates for player " + currenPlayerText)
            userInput = input("> ")
            matches = re.findall(r'\D*([0-2]{1})\D*([0-2]{1})\D*', userInput)

            if matches:
                xInput = matches[0][0]
                yInput = matches[0][1]
                if self.gameBoard.getRowColumn(int(xInput),int(yInput)) == -1:
                    self.gameBoard.setRowColumn(int(xInput),int(yInput),currentPlayer)
                    validInput = True
                else:
                    print("Error: Spot already taken. Please try again.\n")
            else:
                print("Error: Invalid input. Please try again. \n")
            
            
        
    def displayBoard(self) -> None:
        print(self.gameBoard.getBoardTextDisplay())

        

if __name__ == "__main__":
    main = Main()
    main.run()
