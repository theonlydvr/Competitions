import lib

# P1
lines = lib.split_file('input.txt', delim='mul\(')
total = 0
for line in lines:
    for mul in line:
        parts = mul.split(')')
        if len(parts) > 1:
            nums = parts[0].split(',')
            if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
                total += int(nums[0]) * int(nums[1])

print(total)

# P2

total = 0
active = True
for line in lines:
    for mul in line:
        if active:
            parts = mul.split(')')
            if len(parts) > 1:
                nums = parts[0].split(',')
                if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
                    total += int(nums[0]) * int(nums[1])
        i = 0
        while i < len(mul):
            if mul[i:].startswith("do()"):
                active = True
                i += 4
            elif mul[i:].startswith("don't()"):
                active = False
                i += 7
            else:
                i += 1
print(total)
