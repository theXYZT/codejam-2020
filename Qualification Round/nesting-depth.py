# Codejam 2020, Qualification Round: Nesting Depth


def nest(excess):
    if excess > 0:
        return excess * "("
    elif excess < 0:
        return -excess * ")"
    return ""


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    S = list(map(int, input()))

    depth = 0
    result = ""
    for d in S:
        result += nest(d - depth) + str(d)
        depth = d
    result += nest(-depth)

    print('Case #{}: {}'.format(case, result))
