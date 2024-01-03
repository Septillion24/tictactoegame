from typing import List, Optional

class Board:
    def __init__(self) -> None:
        self.rows: List[List[int]] = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        pass
    
    def getBoardRows(self):
        return self.rows
    
    def setRowColumn(self, x:int, y:int, value:int) -> None:
        #0 is o, 1 is x
        #-1 is unset.
        if(value != 1 and value != 0):
            raise Exception
        # print("Trying to replace value " + x.__str__() + ", " + y.__str__() + " to " + value.__str__() + "\n Current: " + self.rows[y][x].__str__())
        self.rows[y][x] = value
    
    def getRowColumn(self, x:int, y:int) -> Optional[int]:
        return self.rows[y][x]
        
    def checkWinningCondition(self) -> bool:
        if self.getWinningPlayer() == -1:
            return False
        else:
            return True
    
    def getWinningPlayer(self) -> int:
        # 0 is o, 1 is x
        # -1 means no winner yet
        # -2 means tie
        
        winner = self.checkRows()
        if winner != -1:
            print("Winning condition found through rows.")
            print("Winning table:" + self.rows.__str__())
            return winner
        winner = self.checkColumns()
        if winner != -1:
            print("Winning condition found through columns")
            return winner
        winner = self.checkDiagonals()
        if winner != -1:
            print("Winning condition found through diagonals")
            return winner
        if self.checkTie():
            return -2
    
        return winner
    
    
    def checkTie(self):
        for x in range(3):
            for y in range(3):
                if self.getRowColumn(x,y) == -1:
                    return False
        return True

    def checkRows(self) -> int:
        winner = -1
        for row in self.rows:
            values = []
            for value in row:
                values.append(value)
            winner = self.checkValuesForWin(values)
            if(winner != -1):
                return winner
        return winner
    
    def checkColumns(self) -> int:
        winner = -1
        for column in range(3):
            values = []
            for row in range(3):
                values.append(self.getRowColumn(row, column))
            winner = self.checkValuesForWin(values)
            if(winner != -1):
                return winner
        return winner
        
    def checkDiagonals(self) -> int:
        winner = -1
        values = []
        for x in range(3):
            values.append(self.getRowColumn(x,x))
        winner = self.checkValuesForWin(values)
        if(winner != -1):
            return winner
        
        values = []
        for x in range(3):
            values.append(self.getRowColumn(x,2-x))
        winner = self.checkValuesForWin(values)
        return winner
    

    def checkValuesForWin(self, values):
        if len(set(values)) == 1:
            if values[0] == -1:
                return -1
            else:
                return values[0]
        else:
            return -1

    def getBoardTextDisplay(self) -> str:
        text = "\033[4m  | 0 | 1 | 2 |\033[0m\n"
        rowNumber = -1
        for row in self.rows:
            rowNumber+=1
            text += rowNumber.__str__() + " | "
            for value in row:
                if value == 1:
                    text += "x | "
                elif value == 0:
                    text += "o | "
                elif value == -1:
                    text +="  | "
            text += "\n"
        return text

                    
                        
                        
        