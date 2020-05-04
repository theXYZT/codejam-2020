# Codejam 2020, Round 1C: Oversized Pancake Choppers

from collections import defaultdict
from functools import reduce
from math import gcd


def binary_search(L, R, func):
    while L <= R:
        m = (L + R) // 2
        if func(m):
            L = m + 1
        else:
            R = m - 1
    return L - 1


def solve(N, D, A):
    if N == 1 or D == 1:
        return D - 1

    limit = binary_search(1, A[-1], lambda s: sum(a // s for a in A) >= D)

    fully_usable_slices = defaultdict(int)
    num_target_slices = defaultdict(int)

    for c in range(1, D + 1):
        for a in A:
            g = gcd(a, c)
            size = (a // g, c // g)

            if size[0] > limit * size[1]:
                break
            if num_target_slices[size] + c <= D:
                fully_usable_slices[size] += 1
                num_target_slices[size] += c

    return D - max(fully_usable_slices.values())


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N, D = map(int, input().split())

    lcm = reduce(lambda x, y: abs(x * y) // gcd(x, y), range(2, D + 1))
    A = sorted(map(lambda x: lcm * int(x), input().split()))

    print('Case #{}: {}'.format(case, solve(N, D, A)))
