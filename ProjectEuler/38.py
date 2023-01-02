i = 1
largest = 0

while True:
    pan = ''
    valid = True
    j = 1
    for j in range(1, 10):
        pan += str(i * j)
        if len(pan) == 9:
            break
        elif len(pan) > 9:
            valid = False
            break
    if not valid and j <= 2:
        break
    else:
        span = set(pan)
        if '0' not in span and len(span) == len(pan) == 9:
            largest = max(largest, int(pan))
    i += 1

print(largest)
