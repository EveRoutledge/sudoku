import random
import math
import numpy as np

def simulated_annealing(grid,schedule=None,max_t=1000,tau = 10,epsilon = 0.01):
    if schedule == None:
        schedule = np.fromfunction(lambda i: math.exp(-i/tau),(max_t), dtype = float)
    badness_grid = init_badness_grid(grid)
    current = fill_init_grid(grid)
    badness_val, badness_grid = update_badness_grid(current,badness_grid)
    # add best
    t=0
    while t < max_t:
        T = schedule[t]
        if T <= epsilon:
            return current
        else:
            succ = gen_successor(current,badness_grid)
            if gen_successor == False:
                return current
            new_badness_val, new_badness_grid = update_badness_grid(succ, badness_grid)
            if new_badness_val == 0:
                return succ
            delta_e = badness_val - new_badness_val
            if delta_e >= 0:
                current = succ
                badness_val = new_badness_val
                badness_grid = new_badness_grid
            else:
                if random.random() < math.exp(delta_e/T):
                    current = succ
                    badness_val = new_badness_val
                    badness_grid = new_badness_grid

def init_badness_grid(grid):
    return np.fromfunction(lambda i,j: -1 if grid[i][j]!=0 else 0,(len(grid),len(grid)))

def update_badness_grid(grid,badness_grid,n):
    badness = np.fromfunction(lambda i,j: 0 if badness_grid[i][j] == -1 else cell_badness(grid,i,j,n),(len(grid),len(grid)))
    return np.sum(badness), badness

def fill_init_grid(grid):
    return np.fromfunction(lambda i,j: grid[i][j] if grid[i][j]!=0 else random.randint(1,9),(len(grid),len(grid)), dtype=int)

def gen_successor(grid, badness_grid, n):
    coords = np.argmax(badness_grid)
    bad = badness_grid[coords[0]][coords[1]]
    val = grid[coords[0]][coords[1]]
    for i in range(1,n*n+1):
        if i != val:
            grid[coords[0]][coords[1]] = i
            if cell_badness(grid, coords[0], coords[1], n)<bad:
                return grid
    badness_grid[coords[0],coords[1]] = 0
    if bad == 0:
        return False

def cell_badness(grid,x,y,n):
    value = grid[x][y]
    bad = 0
    for i in range(n*n):
        if grid[x][i] == value:
            if i != y:
                bad+=1
        if grid[i][y] == value:
            if i != x:
                bad+=1
    large_row = (x//n) * n
    large_col = (y//n) * n
    for i in range(large_row, large_row + n):
        for j in range (large_col, large_col + n):
            if grid[i][j] == value:
                if not (i == x and j == y):
                    bad += 1
    return bad
