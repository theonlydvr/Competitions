import lib

ptotal = 3
diag_count = 5
sl = 5
num = 9

while ptotal / diag_count >= 0.1:
    for i in range(4):
        num += sl - 1
        if lib.is_prime(num):
            ptotal += 1
    diag_count += 4
    sl += 2

print(sl-2)
