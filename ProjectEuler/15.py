def traverse(row, col, dim):
    if row == dim and col == dim:
        return 1
    elif row != dim and col == dim:
        return 1
    elif row == dim and col != dim:
        return 1
    else:
        if (dim - row, dim - col) in paths:
            return paths[(dim - row, dim - col)]
        else:
            dist = traverse(row, col + 1, dim) + traverse(row + 1, col, dim)
            paths[(dim - row, dim - col)] = dist
            paths[(dim - col, dim - row)] = dist
            return dist


paths = {}
for i in range(21):
    traverse(0, 0, i)
print(paths[(20, 20)])
