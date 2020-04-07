# Codejam 2020, Qualification Round: Indicium

import numpy as np


def get_diagonal(N, K):
    if K % N == 0:
        return [K // N] * N
    else:
        min_a = max(1, -((2*N - K) // (N - 2)))
        max_a = min(N, (K - 2) // (N - 2))
        for a in range(min_a, max_a + 1):
            for b in range(1, N+1):
                for c in range(1, N+1):
                    if (N - 2)*a + b + c == K and (a == b) is (a == c):
                        return (N - 2) * [a] + [b, c]
    return None


def generate_latin_square(N, K):
    M = np.diag(get_diagonal(N, K))
    column_set = [set(c[c > 0]) for c in M.T]
    values = [M[0, 0]] + list(set([M[-1, -1], M[-2, -2]]))
    values += list(set(range(1, N + 1)) - set(values))

    for v in values:
        for r in range(N):
            if v not in M[r]:
                for c in [i % N for i in range(r, r + N)]:
                    if M[r, c] == 0 and v not in column_set[c]:
                        M[r, c] = v
                        column_set[c].add(v)
                        break
    return M


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, K = map(int, input().split())

    if K in [N + 1, N * N - 1] or (N, K) in [(3, 5), (3, 7)]:
        print('Case #{}: IMPOSSIBLE'.format(case))
    else:
        M = generate_latin_square(N, K)
        print('Case #{}: POSSIBLE'.format(case))
        for r in M:
            print(" ".join(map(str, r)))
