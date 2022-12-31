import numpy as np
import random
from random import randint

grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]

def numberofzeros():
    zeros = []
    for i in range(0,9):
        zeros.append(grid[i].count(0))
        totalzeros = sum(zeros)
    return totalzeros


def removegridsquares(grid):
    #first need to recognise the non zero squares
    initialzeros = numberofzeros()
    for i in range(0,500):
        x1 = randint(0,8)
        y1 = randint(0,8)
        if grid[x1][y1] != 0:
            if initialzeros < 64:
                grid[x1][y1] = 0
                initialzeros = initialzeros + 1
    print(np.matrix(grid))

removegridsquares(grid)