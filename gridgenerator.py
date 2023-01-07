from random import randint, shuffle
from time import sleep
import numpy as np
import random
import copy

global grid
grid = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],]

# A function to check if the grid is full
def checkGrid(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                return False

def possible(row,column,number): #This function checks if an input is possible
    global grid
    for i in range(0,9): #Does the number exist in this row?
        if grid[row][i] == number:
            return False
    for i in range(0,9): #Does the number exist in this column?
        if grid[i][column] == number:
            return False
    x0 = (column // 3) * 3 #Does the number exists in this 3x3 square?
    y0 = (row // 3) * 3
    for i in range (0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == number:
                return False
    return True

def get_grid():
    grid_copy = solve()
    return grid_copy

#This algorithm creates a valid grid where each number on the diagonal are the same, and shuffles each row.
#It is important that the grid is rotated before shuffling a second time to still be a valid sudoku solution.
# def solve():
#     # Creates a grid where each row and column counts to 9, so that each number on the diagonal are the same.
#     grid = [[(i + k) % 9 + 1 for i in range(1, 10)] for k in range(9)]
#     # Shuffles this list of lists
#     random.shuffle(grid)
#     # Reads each row and puts it into a column. (basically rotates it to its side)
#     grid = [[grid[x][y] for x in range(9)] for y in range(9)]
#     # Shuffles this list again but while its on its side
#     random.shuffle(grid)
#     return grid

def solve():
    global grid
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce grid using randomized baseline pattern
    grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]   
    return grid


    


