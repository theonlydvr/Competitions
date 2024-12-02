import math

count = 0

for i in range(1, 10 ** 9, 2):
    if i % 10 % 2 != i // 10 ** int(math.log10(i)) % 2:
        si = str(i)[::-1]
        revsum = i + int(si)
        valid = True
        for n in range(len(si)):
            if revsum // 10 ** n % 10 % 2 == 0:
                valid = False
                break
        count += valid
    if i % 10 ** 6 == 1:
        print(i)

print(count * 2)
