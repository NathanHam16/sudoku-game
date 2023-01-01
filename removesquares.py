from gridgenerator import solve
from random import randint

# Removes grid squares until number of squares are removed
def removegridsquares(grid, difficulty):
    squarestoremove = 0
    if (difficulty == "Difficulty: Easy"):
        squarestoremove = 45
    elif (difficulty == "Difficulty: Medium"):
        squarestoremove = 55
    elif (difficulty == "Difficulty: Hard"):
        squarestoremove = 60

    zeros = 0
    while (zeros < squarestoremove):
        x1 = randint(0,8)
        y1 = randint(0,8)
        if zeros < squarestoremove:
            if grid[x1][y1] != 0:
                grid[x1][y1] = 0
                zeros += 1
                