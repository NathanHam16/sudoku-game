import numpy as np
import random

# 9x9 grid of 0's
grid = [[0 for i in range(9)] for j in range(9)]


def possible(row, column, number):
    global grid

    # Does the number exist in this row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Does the number exist in this column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # Does the number exists in this 3x3 square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False
    return True


#Generates a random complete solution with backtracking
def solution(grid):
    grid = []
    number_list = [1,2,3,4,5,6,7,8,9]
    for i in range (0,9):
        random.shuffle(number_list)
        grid.append(number_list)
        print(number_list)
    
    
    
    for i in range(0,81):
        row = i // 9
        column = i % 9
#        if grid[row][column] == 0:
#             if self.possible(row, column, element):
#                 self.grid.append((element, row, column))
#            grid[row][column] = element
