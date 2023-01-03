import numpy as np
import random

grid = [[(i + k) % 9 + 1 for i in range(1, 10)] for k in range(9)]
random.shuffle(grid)
grid = [[grid[x][y] for x in range(9)] for y in range(9)]
print(np.matrix(grid))
