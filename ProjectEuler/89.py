import lib

roman_order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_compare(c1, c2):
    if c1 == c2:
        return 0
    return 1 if roman_order.index(c1) > roman_order.index(c2) else -1


def roman_to_dec(roman):
    total = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman_compare(roman[i], roman[i + 1]) < 0:
            total += roman_map[roman[i + 1]] - roman_map[roman[i]]
            i += 2
        else:
            total += roman_map[roman[i]]
            i += 1
    return total


def dec_to_roman(dec):
    if dec == 0:
        return ''
    elif dec % 10 not in {0, 4, 5, 9}:
        return dec_to_roman(dec - (dec % 5)) + ''.join(['I'] * (dec % 5))
    elif dec % 10 == 9:
        return dec_to_roman(dec - 9) + 'IX'
    elif dec % 5 == 4:
        return dec_to_roman(dec - 4) + 'IV'
    elif dec % 10 == 5:
        return dec_to_roman(dec - 5) + 'V'
    elif dec % 100 not in {0, 40, 50, 90}:
        return dec_to_roman(dec - (dec % 50)) + ''.join(['X'] * int((dec % 50) / 10))
    elif dec % 100 == 90:
        return dec_to_roman(dec - 90) + 'XC'
    elif dec % 50 == 40:
        return dec_to_roman(dec - 40) + 'XL'
    elif dec % 100 == 50:
        return dec_to_roman(dec - 50) + 'L'
    elif dec % 1000 not in {0, 400, 500, 900}:
        return dec_to_roman(dec - (dec % 500)) + ''.join(['C'] * int((dec % 500) / 100))
    elif dec % 1000 == 900:
        return dec_to_roman(dec - 900) + 'CM'
    elif dec % 500 == 400:
        return dec_to_roman(dec - 400) + 'CD'
    elif dec % 1000 >= 500:
        return dec_to_roman(dec - 500) + 'D'
    elif dec % 1000 == 0:
        return ''.join(['M']*int(dec / 1000))


data = lib.split_file('p089_roman.txt')
saved = 0
for d in data:
    roman = dec_to_roman(roman_to_dec(d[0]))
    saved += len(d[0]) - len(roman)

print(saved)
