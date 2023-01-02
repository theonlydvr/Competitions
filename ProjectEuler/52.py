i = 1
valid = False
while not valid:
    nums = set()
    for j in range(1, 7):
        l = list(str(i * j))
        l.sort()
        nums.add(''.join(l))
    if len(nums) == 1:
        print(i)
        valid = True
    i += 1
