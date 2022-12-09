import math

#P1
pos = [(0,0)]
tr = 0
tc = 0
hr = 0
hc = 0

with open('input.txt', 'r') as f:
    for line in f:
        ins = line[:-1].split(' ')
        col_step = 0
        row_step = 0
        if ins[0] == 'R':
            col_step = 1
        elif ins[0] == 'L':
            col_step = -1
        elif ins[0] == 'U':
            row_step = 1
        else:
            row_step = -1
        for i in range(int(ins[1])):
            tempr = hr
            tempc = hc
            hr += row_step
            hc += col_step
            if math.pow(hr-tr,2)+math.pow(hc-tc,2) > 2:
                tr = tempr
                tc = tempc
                if (tr, tc) not in pos:
                    pos.append((tr,tc))

print(len(pos))

#P2
pos = [(0,0)]
rope = [(0,0)]*10
horiz = [(-1, 0),(1,0),(0,-1),(0,1)]
diag=[(1,1),(-1,-1),(1,-1),(-1,1)]

with open('input.txt', 'r') as f:
    for line in f:
        ins = line[:-1].split(' ')
        col_step = 0
        row_step = 0
        if ins[0] == 'R':
            col_step = 1
        elif ins[0] == 'L':
            col_step = -1
        elif ins[0] == 'U':
            row_step = 1
        else:
            row_step = -1
        for i in range(int(ins[1])):
            hp = rope[0]
            rope[0] = (rope[0][0]+row_step,rope[0][1]+col_step)
            s = 1
            while s < 10 and math.pow(rope[s-1][0]-rope[s][0],2)+math.pow(rope[s-1][1]-rope[s][1],2) > 2:
                if rope[s-1][0]==rope[s][0] or rope[s-1][1]==rope[s][1]:
                    dists = []
                    for step in horiz:
                        dists.append(math.pow(rope[s-1][0]-step[0]-rope[s][0],2)+math.pow(rope[s-1][1]-step[1]-rope[s][1],2))
                    step = dists.index(min(dists))
                    rope[s] = (rope[s][0]+horiz[step][0], rope[s][1]+horiz[step][1])
                else:
                    dists = []
                    for step in diag:
                        dists.append(math.pow(rope[s-1][0]-step[0]-rope[s][0],2)+math.pow(rope[s-1][1]-step[1]-rope[s][1],2))
                    step = dists.index(min(dists))
                    rope[s] = (rope[s][0]+diag[step][0], rope[s][1]+diag[step][1])
                s += 1
            print(rope)
            if rope[9] not in pos:
                pos.append(rope[9])

print(len(pos))