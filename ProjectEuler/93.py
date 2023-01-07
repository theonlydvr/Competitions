import itertools
from decimal import Decimal


def calculate(nums, calcs, cur):
    if len(nums) == 0:
        try:
            value = eval(cur)
            if value > 0 and (isinstance(value, int) or value.is_integer()):
                calcs.add(int(value))
        except ZeroDivisionError:
            pass
    else:
        for num in nums:
            nums2 = nums.copy()
            nums2.remove(num)
            if cur is None:
                calculate(nums2, calcs, str(num))
            else:
                calculate(nums2, calcs, '{} + {}'.format(num, cur))
                calculate(nums2, calcs, '({} + {})'.format(num, cur))
                calculate(nums2, calcs, '{} - {}'.format(num, cur))
                calculate(nums2, calcs, '{} - {}'.format(cur, num))
                calculate(nums2, calcs, '({} - {})'.format(num, cur))
                calculate(nums2, calcs, '({} - {})'.format(cur, num))
                calculate(nums2, calcs, '{} * {}'.format(num, cur))
                calculate(nums2, calcs, '{} / {}'.format(num, cur))
                calculate(nums2, calcs, '{} / {}'.format(cur, num))


combs = list(itertools.combinations(list(range(0, 10)), 4))
longest = 0
ints = ''
for comb in combs:
    temp = set()
    calculate(list(comb), temp, None)
    temp = list(temp)
    temp.sort()
    length = 0
    while length + 1 < len(temp) and temp[length + 1] == temp[length] + 1:
        length += 1
    if length > longest:
        ints = list(comb)
        ints.sort()
        ints = ''.join([str(i) for i in ints])
        longest = length

print(ints)
