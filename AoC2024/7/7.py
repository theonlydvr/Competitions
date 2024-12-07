def evaluate(goal, numbers, initial):
    if len(numbers) == 0:
        return goal == initial
    else:
        return evaluate(goal, numbers[1:], initial + numbers[0]) or evaluate(goal, numbers[1:], initial * numbers[0])


def evaluate2(goal, numbers, initial):
    if len(numbers) == 0:
        return goal == initial
    else:
        return evaluate2(goal, numbers[1:], initial + numbers[0]) or evaluate2(goal, numbers[1:], initial * numbers[0]) or evaluate2(goal, numbers[1:], int(str(initial) + str(numbers[0])))


import lib

# P1
lines = lib.split_file('input.txt')
total = 0
for line in lines:
    goal = int(line[0][:-1])
    nums = [int(n) for n in line[1:]]
    if evaluate(goal, nums[1:], nums[0]):
        total += goal

print(total)

# P2
total = 0
for line in lines:
    goal = int(line[0][:-1])
    nums = [int(n) for n in line[1:]]
    if evaluate2(goal, nums[1:], nums[0]):
        total += goal

print(total)
