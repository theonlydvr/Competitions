class Elf:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.order = ['N', 'S', 'W', 'E']

# P1
grove = []
elves = []
l_most = -20
b_most = -20
i = -1
with open('input.txt', 'r') as f:
    for line in f:
        i += 1
        grove.append([None]*20)
        for j, c in enumerate(line[:-1]):
            if c == '.':
                grove[i].append(None)
            else:
                elf = Elf(i, j)
                elves.append(elf)
                grove[i].append(elf)
        grove[i] += [None]*20
for _ in range(20):
    grove.insert(0, [None]*len(grove[0]))
    grove.append([None]*len(grove[0]))

for r in range(10):
    proposals = {}
    for elf in elves:
        r = elf.row-l_most
        c = elf.col-b_most
        nrow = None
        ncol = None
        all_empty = True
        for d in elf.order:
            if d == 'N' :
                if grove[r-1][c] is None and grove[r-1][c-1] is None and grove[r-1][c+1] is None:
                    if nrow is None:
                        nrow = r-1
                        ncol = c
                else:
                    all_empty = False    
            elif d == 'S':
                if grove[r+1][c] is None and grove[r+1][c-1] is None and grove[r+1][c+1] is None:
                    if nrow is None:
                        nrow = r+1
                        ncol = c
                else:
                    all_empty = False   
            elif d == 'W':
                if grove[r][c-1] is None and grove[r+1][c-1] is None and grove[r-1][c-1] is None:
                    if nrow is None:
                        nrow = r
                        ncol = c-1
                else:
                    all_empty = False   
            elif d == 'E':
                if grove[r][c+1] is None and grove[r+1][c+1] is None and grove[r-1][c+1] is None:
                    if nrow is None:
                        nrow = r
                        ncol = c+1
                else:
                    all_empty = False   
        if nrow is not None and not all_empty: 
            if (nrow, ncol) not in proposals:
                proposals[(nrow, ncol)] = elf
            else:
                proposals[(nrow, ncol)] = None
    for prop in proposals.keys():
        if proposals[prop] is not None:
            elf = proposals[prop]
            grove[elf.row-l_most][elf.col-b_most]=None
            elf.row = prop[0]+l_most
            elf.col = prop[1]+b_most
            grove[prop[0]][prop[1]] = elf
    for elf in elves:
        tdir = elf.order[0]
        elf.order.remove(tdir)
        elf.order.append(tdir)

rows = (1000, -1000)
cols = (1000, -1000)
for elf in elves:
    rows = (min(rows[0],elf.row), max(rows[1],elf.row))
    cols = (min(cols[0],elf.col), max(cols[1],elf.col))
    
print((rows[1]-rows[0]+1)*(cols[1]-cols[0]+1)-len(elves))

# P2
grove = []
elves = []
l_most = -1000
b_most = -1000
i = -1
with open('input.txt', 'r') as f:
    for line in f:
        i += 1
        grove.append([None]*1000)
        for j, c in enumerate(line[:-1]):
            if c == '.':
                grove[i].append(None)
            else:
                elf = Elf(i, j)
                elves.append(elf)
                grove[i].append(elf)
        grove[i] += [None]*1000
for _ in range(1000):
    grove.insert(0, [None]*len(grove[0]))
    grove.append([None]*len(grove[0]))

moved = True
rounds = 0
while moved:
    rounds += 1
    moved = False
    proposals = {}
    for elf in elves:
        r = elf.row-l_most
        c = elf.col-b_most
        nrow = None
        ncol = None
        all_empty = True
        for d in elf.order:
            if d == 'N' :
                if grove[r-1][c] is None and grove[r-1][c-1] is None and grove[r-1][c+1] is None:
                    if nrow is None:
                        nrow = r-1
                        ncol = c
                else:
                    all_empty = False    
            elif d == 'S':
                if grove[r+1][c] is None and grove[r+1][c-1] is None and grove[r+1][c+1] is None:
                    if nrow is None:
                        nrow = r+1
                        ncol = c
                else:
                    all_empty = False   
            elif d == 'W':
                if grove[r][c-1] is None and grove[r+1][c-1] is None and grove[r-1][c-1] is None:
                    if nrow is None:
                        nrow = r
                        ncol = c-1
                else:
                    all_empty = False   
            elif d == 'E':
                if grove[r][c+1] is None and grove[r+1][c+1] is None and grove[r-1][c+1] is None:
                    if nrow is None:
                        nrow = r
                        ncol = c+1
                else:
                    all_empty = False   
        if nrow is not None and not all_empty: 
            if (nrow, ncol) not in proposals:
                proposals[(nrow, ncol)] = elf
            else:
                proposals[(nrow, ncol)] = None
    for prop in proposals.keys():
        if proposals[prop] is not None:
            moved = True
            elf = proposals[prop]
            grove[elf.row-l_most][elf.col-b_most]=None
            elf.row = prop[0]+l_most
            elf.col = prop[1]+b_most
            grove[prop[0]][prop[1]] = elf
    for elf in elves:
        tdir = elf.order[0]
        elf.order.remove(tdir)
        elf.order.append(tdir)

rows = (3000, -3000)
cols = (3000, -3000)
for elf in elves:
    rows = (min(rows[0],elf.row), max(rows[1],elf.row))
    cols = (min(cols[0],elf.col), max(cols[1],elf.col))
    
print(rounds)
                
                
        
        