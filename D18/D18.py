import numpy as np

def count_exposed(pos, grid):
    nexposed = 0
    for n in get_neighbors(pos, grid):
        if grid[n[0]][n[1]][n[2]] == 0:
            nexposed += 1
    return nexposed

def get_neighbors(pos, grid):
    neighbors = []
    possible = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    for p in possible:
        np = (pos[0]+p[0],pos[1]+p[1],pos[2]+p[2])
        if np[0] >= 0 and np[1] >= 0 and np[2] >= 0 and np[0] <= 23 and np[1] <= 23 and np[2] <= 23:
            neighbors.append(np)
    return neighbors

def traverse_open(pos, grid, tried):
    global visited
    tried.append(pos)
    neighbors = get_neighbors(pos, grid)
    for n in neighbors:
        if n in visited:
            return True
    for n in neighbors:
        if n not in tried and grid[n[0]][n[1]][n[2]] == 0:
            if traverse_open(n, grid, tried):
                return True
    return False

# P1
obsidian=np.zeros((24,24,24))
with open('input.txt', 'r') as f:
    for line in f:
        comps = line[:-1].split(',')
        comps = [int(x)+1 for x in comps]
        obsidian[comps[0]][comps[1]][comps[2]] = 1

sa = 0

visited = []

for i in range(24):
    for j in range(24):
        for k in range(24):
            if obsidian[i][j][k] == 1:
                sa += count_exposed((i,j,k), obsidian)

print(sa)

# P2
visited = set()
obsidian2 = obsidian.copy()
for i in range(24):
    for j in range(24):
        visited.add((0,i,j))
        visited.add((i,j,0))
        visited.add((i,0,j))
        visited.add((23,i,j))
        visited.add((i,j,23))
        visited.add((i,23,j))
for i in range(24):
    for j in range(24):
        for k in range(24):
            if obsidian[i][j][k]==0 and (i,j,k) not in visited:
                tried = []
                if traverse_open((i,j,k),obsidian2,tried):
                    visited.update(tried)
                else:
                    for n in tried:
                        obsidian2[n[0]][n[1]][n[2]] = 2
sa = 0
for i in range(24):
    for j in range(24):
        for k in range(24):
            if obsidian2[i][j][k] == 1:
                sa += count_exposed((i,j,k), obsidian2)
print(sa)