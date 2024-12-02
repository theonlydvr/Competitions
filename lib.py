import itertools
import math
import re
from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


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


def split_file(file, delim="[\s]", cast=False):
    data = []
    with open(file) as f:
        for line in f:
            comps = re.split(delim, line[:-1])
            if cast:
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


def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor


def totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = int(n / p)
            result -= int(result / p)
        p += 1
    if n > 1:
        result -= int(result / n)
    return result


def neighbors8(matrix, rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append((newRow, newCol))
    return result


def neighbors4(matrix, rowNumber, colNumber, check_dims=True):
    result = []
    if not check_dims or rowNumber >= 1:
        result.append((rowNumber - 1, colNumber))
    if not check_dims or rowNumber < matrix.shape[0] - 1:
        result.append((rowNumber + 1, colNumber))
    if not check_dims or colNumber >= 1:
        result.append((rowNumber, colNumber - 1))
    if not check_dims or colNumber < matrix.shape[1] - 1:
        result.append((rowNumber, colNumber + 1))
    return result


def neighbors4_wrapped(matrix, rowNumber, colNumber):
    result = [((rowNumber - 1) % matrix.shape[0], colNumber % matrix.shape[1]),
              ((rowNumber + 1) % matrix.shape[0], colNumber % matrix.shape[1]),
              (rowNumber % matrix.shape[0], (colNumber - 1) % matrix.shape[1]),
              (rowNumber % matrix.shape[0], (colNumber + 1) % matrix.shape[1])]
    return result
