# Codejam 2020, Qualification Round: Vestigium

import numpy as np

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    M = np.array([list(map(int, input().split())) for _ in range(N)])

    K = np.trace(M)
    R = sum(len(set(r)) < N for r in M)
    C = sum(len(set(c)) < N for c in M.T)
    print('Case #{}: {} {} {}'.format(case, K, R, C))
