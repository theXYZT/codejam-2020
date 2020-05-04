# Codejam 2020, Round 1C: Overexcited Fan


def solve(x, y, moves):
    t = 0
    if abs(x) + abs(y) == t:
        return t

    for m in moves:
        t += 1

        if m == 'N':
            y += 1
        elif m == 'S':
            y -= 1
        elif m == 'E':
            x += 1
        elif m == 'W':
            x -= 1

        if abs(x) + abs(y) <= t:
            return t

    return 'IMPOSSIBLE'


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    X, Y, M = input().split()

    time_to_intercept = solve(int(X), int(Y), M)
    print('Case #{}: {}'.format(case, time_to_intercept))
