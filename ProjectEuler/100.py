from decimal import *
n = Decimal(1)
sq2 = Decimal(2).sqrt()
y = (Decimal(1/4)*(-(3-2*sq2)**n-sq2*(3-2*sq2)**n-(3+2*sq2)**n+sq2*(3+2*sq2)**n+2)).to_integral_value()
while y < 10 ** 12:
    n += 1
    y = (Decimal(1/4)*(-(3-2*sq2)**n-sq2*(3-2*sq2)**n-(3+2*sq2)**n+sq2*(3+2*sq2)**n+2)).to_integral_value()
x = (Decimal(1/2) * ((2 * y ** 2 - 2 * y + 1).sqrt() + 1)).to_integral_value()
print(x)
