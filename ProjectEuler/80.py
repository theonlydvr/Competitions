import math

total = 0
for i in range(1, 101):
    if not math.sqrt(i).is_integer():
        A = 5 * i
        B = 5
        for j in range(100):
            while A > B:
                A -= B
                B += 10
            A *= 100
            B = int(str(B)[:-1] + '0' + str(B)[-1])
        total += sum([int(i) for i in list(str(B)[:100])])

print(total)
