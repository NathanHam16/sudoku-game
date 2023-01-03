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

def solve():
    width = 9
    board = [[(i + k) % 9 + 1 for i in range(1, width + 1)] for k in range(width)] # Creates a board where each row counts to 9 such that no row contains more than one kind of each number. You can run this separately to see what it generates.
    random.shuffle(board) # Shuffles this list of lists
    board = [[board[x][y] for x in range(9)] for y in range(9)] # Reads each row and puts it into a column. (basically rotates it to its side)
    random.shuffle(board) # Shuffles this list again but while its on its side
    return board


