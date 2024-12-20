import lib


def make_towel(pattern):
    if pattern == "":
        return True
    else:
        valid = False
        for towel in towels:
            if pattern.startswith(towel):
                check = make_towel(pattern[len(towel):])
                if check:
                    valid = True
                    break
        return valid


def make_towel2(pattern):
    nvalid = 0
    if pattern == "":
        return 1
    elif pattern in combs:
        return combs[pattern]
    else:
        for towel in towels:
            if pattern.startswith(towel):
                nvalid += make_towel2(pattern[len(towel):])
        combs[pattern] = nvalid
        return nvalid


# P1
lines = lib.split_file('input.txt')
towels = [t.split(',')[0] for t in lines[0]]

total = 0
for line in lines[2:]:
    total += make_towel(line[0])

print(total)

# P2
combs = {}
towels = set(towels)
total = 0
for i, line in enumerate(lines[2:]):
    total += make_towel2(line[0])

print(total)
