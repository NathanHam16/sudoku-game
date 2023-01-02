from random import randint, shuffle
from time import sleep
import numpy as np
import random
import copy

#Initialise 9x9 grid with 0's
grid = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,9,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],]

# grid = [[5,3,0,0,7,0,0,0,0],
#         [6,0,0,1,9,5,0,0,0],
#         [0,9,8,0,0,0,0,6,0],
#         [8,0,0,0,6,0,0,0,3],
#         [4,0,0,8,0,3,0,0,1],
#         [7,0,0,0,2,0,0,0,6],
#         [0,6,0,0,0,0,2,8,0],
#         [0,0,0,4,1,9,0,0,5],
#         [0,0,0,0,8,0,0,0,0],]

grid_copy = []

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
    number_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(number_list) #Shuffles the first row of the solution
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0: #Runs only if square is 0
                for number in number_list: #Iterates at a random order to determine possible results
                    if possible(row, column, number): #If the random number can be a solution to the square
                        grid[row][column] = number #Assign this number to the square
                        solve(grid)
                        grid[row][column] = 0
                return
    grid_copy = copy.deepcopy(grid)
    print(np.matrix(grid))
    return


import random

def generate_sudoku():
  grid = [[0 for _ in range(9)] for _ in range(9)]
  tried = [[[False for _ in range(9)] for _ in range(9)] for _ in range(9)]
  
  def is_valid(grid, row, col, num):
    for i in range(9):
      if grid[row][i] == num:
        return False
    for i in range(9):
      if grid[i][col] == num:
        return False
    start_row = row // 3 * 3
    start_col = col // 3 * 3
    for i in range(3):
      for j in range(3):
        if grid[start_row + i][start_col + j] == num:
          return False
    return True

  def generate(grid, tried):
    row = col = 0
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
      if is_valid(grid, row, col, num) and not tried[row][col][num-1]:
        grid[row][col] = num
        tried[row][col][num-1] = True
        if col == 8:
          col = 0
          row += 1
        else:
          col += 1
        if row == 9:
          return True
      else:
        if col > 0:
          col -= 1
        elif row > 0:
          row -= 1
          col = 8
        else:
          return False
      if not generate(grid, tried):
        grid[row][col] = 0
        tried[row][col][num-1] = False
        if col > 0:
          col -= 1
        elif row > 0:
          row -= 1
          col = 8
        else:
          return False
    return True
  
  if not generate(grid, tried):
    print("Error: Could not generate a valid Sudoku grid")
    return None
  return grid
