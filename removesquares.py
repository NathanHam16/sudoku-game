from gridgenerator import solve
from random import randint
import random

# Removes grid squares until number of squares are removed
def removegridsquares(grid, difficulty):
    attempts = 0
    if (difficulty == "Difficulty: Easy"):
        attempts = 40
    elif (difficulty == "Difficulty: Medium"):
        attempts = 55
    elif (difficulty == "Difficulty: Hard"):
        attempts = 60

    h, w, r = len(grid), len(grid[0]), []
    spaces = [[x, y] for x in range(h) for y in range(w)]
    for k in range(attempts):
        r = random.choice(spaces)
        grid[r[0]][r[1]] = 0
        spaces.remove(r)
    return grid


    # while attempts>0:
    #     row = randint(0,8)
    #     col = randint(0,8)
    #     while grid[row][col]==0:
    #         row = randint(0,8)
    #         col = randint(0,8)
    #     backup = grid[row][col]
    #     grid[row][col]=0
        
    zeros = 0
    while (zeros < attempts):
        backup
        x1 = randint(0,8)
        y1 = randint(0,8)
        if zeros < attempts:
            if grid[x1][y1] != 0:
                backup = grid[x1][y1]
                grid[x1][y1] = 0
                zeros += 1
                
#         #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
#         counter=0      
#         solve(copyGrid)   
#         #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
#         if counter!=1:
#             grid[row][col]=backup
#             #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
#             attempts -= 1                

# #A higher number of attempts will end up removing more numbers from the grid
# #Potentially resulting in more difficiult grids to solve!
# def removegridsquares(grid, difficuilty):
#     attempts = 5 
#     counter=1
#     while attempts>0:
#     #Select a random cell that is not already empty
#         row = randint(0,8)
#         col = randint(0,8)
#         while grid[row][col]==0:
#             row = randint(0,8)
#             col = randint(0,8)
#         #Remember its cell value in case we need to put it back  
#         backup = grid[row][col]
#         grid[row][col]=0
        
#         #Take a full copy of the grid
#         copyGrid = []
#         for r in range(0,9):
#             copyGrid.append([])
#             for c in range(0,9):
#                 copyGrid[r].append(grid[r][c])
        
#         #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
#         counter=0      
#         solve(copyGrid)   
#         #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
#         if counter!=1:
#             grid[row][col]=backup
#             #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
#             attempts -= 1

  
                