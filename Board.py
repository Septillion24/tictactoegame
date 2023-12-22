from typing import List, Optional

class Board:
    def __init__(self) -> None:
        self.rows: List[List[Optional[int]]] = [[None,None,None],[None,0,None],[None,None,None]]
        pass
    
    def getBoardRows(self):
        return self.rows
    
    def setRowColumn(self, x:int, y:int, value:int) -> None:
        if(value != 1 and value != 0):
            raise Exception
        print("Trying to replace value " + x.__str__() + ", " + y.__str__() + " to " + value.__str__() + "\n Current: " + self.rows[y][x].__str__())
        self.rows[y][x] = value