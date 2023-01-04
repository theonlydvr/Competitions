import math

fib = [0, 1]
all_sum = 0
prev = 0
sum_seq = []
for j in range(1000):
    num = str(j % 9) + ''.join(str(n) for n in [9] * math.floor(j / 9))
    all_sum += int(num)
    all_sum %= 1000000007
    # print(all_sum)
    sum_seq.append(all_sum)
    prev = all_sum
print(sum_seq)

for i in range(2, 30):
    fib.append(fib[i-1] + fib[i-2])
    num = '0'
    for j in range(fib[-1]+1):
        all_sum += int(num)
        all_sum %= 1000000007
        num = str(j % 9) + ''.join(str(n) for n in [9]*math.floor(j/9))
    print(all_sum)

print(all_sum)
