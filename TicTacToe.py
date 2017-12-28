class TicTacToe:
    nmoves=0
    grid=[[]]
    # values in grid: 0=blank, 1=x, 2=o
    currentPlayer=1

    winLines=['123','456','789',
              '147','258','369',
              '159','357']
    lines={}
    
    def __init__(self):
        # Start by allocating the grid and doing initial setup

        self.grid=[[0 for j in range(3)] for i in range(3)]
        self.nmoves=0
        self.currentPlayer=1
        for l in self.winLines:
            self.lines[l]=[3,0,0]
    
    def returnCell(self, num):
        y0=int((num-1)/3)
        x0=(num-1)%3
        if self.grid[x0][y0]==0:
            return '-'
        elif self.grid[x0][y0]==1:
            return "X"
        elif self.grid[x0][y0]==2:
            return 'O'
        else: # should not happen, but...
            return "?"
        
    def printGrid(self):
        print("%s|%s|%s" % (self.returnCell(1), self.returnCell(2), self.returnCell(3)))
        print("%s|%s|%s" % (self.returnCell(4), self.returnCell(5), self.returnCell(6)))
        print("%s|%s|%s" % (self.returnCell(7), self.returnCell(8), self.returnCell(9)))
        
    def userMove(self, cellNum, player):
        """ cellNum is from 1-9; player is either 1 (X) or 2 (Y)"""
        y0=int((cellNum-1)/3)
        x0=(cellNum-1)%3
        s0="%d"%cellNum
        
        if self.grid[x0][y0]==0:
            self.grid[x0][y0]=player
            self.nmoves=self.nmoves+1
            for i in self.lines.keys():
                if s0 in i:
                    self.lines[i][0]=self.lines[i][0]-1
                    self.lines[i][player]=self.lines[i][player]+1

    @property
    def checkGrid(self):
        # Checks for win conditions
        for i in self.lines.keys():
            if self.lines[i][1]==3:
                print("X has won!")
                return True
            if self.lines[i][2]==3:
                print("O has won!")
                return True
        return False

a=TicTacToe()
a.printGrid()
a.userMove(2,1)
a.printGrid()
print(a.lines)
