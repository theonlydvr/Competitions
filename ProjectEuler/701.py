import math
from decimal import Decimal

num = ''
dig = 1
b0 = Decimal('2.223561019313554106173177195')
b = b0
for i in range(15):
    num += str(math.floor(b))
    b = math.floor(b) * (b - math.floor(b) + 1)
print(num)
print(str(b0)[:26])
