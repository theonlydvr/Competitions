i = 1
seq = 1
sl = 3
while sl <= 1001:
    for j in range(4):
        i += sl - 1
        seq += i
    sl += 2

print(seq)
