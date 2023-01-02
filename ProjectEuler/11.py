import numpy as np

import lib

grid = np.asarray(lib.file_to_ints('11.txt'))
max_prod = 0

for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
        if r + 3 < grid.shape[0]:
            max_prod = max(max_prod, grid[r, c] * grid[r + 1, c] * grid[r + 2][c] * grid[r + 3][c])
        if c + 3 < grid.shape[1]:
            max_prod = max(max_prod, grid[r, c] * grid[r, c + 1] * grid[r][c + 2] * grid[r][c + 3])
        if r + 3 < grid.shape[0] and c + 3 < grid.shape[1]:
            max_prod = max(max_prod, grid[r, c] * grid[r + 1, c + 1] * grid[r + 2][c + 2] * grid[r + 3][c + 3])
        if r + 3 < grid.shape[0] and c - 3 >= 0:
            max_prod = max(max_prod, grid[r, c] * grid[r + 1, c - 1] * grid[r + 2][c - 2] * grid[r + 3][c - 3])

print(max_prod)
