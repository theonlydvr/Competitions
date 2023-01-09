recs = {(1, 1)}
closest = 2 * 10 ** 6
c_grid = (0, 0)

i = 1
done = False
while True:
    k = 1
    for j in range(1, i + 1):
        recs.add((j, i + 1))
        recs.add((i + 1, j))
    for k in range(1, i + 2):
        rec_count = 0
        for c in range(1, i + 2):
            for r in range(1, k + 1):
                rec_count += (k - r + 1) * (i + 1 - c + 1)
        if k == 1 and rec_count > 2.1 * 10 ** 6:
            done = True
            break
        if abs(rec_count - 2 * 10 ** 6) < closest:
            closest = abs(rec_count - 2 * 10 ** 6)
            c_grid = (k, i + 1)
        elif rec_count > 2 * 10 ** 6:
            break
    i += 1
    if done:
        break

print(c_grid[0] * c_grid[1])
