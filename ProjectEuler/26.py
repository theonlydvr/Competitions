longest = 0
longest_n = 0

for i in range(1, 1001):
    num = 1
    rem = {1 % i}
    j = 1
    while num != 0:
        num = num * 10 % i
        if num not in rem:
            rem.add(num)
            j += 1
        else:
            if j > longest:
                longest = max(j, longest)
                longest_n = i
            break

print(longest_n)
