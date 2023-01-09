def attempt_cycle(seq, needed):
    if len(seq) == 6 and seq[-1][2:] == seq[0][:2]:
        return sum([int(i) for i in seq])
    else:
        cycle = None
        for shape in needed:
            for num in shapes[shape]:
                if num.startswith(seq[-1][2:]):
                    new_seq = seq.copy()
                    new_seq.append(num)
                    new_needed = needed.copy()
                    new_needed.remove(shape)
                    cycle = attempt_cycle(new_seq, new_needed)
                    if cycle is not None:
                        return cycle
        if cycle is None:
            return None


shapes = [set(), set(), set(), set(), set(), set()]

n = 1
while n * (n + 1) / 2 < 10000:
    if n * (n + 1) / 2 > 999:
        shapes[0].add(str(int(n * (n + 1) / 2)))
    if 999 < n ** 2 < 10000:
        shapes[1].add(str(int(n ** 2)))
    if 999 < n * (3 * n - 1) / 2 < 10000:
        shapes[2].add(str(int(n * (3 * n - 1) / 2)))
    if 999 < n * (2 * n - 1) < 10000:
        shapes[3].add(str(int(n * (2 * n - 1))))
    if 999 < n * (5 * n - 3) / 2 < 10000:
        shapes[4].add(str(int(n * (5 * n - 3) / 2)))
    if 999 < n * (3 * n - 2) < 10000:
        shapes[5].add(str(int(n * (3 * n - 2))))
    n += 1

shapes[0].difference(shapes[1]).difference(shapes[2]).difference(shapes[3]).difference(shapes[4]).difference(shapes[5])
shapes[1].difference(shapes[0]).difference(shapes[2]).difference(shapes[3]).difference(shapes[4]).difference(shapes[5])
shapes[2].difference(shapes[1]).difference(shapes[0]).difference(shapes[3]).difference(shapes[4]).difference(shapes[5])
shapes[3].difference(shapes[1]).difference(shapes[2]).difference(shapes[0]).difference(shapes[4]).difference(shapes[5])
shapes[4].difference(shapes[1]).difference(shapes[2]).difference(shapes[3]).difference(shapes[0]).difference(shapes[5])
shapes[5].difference(shapes[1]).difference(shapes[2]).difference(shapes[3]).difference(shapes[4]).difference(shapes[0])

for n in shapes[0]:
    cycle = attempt_cycle([n], [1, 2, 3, 4, 5])
    if cycle is not None:
        print(cycle)
        break
