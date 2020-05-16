# Codejam 2020, Round 2: Incremental House of Pancakes


def binary_search(L, R, func):
    while L <= R:
        m = (L + R) // 2
        if func(m):
            L = m + 1
        else:
            R = m - 1
    return L - 1


def first_phase(A, B):
    """Assumes A > B."""
    D = A - B
    i = binary_search(0, D, lambda x: x * (x + 1) <= 2 * D)
    A -= i * (i + 1) // 2
    return i, A, B


def second_phase(A, B, i):
    """Assumes A goes first."""
    c1 = binary_search(0, A, lambda x: (i * x) + x*x <= A)
    c2 = binary_search(0, B, lambda x: ((i + 1) * x) + x*x <= B)
    A -= (i * c1) + c1*c1
    B -= ((i + 1) * c2) + c2*c2
    return c1, c2, A, B


def solve(L, R):
    if L > R:
        i1, L, R = first_phase(L, R)
    else:
        i1, R, L = first_phase(R, L)

    if L >= R:
        c1, c2, L, R = second_phase(L, R, i1)
    else:
        c1, c2, R, L = second_phase(R, L, i1)

    return i1 + c1 + c2, L, R


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    L, R = map(int, input().split())
    print('Case #{}: {} {} {}'.format(case, *solve(L, R)))
