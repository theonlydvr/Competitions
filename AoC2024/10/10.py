import copy

import lib
import numpy as np


def visit(height, pos, visited, reached):
    if height == 9:
        reached.add(pos)
    neighbors = lib.neighbors4(grid, pos[0], pos[1])
    for neighbor in neighbors:
        if grid[neighbor[0], neighbor[1]] == height + 1 and neighbor not in visited:
            new_visited = copy.deepcopy(visited)
            new_visited.add(pos)
            visit(height + 1, neighbor, new_visited, reached)


def visit2(height, pos, visited):
    if height == 9:
        return 1
    neighbors = lib.neighbors4(grid, pos[0], pos[1])
    total = 0
    for neighbor in neighbors:
        if grid[neighbor[0], neighbor[1]] == height + 1 and neighbor not in visited:
            new_visited = copy.deepcopy(visited)
            new_visited.add(pos)
            total += visit2(height + 1, neighbor, new_visited)
    return total


# P1
grid = lib.file_to_mat("input.txt")
trailheads = np.where(grid == 0)
total_score = 0
for i in range(trailheads[0].shape[0]):
    reached = set()
    visit(0, (trailheads[0][i], trailheads[1][i]), set(), reached)
    total_score += len(reached)
print(total_score)

# P2
trailheads = np.where(grid == 0)
total_score = 0
for i in range(trailheads[0].shape[0]):
    total_score += visit2(0, (trailheads[0][i], trailheads[1][i]), set())
print(total_score)
