import itertools
import re
import numpy as np


def file_to_match(file, match=r'\w+'):
    data = []
    with open(file) as f:
        for line in f:
            data.append(re.findall(match, line[:-1]))
    return data


def file_to_ints(file, multi=True):
    data = []
    with open(file) as f:
        for line in f:
            if multi:
                data.append([int(s) for s in re.findall(r'\b\d+\b', line[:-1])])
            else:
                data.append(int(line[:-1]))
    return data


def split_file(file, delim="[\s]"):
    data = []
    with open(file) as f:
        for line in f:
            comps = re.split(delim, line[:-1])
            for i in range(len(comps)):
                if is_float(comps[i]):
                    if comps[i].isdigit():
                        comps[i] = int(comps[i])
                    else:
                        comps[i] = float(comps[i])
            data.append(comps)

    return data


def file_to_list2(file, cols=False, cast_ints=False):
    data = []
    with open(file) as f:
        for line in f:
            data.append([])
            for c in line[:-1]:
                if cast_ints and c.isdigit():
                    data[-1].append(int(c))
                else:
                    data[-1].append(c)
    if cols:
        return list(zip(*data))
    else:
        return data


def file_to_mat(file):
    return np.asarray(file_to_list2(file, cast_ints=True))


def is_float(element: any) -> bool:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_prime(num):
    for i in range(2, int(num ** (1/2)) + 1):
        if num % i == 0:
            return False
    return num > 1


def prime_factorize(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors
