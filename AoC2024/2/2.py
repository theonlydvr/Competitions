import lib

def is_safe(line):
    prev_val = None
    prev_step = None
    for c in line:
        if prev_val is None:
            prev_val = int(c)
        elif prev_step is None:
            prev_step = int(c) - prev_val
            if abs(prev_step) <= 3:
                prev_val = int(c)
            else:
                return False
        elif (((int(c) - prev_val) > 0 and prev_step > 0) or ((int(c) - prev_val) < 0 and prev_step < 0)) and abs(int(c) - prev_val) <= 3:
            prev_step = int(c) - prev_val
            prev_val = int(c)
        else:
            return False
    return True


# P1
lines = lib.split_file('input.txt')
n_safe = 0
for line in lines:
    n_safe += is_safe(line)

print(n_safe)

# P2

n_safe = 0
for line in lines:
    safe = False
    for i in range(len(line)):
        if is_safe(line[:i] + line[i+1:]):
            safe = True
            break
    n_safe += safe

print(n_safe)
