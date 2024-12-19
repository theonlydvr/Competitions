import numpy as np

import lib

# P1
lines = lib.split_file('input.txt')
goal = (70, 70)
grid = np.zeros((goal[0] + 1, goal[1] + 1))
nb = 1024
for i in range(nb):
    pair = lines[i][0].split(',')
    grid[int(pair[1]), int(pair[0])] = 1

pos = {(0, 0)}
step = 0
found = False
visited = set()

while True:
    new_pos = set()
    for p in pos:
        visited.add(p)
        if p == goal:
            found = True
            break
        neighbors = lib.neighbors4(grid, p[0], p[1])
        for n in neighbors:
            if grid[n[0], n[1]] == 0 and n not in visited:
                new_pos.add(n)
    if found:
        break
    pos = new_pos
    step += 1

print(step)

# P2
path = set()
for i in range(nb, len(lines)):
    pair = lines[i][0].split(',')
    grid[int(pair[1]), int(pair[0])] = 1
    pos = {(0, 0)}
    step = 0
    found = False
    visited = set()

    while len(pos) > 0:
        new_pos = set()
        for p in pos:
            visited.add(p)
            if p == goal:
                found = True
                break
            neighbors = lib.neighbors4(grid, p[0], p[1])
            for n in neighbors:
                if grid[n[0], n[1]] == 0 and n not in visited:
                    new_pos.add(n)
        if found:
            break
        pos = new_pos
        step += 1

    if len(pos) == 0:
        break

print(lines[i][0])
