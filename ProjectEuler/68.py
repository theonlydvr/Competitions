import copy


def make_Ngons(grid, ind, nums, target):
    if len(nums) == 1:
        grid[ind // 3][ind % 3] = nums[0]
        if sum(grid[ind // 3]) == target and not any(l[0] < grid[0][0] for l in grid):
            return int(''.join(str(n) for l in grid for n in l))
        else:
            return 0
    else:
        total = sum(grid[ind // 3])
        mx = 0
        for n in nums:
            if (ind % 3 < 2 and total + n < target) or (ind % 3 == 2 and total + n == target):
                new_grid = copy.deepcopy(grid)
                new_grid[ind // 3][ind % 3] = n
                if ind % 3 == 1:
                    new_grid[ind // 3 - 1][2] = n
                elif ind % 3 == 2:
                    new_grid[ind // 3 + 1][1] = n
                new_ind = ind + 1
                while new_grid[new_ind // 3][new_ind % 3] != 0:
                    new_ind += 1
                new_nums = nums.copy()
                new_nums.remove(n)
                mx = max(make_Ngons(new_grid, new_ind, new_nums, target), mx)
        return mx


mx = 0
N = 5
for i in range(2*N + 1 + 2, 3 * 2 * N - 2):
    for n in range(1, N + 2):
        nums = list(range(1, 2 * N))
        nums.remove(n)
        for k in range(1, N):
            grid = [[0 for i in range(3)] for j in range(N)]
            grid[k][0] = 2 * N
            grid[0][0] = n
            mx = max(mx, make_Ngons(grid, 1, nums, i))

print(mx)
