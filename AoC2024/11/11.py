import lib

# P1
lines = lib.split_file('input.txt')
stones = [int(n) for n in lines[0]]
steps = 25
for i in range(steps):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s_stone = str(stone)
            new_stones.append(int(s_stone[:len(s_stone) // 2]))
            new_stones.append(int(s_stone[len(s_stone) // 2:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))


stone_map = {}


def stone_travel(stone, step):
    if (stone, step) in stone_map:
        return stone_map[(stone, step)]
    if step == 75:
        created = 1
    elif stone == 0:
        created = stone_travel(1, step + 1)
    elif len(str(stone)) % 2 == 0:
        s_stone = str(stone)
        created = stone_travel(int(s_stone[:len(s_stone) // 2]), step + 1) + stone_travel(int(s_stone[len(s_stone) // 2:]), step + 1)
    else:
        created = stone_travel(stone * 2024, step + 1)
    stone_map[(stone, step)] = created
    return created


# P2
stones = [int(n) for n in lines[0]]
steps = 75
total = 0
for stone in stones:
    total += stone_travel(stone, 0)

print(total)
