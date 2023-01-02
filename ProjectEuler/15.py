def traverse(row, col, dim):
    if row == dim and col == dim:
        return 1
    elif row != dim and col == dim:
        return 1
    elif row == dim and col != dim:
        return 1
    else:
        return traverse(row, col + 1, dim) + traverse(row + 1, col, dim)


print(traverse(0, 0, 15))
print(6*(4**17))