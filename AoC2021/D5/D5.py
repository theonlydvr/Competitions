import lib

data = lib.file_to_ints('input.txt')
grid = []
for row in data:
    if row[0] == row[2]:
        while row[1] > len(grid)