import lib

# P1
lines = lib.split_file('input.txt')
total = 0
for i in range(0, len(lines), 4):
    x1 = int(lines[i][2][2:-1])
    y1 = int(lines[i][3][2:])
    x2 = int(lines[i+1][2][2:-1])
    y2 = int(lines[i+1][3][2:])
    px = int(lines[i+2][1][2:-1])
    py = int(lines[i+2][2][2:])
    A = (x2 * py - px * y2) / (x2 * y1 - x1 * y2)
    B = (x1 * py - px * y1) / (x1 * y2 - x2 * y1)
    if int(A) == A and int(B) == B:
        total += A * 3 + B

print(total)

# P2

total = 0
for i in range(0, len(lines), 4):
    x1 = int(lines[i][2][2:-1])
    y1 = int(lines[i][3][2:])
    x2 = int(lines[i+1][2][2:-1])
    y2 = int(lines[i+1][3][2:])
    px = int(lines[i+2][1][2:-1]) + 10000000000000
    py = int(lines[i+2][2][2:]) + 10000000000000
    A = (x2 * py - px * y2) / (x2 * y1 - x1 * y2)
    B = (x1 * py - px * y1) / (x1 * y2 - x2 * y1)
    if int(A) == A and int(B) == B:
        total += A * 3 + B

print(total)
