import numpy as np
import random
from random import randint

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

#This function solves the given grid. Furthermore, it iterates through the number list randomly
#Because this function is also used to generate a completely random solution given a grid of 0's
def solve():
    global grid
    number_list = [1,2,3,4,5,6,7,8,9]
    random.shuffle(number_list) #Shuffles the first row of the solution
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in number_list: #Iterates at a random order to determine possible results
                    if possible(row,column, number): #If the random number can be a solution to the square
                        grid[row][column] = number #Assign this number to the square
                        solve()
                        grid[row][column] = 0
                return  
    print(np.matrix(grid))
    input("More Solutions")