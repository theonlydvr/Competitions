import lib

primes = []

for i in range(2, 10**6):
    if lib.is_prime(i):
        primes.append(i)

mx = max(primes)
pset = set(primes)
most_consec = 0
pconsec = 0

for i in range(len(primes)):
    cur_sum = primes[i]
    for j in range(i+1, len(primes)):
        cur_sum += primes[j]
        if cur_sum > mx:
            break
        elif j-i + 1 > most_consec and cur_sum in pset:
            most_consec = j-i + 1
            pconsec = cur_sum

print(pconsec)
