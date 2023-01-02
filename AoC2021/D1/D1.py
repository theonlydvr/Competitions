import lib

# p1
data = lib.file_to_ints('input.txt', multi=False)
n = data[0]
count = 0
for i in range(1, len(data)):
    if data[i] > n:
        count += 1
    n = data[i]
print(count)

# P2
n = [data[2], data[1], data[0]]
count = 0
for i in range(3, len(data)):
    nn = [data[i]]+n[0:2]
    if sum(nn) > sum(n):
        count += 1
    n = nn
print(count)
