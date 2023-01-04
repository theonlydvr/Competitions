def split_sum(sq, num, ind, cur_sum, agg):
    if ind == len(sq):
        if agg == '':
            agg = '0'
        return cur_sum + int(agg) == num
    else:
        if cur_sum + int(agg+sq[ind:]) < num or cur_sum + int(agg + sq[ind]) + sum([int(c) for c in sq[ind+1:]]) > num:
            return False
        else:
            agg += sq[ind]
            val = split_sum(sq, num, ind+1, cur_sum + int(agg), '')
            if not val:
                val = split_sum(sq, num, ind + 1, cur_sum, agg)
            return val


i = 4
all_sum = 0
while i ** 2 <= 10 ** 12:
    sq = i ** 2
    if split_sum(str(sq), i, 0, 0, ''):
        all_sum += sq
    i += 1

print(all_sum)
