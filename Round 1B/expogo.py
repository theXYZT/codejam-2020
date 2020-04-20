# Codejam 2020, Round 1B: Expogo

from functools import lru_cache


@lru_cache(maxsize=None)
def solve(X, Y):
    if X == Y == 0:
        return True, ''

    if X % 2 == Y % 2:
        return False, None

    if X % 2 == 1:
        # Jump West
        if (X, Y) != (1, 0):
            possible, jumps = solve((X + 1) // 2, Y // 2)
            if possible:
                return True, 'W' + jumps

        # Jump East
        if (X, Y) != (-1, 0):
            possible, jumps = solve((X - 1) // 2, Y // 2)
            if possible:
                return True, 'E' + jumps

    else:
        # Jump South
        if (X, Y) != (0, 1):
            possible, jumps = solve(X // 2, (Y + 1) // 2)
            if possible:
                return True, 'S' + jumps

        # Jump North
        if (X, Y) != (0, -1):
            possible, jumps = solve(X // 2, (Y - 1) // 2)
            if possible:
                return True, 'N' + jumps

    return False, None


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    X, Y = map(int, input().split())

    possible, jumps = solve(X, Y)
    if possible:
        print('Case #{}: {}'.format(case, jumps))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case))
