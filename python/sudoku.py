import numpy as np


class Sudoku:
    def __init__(self, grid: np.ndarray, n: int):
        self.array = grid
        self.n = n
    def __str__(self):
        '''Print object-> print()'''
    def __getitem__(self, key: int) -> int:
        return self.array[key]
    def __setitem__(self, key:int, value)-> None:
        self.array[key] = value
    
    