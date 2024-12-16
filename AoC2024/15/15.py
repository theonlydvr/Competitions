import numpy as np

import lib

# P1
grid = lib.file_to_mat("grid.txt")
inst = lib.split_file("input.txt")

pos = np.where(grid == '@')

for line in inst:
    for i in line[0]:
        if i == '>':
            d = [0, 1]
        elif i == '<':
            d = [0, -1]
        elif i == 'v':
            d = [1, 0]
        else:
            d = [-1, 0]
        if grid[pos[0] + d[0], pos[1] + d[1]] == 'O':
            p_new = pos
            while grid[p_new[0] + d[0], p_new[1] + d[1]] == 'O':
                p_new = (p_new[0] + d[0], p_new[1] + d[1])
            while grid[p_new[0] + d[0], p_new[1] + d[1]] == '.' and grid[p_new[0], p_new[1]] == 'O':
                grid[p_new[0] + d[0], p_new[1] + d[1]] = 'O'
                grid[p_new[0], p_new[1]] = '.'
                p_new = (p_new[0] - d[0], p_new[1] - d[1])

        if grid[pos[0] + d[0], pos[1] + d[1]] == '.':
            grid[pos[0], pos[1]] = '.'
            pos = (pos[0] + d[0], pos[1] + d[1])
            grid[pos[0], pos[1]] = '@'

total = 0
boxes = np.where(grid == 'O')
for i in range(boxes[0].shape[0]):
    total += boxes[0][i] * 100 + boxes[1][i]
print(total)

# P2
grid = lib.file_to_mat("grid.txt")
grid1 = np.copy(grid)
grid1[grid1 == 'O'] = '['
grid2 = np.copy(grid)
grid2[grid2 == 'O'] = ']'
grid2[grid2 == '@'] = '.'
gridw = np.empty((grid1.shape[0], 2 * grid1.shape[1]), dtype=grid1.dtype)
gridw[:, 0::2] = grid1
gridw[:, 1::2] = grid2
pos = np.where(gridw == '@')

for line in inst:
    for i in line[0]:
        if i == '>':
            d = [0, 1]
            axis = 1
        elif i == '<':
            d = [0, -1]
            axis = 1
        elif i == 'v':
            d = [1, 0]
            axis = 0
        else:
            d = [-1, 0]
            axis = 0
        if axis == 1:
            p_new = pos
            while gridw[p_new[0] + d[0], p_new[1] + d[1]] == '[' or gridw[p_new[0] + d[0], p_new[1] + d[1]] == ']':
                p_new = (p_new[0] + d[0], p_new[1] + d[1])
            while gridw[p_new[0] + d[0], p_new[1] + d[1]] == '.' and (gridw[p_new[0], p_new[1]] == '[' or gridw[p_new[0], p_new[1]] == ']'):
                gridw[p_new[0] + d[0], p_new[1] + d[1]] = gridw[p_new[0], p_new[1]]
                gridw[p_new[0], p_new[1]] = '.'
                p_new = (p_new[0] - d[0], p_new[1] - d[1])
            if gridw[pos[0] + d[0], pos[1] + d[1]] == '.':
                gridw[pos[0], pos[1]] = '.'
                pos = (pos[0] + d[0], pos[1] + d[1])
                gridw[pos[0], pos[1]] = '@'
        else:
            p_new = pos
            chunk = [[pos]]
            found_box = True
            while found_box:
                found_box = False
                chunk.append([])
                for p in chunk[-2]:
                    if gridw[p[0] + d[0], p[1] + d[1]] == '[' or gridw[p[0] + d[0], p[1] + d[1]] == ']':
                        found_box = True
                        chunk[-1].append((p[0] + d[0], p[1] + d[1]))
                if len(chunk[-1]) > 0:
                    j = 0
                    while j < len(chunk[-1]):
                        if gridw[chunk[-1][j][0], chunk[-1][j][1]] == ']' and (j == 0 or chunk[-1][j-1][1] != chunk[-1][j][1] - 1):
                            chunk[-1].insert(j, (chunk[-1][j][0], chunk[-1][j][1] - 1))
                            j += 2
                        elif gridw[chunk[-1][j][0], chunk[-1][j][1]] == '[' and (j == len(chunk[-1]) - 1 or chunk[-1][j+1][1] != chunk[-1][j][1] + 1):
                            chunk[-1].insert(j+1, (chunk[-1][j][0], chunk[-1][j][1] + 1))
                            j += 2
                        else:
                            j += 1
            valid = all(all(gridw[p[0] + d[0], p[1] + d[1]] == '.' or gridw[p[0] + d[0], p[1] + d[1]] == '[' or gridw[p[0] + d[0], p[1] + d[1]] == ']' for p in r) for r in chunk)
            if valid:
                for r in reversed(chunk):
                    for p in r:
                        gridw[p[0] + d[0], p[1] + d[1]] = gridw[p[0], p[1]]
                        gridw[p[0], p[1]] = '.'
                pos = (pos[0] + d[0], pos[1] + d[1])

total = 0
boxes = np.where(gridw == '[')
for i in range(boxes[0].shape[0]):
    total += boxes[0][i] * 100 + boxes[1][i]
print(total)
