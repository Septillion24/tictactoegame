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
        return False
    
    def getWinningPlayer(self) -> int:
        # 0 is o, 1 is x
        # -1 means no winner

        if not self.checkWinningCondition():
            return -1
        else:
            winner = self.checkRows()
            if winner != -1:
                return winner
            winner = self.checkColumns()
            if winner != -1:
                return winner
            # winner = self.checkDiagonals()
            return winner

    def checkRows(self) -> int:
        winner = -1
        for row_num, row in enumerate(self.rows):
            values = []
            for col_num, value in enumerate(row):
                values.append(self.getRowColumn(col_num, row_num))
            winner = self.checkValuesForWin(values)
            if(winner != -1):
                return winner
        return winner
    
    def checkColumns(self) -> int:
        winner = -1
        for i in range(3):
            values = []
            for row_num, row in enumerate(self.rows):
                values.append(self.getRowColumn(row_num, i))
            winner = self.checkValuesForWin(values)
            if(winner != -1):
                return winner
        return winner
        

    def checkValuesForWin(self, values) -> int:
        win = not 1 in values and 0 in values and not None in values
        if win and 1 in values:
            winner = 1
        else:
            winner = 0
        if not win:
            winner = -1
        return winner
                    

                    
                        
                        
        