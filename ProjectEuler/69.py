import lib

mx = 0
n = 0
for i in range(2, 1000000+1):
    tot = lib.totient(i)
    if i/tot > mx:
        mx = i/tot
        n = i
print(n)
