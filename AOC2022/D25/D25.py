import math

def convert(string):
    place = len(string)-1
    num = 0
    for c in string:
        if c == '1':
            num += 5 ** place
        elif c == '2':
            num += 2 * (5 ** place)
        elif c == '-':
            num -= 5 ** place
        elif c == '=':
            num -= 2 * (5 ** place)
        place -= 1
    return num

def calculate(string, place, target):
    if convert(string) == target:
        return string
    elif place >= 0:
        chars = ['1', '2', '0', '-', '=']
        for c in chars:
            if convert(string + c + '2'*(place-1)) >= target and convert(string + c + '='*(place-1)) <= target:
                res = calculate(string + c, place - 1, target)
                if res is not None:
                    return res
    else:
        return None

# P1
total = 0
with open('input.txt', 'r') as f:
    for line in f:
        total += convert(line[:-1])

print(calculate('', math.floor(math.log(total,5))+1,total))