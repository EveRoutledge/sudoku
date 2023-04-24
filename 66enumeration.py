import numpy as np
#note to self grid[row, column]

class Sudoku:
    def __init__(self, set):
        self.grid = np.zeros((6,6))
        if set=='pure':
            self.grid[0] = [1,2,3,4,5,6]
        elif set=='mixeda':
            self.grid[0] = [1,2,3,5,4,6]
        else:
            self.grid[0] = [1,2,3,6,4,5]
        self.grid[1:,0] = [3,5,2,4,6]
        self.grid[1:3,1] = [4,6]
        self.count = 0

    def solve(self)-> int:
        x,y,complete= self.empty_cell()
        count=0
        if not complete:
            valid_vals = np.setdiff1d(np.array([1,2,3,4,5,6]),self.grid[:,x])
            valid_vals=np.setdiff1d(valid_vals,self.grid[y,:])
            sash = y//3
            pillar = x//2
            valid_vals = np.setdiff1d(valid_vals,self.grid[sash*3:sash*3+3,pillar*2:pillar*2+2].flatten())
            # box constraint
            if valid_vals.size == 0:
                return 0
            else:
                for val in valid_vals:
                    #transform grid
                    self.grid[y,x] = val
                    count += self.solve()
                    # de trasform grid 
                    self.grid[y,x] = 0
        else:
            return 1
        return count

    def empty_cell(self):
        for i in range(1,6):
            for j in range(3,6):
                if self.grid[j,i]==0:
                    return (i,j,False)
        return (0,0,True)
    def print(self):
        print(np.array_str(self.grid, precision=0, suppress_small=True))

sudokus = []
counts = []
#pure
opt1=[5,6]
opt2=[1,2]
opt3=[1,2]
opt4=[3,4]
for i in range(16):
    sudoku = Sudoku('pure')
    if (i//8)%2==0:
        sudoku.grid[1,2:4] = opt1
    else:
        sudoku.grid[1,2:4] = opt1[::-1]
    if (i//4)%2==0:
        sudoku.grid[1,4:6] = opt2
    else:
        sudoku.grid[1,4:6] = opt2[::-1]
    if (i//2)%2==0:
        sudoku.grid[2,2:4] = opt3
    else:
        sudoku.grid[2,2:4] = opt3[::-1]
    if i%2==0:
        sudoku.grid[2,4:6] = opt4
    else:
        sudoku.grid[2,4:6] = opt4[::-1]
    counts.append(sudoku.solve())
    sudokus.append(sudoku.grid)


# mixed a=1
opt1=[6,1]
opt2=[5,2]
opt3=[4,2]
opt4=[3,1]
for j in range(2):
    for i in range(16):
        sudoku = Sudoku('mixeda')
        if (i//8)%2==0:
            sudoku.grid[1,2:4] = opt1
        else:
            sudoku.grid[1,2:4] = opt1[::-1]
        if (i//4)%2==0:
            sudoku.grid[1,4:6] = opt2
        else:
            sudoku.grid[1,4:6] = opt2[::-1]
        if (i//2)%2==0:
            sudoku.grid[2,2:4] = opt3
        else:
            sudoku.grid[2,2:4] = opt3[::-1]
        if i%2==0:
            sudoku.grid[2,4:6] = opt4
        else:
            sudoku.grid[2,4:6] = opt4[::-1]
        counts.append(sudoku.solve())
        sudokus.append(sudoku.grid)
    opt1=[6,2]
    opt2=[5,1]
    opt3=[4,1]
    opt4=[3,2]



# mixed a=2
opt1=[5,1]
opt2=[6,2]
opt3=[4,2]
opt4=[3,1]
for j in range(2):
    for i in range(16):
        sudoku = Sudoku('mixedb')
        if (i//8)%2==0:
            sudoku.grid[1,2:4] = opt1
        else:
            sudoku.grid[1,2:4] = opt1[::-1]
        if (i//4)%2==0:
            sudoku.grid[1,4:6] = opt2
        else:
            sudoku.grid[1,4:6] = opt2[::-1]
        if (i//2)%2==0:
            sudoku.grid[2,2:4] = opt3
        else:
            sudoku.grid[2,2:4] = opt3[::-1]
        if i%2==0:
            sudoku.grid[2,4:6] = opt4
        else:
            sudoku.grid[2,4:6] = opt4[::-1]
        counts.append(sudoku.solve())
        sudokus.append(sudoku.grid)
    opt1=[5,2]
    opt2=[6,1]
    opt3=[4,1]
    opt4=[3,2]

print(sum(counts))

