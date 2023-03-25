import numpy as np
import copy 

class Solver:
    def __init__(self,n):
        self.n = n
    def solve(self,grid: np.ndarray) -> bool | np.ndarray:
        pass
    def validate_entry(self,grid: np.ndarray, x: int, y: int, value: int) -> bool:
        for i in range(self.n*self.n):
            if grid[x][i]== value:
                return False
            if grid[i][y]== value:
                return False
        large_row = (x//self.n) * self.n
        large_col = (y//self.n) * self.n
        for i in range(large_row, large_row + self.n):
            for j in range (large_col, large_col + self.n):
                if grid[i][j]== value:
                    return False
        return True

class Backtracking(Solver):
    def __init__(self):
        super().__init__(self)
    def solve(self,grid: np.ndarray)-> bool | np.ndarray:
        new_board = copy.deepcopy(grid)
        for i in range(self.n*self.n):
            for j in range(self.n*self.n):
                if grid[j][i] == 0:
                    for k in range(1,self.n*self.n+1):
                        if self.validate_entry(grid, j, i, k):
                            new_board[j][i] = k
                            result = self.solve(new_board)
                            if type(result) is np.ndarray:
                                return result
                    return False
        return grid

class StochasticSolver(Solver):
    def __init__(self):
        super().__init__(self)
    def evaluate_score(self, grid: np.ndarray) -> int:
        '''Return a score with larger score being worse, smaller is better''' 
    def augment_grid(self, grid: np.ndarray) -> np.ndarray:
        pass
    def 



