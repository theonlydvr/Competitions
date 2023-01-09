MAX_SIZE = 10000001

isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * MAX_SIZE


def manipulated_sieve(N):
    isprime[0] = isprime[1] = False

    for i in range(2, N):
        if isprime[i]:
            prime.append(i)
            SPF[i] = i
        j = 0
        while (j < len(prime) and
               i * prime[j] < N and
               prime[j] <= SPF[i]):
            isprime[i * prime[j]] = False

            # put smallest prime factor of i*prime[j]
            SPF[i * prime[j]] = prime[j]

            j += 1


manipulated_sieve(MAX_SIZE - 1)
phis = [0] * MAX_SIZE
phis[1] = 1
min_rat = 100
n = 0
for i in range(2, MAX_SIZE - 1):
    phis[i] = phis[int(i / SPF[i])] * (SPF[i] if i % SPF[i] ** 2 == 0 else SPF[i] - 1)
    sphi = list(str(phis[i]))
    sphi.sort()
    si = list(str(i))
    si.sort()
    if ''.join(si) == ''.join(sphi):
        if i / phis[i] < min_rat:
            min_rat = i / phis[i]
            n = i
print(n)

