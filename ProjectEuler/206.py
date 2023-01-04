lowest = 1058921220
highest = 1389026624
n = lowest
for i in range(lowest, highest+1, 10):
    sq = n ** 2
    if str(sq)[::2] == '1234567890':
        print(n)
        break
    n += 10
