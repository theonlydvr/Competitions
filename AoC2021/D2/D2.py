import lib

# P1
data = lib.split_file('input.txt')
row = 0
col = 0
for d in data:
    if d[0] == 'forward':
        col += d[1]
    elif d[0] == 'down':
        row += d[1]
    elif d[0] == 'backward':
        col -= d[1]
    elif d[0] == 'up':
        row -= d[1]

print(row*col)

# P2
row = 0
col = 0
aim = 0
for d in data:
    if d[0] == 'forward':
        col += d[1]
        row += aim*d[1]
    elif d[0] == 'down':
        aim += d[1]
    elif d[0] == 'backward':
        col -= d[1]
    elif d[0] == 'up':
        aim -= d[1]

print(row*col)