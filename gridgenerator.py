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
    solve(grid)
    return grid_copy


#This function solves the given grid. Furthermore, it iterates through the number list randomly
#Because this function is also used to generate a completely random solution given a grid of 0's
def solve(grid):
    global grid_copy
    base  = 3
    side  = 9

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    grid = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    grid_copy = copy.deepcopy(grid)



