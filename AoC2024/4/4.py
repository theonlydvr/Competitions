import lib

# P1
grid = lib.file_to_mat("input.txt")
total = 0
word = "XMAS"

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        inds_check = []
        if i >= 3:
            inds_check.append([(i, j), (i-1, j), (i-2, j), (i-3, j)])
            if j >= 3:
                inds_check.append([(i, j), (i - 1, j-1), (i - 2, j-2), (i - 3, j-3)])
            if j <= grid.shape[1] - 4:
                inds_check.append([(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)])
        if i <= grid.shape[0] - 4:
            inds_check.append([(i, j), (i + 1, j), (i + 2, j), (i + 3, j)])
            if j >= 3:
                inds_check.append([(i, j), (i + 1, j-1), (i + 2, j-2), (i + 3, j-3)])
            if j <= grid.shape[1] - 4:
                inds_check.append([(i, j), (i + 1, j+1), (i + 2, j+2), (i + 3, j+3)])
        if j >= 3:
            inds_check.append([(i, j), (i, j-1), (i, j-2), (i, j-3)])
        if j <= grid.shape[1] - 4:
            inds_check.append([(i, j), (i, j+1), (i, j+2), (i, j+3)])

        for seq in inds_check:
            valid = True
            for k in range(len(word)):
                if grid[seq[k][0], seq[k][1]] != word[k]:
                    valid = False
                    break
            total += valid

print(total)

# P2
word = "MAS"
total = 0
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        inds_check = []
        if 1 <= i < grid.shape[0] - 1 and 1 <= j < grid.shape[0] - 1:
            inds_check.append([(i-1, j-1), (i, j), (i+1, j+1)])
            inds_check.append([(i - 1, j+1), (i, j), (i + 1, j-1)])
            inds_check.append([(i + 1, j - 1), (i, j), (i - 1, j + 1)])
            inds_check.append([(i + 1, j + 1), (i, j), (i - 1, j - 1)])
        x = 0
        for seq in inds_check:
            valid = True
            for k in range(len(word)):
                if grid[seq[k][0], seq[k][1]] != word[k]:
                    valid = False
                    break
            x += valid
        total += x >= 2

print(total)
