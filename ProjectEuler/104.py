import math

prev = 1
cur = 1

comp = set(i for i in range(1, 10))
k = 2

while math.log10(cur) < 9 or set(cur // 10 ** i % 10 for i in range(9)) != comp or set(cur // 10 ** i % 10 for i in range(int(math.log10(cur)), int(math.log10(cur))-9, -1)) != comp:
    temp = cur
    cur = prev + cur
    prev = temp
    k += 1

print(k)

