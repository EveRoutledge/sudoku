import numpy as np
import sys
#note to self grid[row, column]

class Sudoku:
    def __init__(self):
        self.grid = np.zeros((8,8))
        self.grid[:,0] = [1,3,5,7,2,4,6,8]
        self.grid[:4,1] = [2,4,6,8]
        self.count = 0

    def solve(self)-> int:
        x,y,complete= self.empty_cell()
        count=0
        if not complete:
            valid_vals = np.setdiff1d(np.array([1,2,3,4,5,6,7,8]),self.grid[:,x])
            valid_vals=np.setdiff1d(valid_vals,self.grid[y,:])
            sash = y//4
            pillar = x//2
            valid_vals = np.setdiff1d(valid_vals,self.grid[sash*4:sash*4+4,pillar*2:pillar*2+2].flatten())
            # box constraint
            if valid_vals.size == 0:
                return 0
            else:
                for val in valid_vals:
                    #transform grid
                    self.grid[y,x] = val
                    count += self.solve()
                    print(count)
                    # de transform grid 
                    self.grid[y,x] = 0
        else:
            return 1
        return count

    def empty_cell(self):
        for j in range(4,8):
            if self.grid[j,1]==0:
                return (j,1,False)
        for i in range(2,8):
            for j in range(0,4):
                if self.grid[j,i]==0:
                    return (i,j,False)
        for j in range(4,8):
            for i in range(2,8):
                if self.grid[j,i]==0:
                    return (i,j,False)
        return (0,0,True)
    def print(self):
        print(np.array_str(self.grid, precision=0, suppress_small=True))

sys.setrecursionlimit(2000)
print(Sudoku().solve())
