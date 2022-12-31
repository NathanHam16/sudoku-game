import numpy as np
import random
from random import randint

initialgrid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0],]
grid = initialgrid
# grid = [[0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,1,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],]

#This function checks if an input is possible
def possible(row,column,number):
    global grid

    #Does the number exist in this row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Does the number exist in this column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    #Does the number exists in this 3x3 square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range (0,3):
        for j in range (0,3):
            if grid[y0+i][x0+j] == number:
                return False
    return True

#This function solves the given grid. Furthermore, it iterates through the number list randomly
#Because this function is also used to generate a completely random solution given a grid of 0's
def solve(grid):
    number_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(number_list) #Shuffles the first row of the solution
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in number_list: #Iterates at a random order to determine possible results
                    if possible(row,column, number): #If the random number can be a solution to the square
                        grid[row][column] = number #Assign this number to the square
                        solve(grid)
                        grid[row][column] = 0
                return

    print(np.matrix(grid))
    input('More Possible Solutions')

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
                gridcopy = grid.copy
                initialzeros = initialzeros + 1
                if solve(gridcopy) == solve(initialgrid):
                    
    print(np.matrix(grid))
    
removegridsquares(grid)

#if solving after removing a square still results in the same solution
grid = solve(grid)