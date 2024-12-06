import lib
import numpy as np

# P1
grid = lib.file_to_mat("input.txt")
visited = np.zeros(grid.shape)

pos = np.where(grid == '^')
pos = (pos[0][0], pos[1][0])
d = [-1, 0]

while 0 <= pos[0] < grid.shape[0] and 0 <= pos[1] < grid.shape[1]:
    visited[pos[0], pos[1]] = 1
    if 0 <= pos[0] + d[0] < grid.shape[0] and 0 <= pos[1] + d[1] < grid.shape[1] and grid[pos[0] + d[0], pos[1] + d[1]] == '#':
        d = [d[1], -d[0]]
    else:
        pos = (pos[0] + d[0], pos[1] + d[1])

print(np.sum(visited))

# P2
total = 0
obs_locs = np.where(visited)
for r, c in zip(obs_locs[0], obs_locs[1]):
    pos = np.where(grid == '^')
    pos = (pos[0][0], pos[1][0])
    if r != pos[0] or c != pos[1]:
        new_grid = grid.copy()
        new_grid[r, c] = '#'
        path_dict = set()
        d = (-1, 0)

        while (0 <= pos[0] < new_grid.shape[0] and 0 <= pos[1] < new_grid.shape[1]) and (pos, d) not in path_dict:
            path_dict.add((pos, d))
            if 0 <= pos[0] + d[0] < new_grid.shape[0] and 0 <= pos[1] + d[1] < new_grid.shape[1] and new_grid[pos[0] + d[0], pos[1] + d[1]] == '#':
                d = (d[1], -d[0])
            else:
                pos = (pos[0] + d[0], pos[1] + d[1])
        total += (pos, d) in path_dict
print(total)
