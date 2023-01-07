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
  
                