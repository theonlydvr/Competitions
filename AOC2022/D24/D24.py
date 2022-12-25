class Blizzard:
    def __init__(self, d, row, col):
        self.d = d
        self.col = col
        self.row = row
            
def update_blizzards(grid, blizzards):
    for k in blizzards.keys():
        b = blizzards[k]
        grid[b.row][b.col]-=1
        if grid[b.row][b.col] == 0:
            grid[b.row][b.col] = None
        if b.d == '>':
            b.col += 1
            if b.col == len(grid[0])-1:
                b.col = 1
        elif b.d == '<':
            b.col -= 1
            if b.col == 0:
                b.col = len(grid[0])-2
        elif b.d == 'v':
            b.row += 1
            if b.row == len(grid)-2:
                b.row = 2
        elif b.d == '^':
            b.row -= 1
            if b.row == 1:
                b.row = len(grid)-3
        if grid[b.row][b.col] is None:
            grid[b.row][b.col] = 1
        else:
            grid[b.row][b.col] += 1

# P1
grid = []
blizzards = {}
bid = 0
r = -1
with open('input.txt', 'r') as f:
    for line in f:
        r += 1
        grid.append([])
        for i, c in enumerate(line[:-1]):
            if c == '#':
                grid[r].append(0)
            elif c == '.':
                grid[r].append(None)
            else:
                b = Blizzard(c, r+1, i)
                grid[r].append(1)
                blizzards[bid] = b
                bid += 1
    
grid.insert(0, [0]*len(grid[0]))
grid.append([0]*len(grid[0]))

pos = (1,1)
goal = (len(grid)-2,len(grid[0])-2)

positions = [[pos]]
while not any(p == goal for p in positions[-1]):
    plist = set()
    for p in positions[-1]:
        if grid[p[0]][p[1]] is None:
            plist.add((p[0]+1,p[1]))
            plist.add((p[0],p[1]+1))
            plist.add(p)
            plist.add((p[0],p[1]-1))
            plist.add((p[0]-1,p[1]))
    update_blizzards(grid, blizzards)
    positions.append(plist)

print(len(positions)-1)

# P2
positions2 = [[goal]]
while not any(p == pos for p in positions2[-1]):
    plist = set()
    for p in positions2[-1]:
        if grid[p[0]][p[1]] is None:
            plist.add((p[0]+1,p[1]))
            plist.add((p[0],p[1]+1))
            plist.add(p)
            plist.add((p[0],p[1]-1))
            plist.add((p[0]-1,p[1]))
    update_blizzards(grid, blizzards)
    positions2.append(plist)

positions3 = [[pos]]
while not any(p == goal for p in positions3[-1]):
    plist = set()
    for p in positions3[-1]:
        if grid[p[0]][p[1]] is None:
            plist.add((p[0]+1,p[1]))
            plist.add((p[0],p[1]+1))
            plist.add(p)
            plist.add((p[0],p[1]-1))
            plist.add((p[0]-1,p[1]))
    update_blizzards(grid, blizzards)
    positions3.append(plist)

print(len(positions)+len(positions2)+len(positions3)-3)