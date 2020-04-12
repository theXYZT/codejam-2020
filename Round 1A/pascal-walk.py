# Codejam 2020, Round 1A: Pascal Walk


def pascal_walk(N):
    rows = [b == '1' for b in format(N - N.bit_length(), "b")][::-1]
    walk = []
    walk_sum = 0

    for i, b in enumerate(rows, 1):
        row_walk = [(i, k) for k in range(1, i + 1)]
        if walk and walk[-1][0] == walk[-1][-1]:
            row_walk = row_walk[::-1]
        if b:
            walk += row_walk
            walk_sum += 2**(i - 1)
        else:
            walk += row_walk[:1]
            walk_sum += 1

    excess_rows = range(walk[-1][0] + 1,
                        walk[-1][0] + 1 + N - walk_sum)

    if walk[-1][-1] == 1:
        walk += [(i, 1) for i in excess_rows]
    else:
        walk += [(i, i) for i in excess_rows]

    return walk


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    result = pascal_walk(N)
    print('Case #{}:'.format(case))
    for r, k in result:
        print('{} {}'.format(r, k))
