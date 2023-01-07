from decimal import Decimal

a = [Decimal(1), Decimal(1), Decimal(5)]
perimeter_sum = 16

while True:
    a.append(3*a[-1]+3*a[-2]-a[-3])
    if 3 * a[-1] - 2 > 10 ** 9:
        break
    s1 = (3 * a[-1] + 1) / 2
    s2 = (3 * a[-1] - 1) / 2
    if (s1 * (s1 - a[-1]) * (s1 - a[-1]) * (s1 - a[-1] - 1)).sqrt() % 1 == 0:
        perimeter_sum += 3 * a[-1] + 1
    if (s2 * (s2 - a[-1]) * (s2 - a[-1]) * (s2 - a[-1] + 1)).sqrt() % 1 == 0:
        perimeter_sum += 3 * a[-1] - 1

print(perimeter_sum)
