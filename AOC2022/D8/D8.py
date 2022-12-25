#P1
trees = []
visible = []
viewing = []
row=0
with open('input.txt', 'r') as f:
    for line in f:
        trees.append([])
        visible.append([])
        viewing.append([])
        for c in line[:-1]:
            trees[row].append(int(c))
            visible[row].append(0)
            viewing[row].append(0)
        row += 1

for i in range(len(trees)):
    cur_max = -1
    for j in range(len(trees[i])):
        if trees[i][j] > cur_max:
            cur_max = trees[i][j]
            visible[i][j] = 1
    cur_max = -1
    for j in range(len(trees[i])-1, -1, -1):
        if trees[i][j] > cur_max:
            cur_max = trees[i][j]
            visible[i][j] = 1
for i in range(len(trees[0])):
    cur_max = -1
    for j in range(len(trees)):
        if trees[j][i] > cur_max:
            cur_max = trees[j][i]
            visible[j][i] = 1
    cur_max = -1
    for j in range(len(trees)-1, -1, -1):
        if trees[j][i] > cur_max:
            cur_max = trees[j][i]
            visible[j][i] = 1

print(sum(sum(visible,[])))

#P2
max_scenic = 0

for i in range(1, len(trees)-1):
    for j in range(1,len(trees[0])-1):
        if visible[i][j] == 1:
            scenic1 = 0
            for k in range(i-1, -1, -1):
                scenic1 += 1
                if trees[k][j] >= trees[i][j]:
                    break
            scenic2 = 0
            for k in range(i+1, len(trees)):
                scenic2 += 1
                if trees[k][j] >= trees[i][j]:
                    break
            scenic3 = 0
            for k in range(j-1, -1, -1):
                scenic3 += 1
                if trees[i][k] >= trees[i][j]:
                    break
            scenic4 = 0
            for k in range(j+1, len(trees[0])):
                scenic4 += 1
                if trees[i][k] >= trees[i][j]:
                    break
            max_scenic = max(scenic1*scenic2*scenic3*scenic4, max_scenic)

print(max_scenic)
                