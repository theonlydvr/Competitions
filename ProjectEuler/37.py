import lib

count = 0
all_sum = 0
i = 10

while count != 11:
    if lib.is_prime(i):
        si = str(i)
        valid = True
        for j in range(1, len(si)):
            if not lib.is_prime(int(si[j:])):
                valid = False
                break
            if not lib.is_prime(int(si[:-j])):
                valid = False
                break
        if valid:
            all_sum += i
            count += 1
    i += 1

print(all_sum)
