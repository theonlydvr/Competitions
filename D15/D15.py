# P1

trow = 2000000
intervals = []
btrow = []

with open('input.txt', 'r') as f:
    for line in f:
        parts = line[:-1].split(' ')
        sx = int(parts[2][2:-1])
        sy = int(parts[3][2:-1])
        bx = int(parts[8][2:-1])
        by = int(parts[9][2:])
        dist = abs(bx-sx) + abs(by-sy)
        dtrow = abs(trow-sy)
        if dtrow <= dist:
            intervals.append((sx-(dist-dtrow),sx+(dist-dtrow)))
        if by == trow and not bx in btrow:
            btrow.append(bx)

intervals.sort(key=lambda x: x[0])
nintervals = []
ind = 0
iend = 0
for i, x in enumerate(intervals):
    if x[0] <= intervals[iend][1]:
        if x[1] > intervals[iend][1]:
            iend = i
    else:
        nintervals.append((intervals[ind][0], intervals[iend][1]))
        ind = i
        iend = ind
nintervals.append((intervals[ind][0], intervals[iend][1]))
print(sum(i[1] - i[0] + 1 for i in nintervals) - len(btrow))

# P2

intervals = [[] for x in range(4000001)]

with open('input.txt', 'r') as f:
    for line in f:
        parts = line[:-1].split(' ')
        sx = int(parts[2][2:-1])
        sy = int(parts[3][2:-1])
        bx = int(parts[8][2:-1])
        by = int(parts[9][2:])
        dist = abs(bx-sx) + abs(by-sy)
        for i in range(max(0, sy - dist), min(sy + dist + 1, 4000001)):
            dy = abs(sy - i)
            if dy <= dist:
               intervals[i].append((max(sx - (dist - dy), 0), min(sx + (dist - dy), 4000001)))

done  = False
for j in range(len(intervals)):
    row = intervals[j]
    row.sort(key=lambda x: x[0])
    ind = 0
    iend = 0
    for i in range(len(row) - 1):
        if row[i+1][0] > row[iend][1]:
            print(row)
            print((row[i+1][0]-1)*4000000+j)
            done = True
            break
        if row[i+1][1] > row[iend][1]:
            iend = i+1
    if done:
        break