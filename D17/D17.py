# P1

def find_bottom(grid, bottom, pos, newbot):
    if pos[1] == len(grid[0])-1:
        return newbot
    elif pos[0]+1<len(grid) and grid[pos[0]+1][pos[1]+1] == 1:
        return find_bottom(grid,bottom,(pos[0]+1,pos[1]+1),newbot)
    elif pos[0] - 1 == bottom or grid[pos[0]-1][pos[1]+1] == 1:
        return find_bottom(grid, bottom,(pos[0]-1,pos[1]+1),min(pos[0]-1+bottom,newbot))
    elif pos[0] == bottom or grid[pos[0]][pos[1]+1] == 1:
        return find_bottom(grid, bottom,(pos[0]-1,pos[1]+1),newbot)
    else:
        return bottom

with open('input.txt', 'r') as f:
    for line in f:
        sequence = line[:-1]

grid = [[1]*7]
bottom = 0
prehighest = 0
highest = 0
i = 0
b = 0

blocks = [[(0,0),(1,0),(2,0),(3,0)],
          [(0,1),(1,2),(1,1),(1,0),(2,1)],
          [(0,0),(1,0),(2,0),(2,1),(2,2)],
          [(0,0),(0,1),(0,2),(0,3)],
          [(0,0),(0,1),(1,0),(1,1)]]
history = []
while b < 4000:
    block = b % len(blocks)
    tempB = blocks[block].copy()
    maxh = highest - bottom
    for j, c in enumerate(tempB):
        tempB[j] = (c[0] + 2, c[1] + highest + 4 - bottom)
        maxh = max(maxh, tempB[j][1])
    while maxh >= len(grid):
        grid.append([0]*7)
    while True:
        ins = i % len(sequence)
        valid = True
        if sequence[ins] == '>':  
            step = 1
            for c in tempB:
                if c[0] + 1 == len(grid[0]) or grid[c[1]][c[0] + 1] == 1:
                    valid = False
                    break
        else:
            step = -1
            for c in tempB:
                if c[0] - 1 < 0 or grid[c[1]][c[0] - 1] == 1:
                    valid = False
                    break
        i += 1
        if valid:
            for j, c in enumerate(tempB):
                tempB[j] = (c[0] + step, c[1]) 
        valid = True
        for c in tempB:
            if grid[c[1] - 1][c[0]] == 1:
                valid = False
                break
        if valid:
            for j, c in enumerate(tempB):
                tempB[j] = (c[0], c[1] - 1)
        else:
            for j, c in enumerate(tempB):
                grid[c[1]][c[0]] = 1
                highest = max(highest, c[1] + bottom)
            break
    b += 1
    for r in range(len(grid)-1,-1,-1):
        if grid[r][0] == 1:
            newbot = find_bottom(grid, bottom, (r,0), r)
            if newbot > bottom:
                while newbot > bottom:
                    del grid[0]
                    bottom += 1
                break
    history.append(highest-prehighest)
    prehighest = highest

print(sum(history[:2022]))

# P2
import math
settle = 229*5-1    # Determined from visual inspection of history
cycle = 347*5       # Determined from visual inspection of history
base = sum(history[:settle])
cycleseg = history[settle:settle+cycle]
tb = 1000000000000
print(base+math.floor((tb-settle)/cycle)*sum(cycleseg)+sum(cycleseg[:(tb-settle)%cycle]))