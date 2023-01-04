n = 1

coins = set()
minc = 4503599627370517

for n in range(1, 1000000000):
    coin = 1504170715041707 * n % 4503599627370517
    if coin < minc:
        coins.add(coin)
        minc = coin
        print(minc)

print(sum(coins))
