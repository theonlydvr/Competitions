def coin_sum(coins, val, target):
    s = 0
    for i, coin in enumerate(coins):
        if val + coin == target:
            s += 1
        elif val + coin < target:
            s += coin_sum(coins[:i+1], val + coin, target)
    return s


print(coin_sum([1, 2, 5, 10, 20, 50, 100, 200], 0, 200))
