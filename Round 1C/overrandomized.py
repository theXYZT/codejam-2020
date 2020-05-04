# Codejam 2020, Round 1C: Overrandomized

from collections import Counter


def solve(responses):
    all_digits = set().union(*responses)
    first_digits = Counter([r[0] for r in responses])
    nonzero = ''.join(d for d, c in first_digits.most_common())
    return all_digits.difference(nonzero).pop() + nonzero


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    U = int(input())
    responses = [input().split()[-1] for _ in range(10**4)]
    print('Case #{}: {}'.format(case, solve(responses)))
