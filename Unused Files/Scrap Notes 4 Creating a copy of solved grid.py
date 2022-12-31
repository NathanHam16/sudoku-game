import numpy as np
import random
from random import randint
import copy




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

class Solution(object):
    global gridcopy
    global grid
    grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,1,0,0],]
    
    def solve(gridcopy: object):
        number_list = [1,2,3,4,5,6,7,8,9]
        random.shuffle(number_list) #Shuffles the first row of the solution
        print(grid)
#         for row in range(0,9):
#             for column in range(0,9):
#                 if grid[row][column] == 0:
#                     for number in number_list:
#                         if possible(row, column, number):
#                             grid[row][column] = number
#                             solve()
#                             grid[row][column] = 0
#                     return
        gridcopy.matrixGrid = np.matrix(grid)              
                
    problem = object()
    solve(problem)

    print(problem.matrixGrid)               

