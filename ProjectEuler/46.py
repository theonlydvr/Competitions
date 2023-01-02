import lib

i = 9
while True:
    if not lib.is_prime(i):
        sq = 1
        valid = False
        while True:
            if 2 * (sq ** 2) > i:
                break
            elif lib.is_prime(i - 2 * (sq ** 2)):
                valid = True
                break
            sq += 1
        if not valid:
            print(i)
            break
    i += 2
