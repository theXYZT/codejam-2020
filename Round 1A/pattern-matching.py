# Codejam 2020, Round 1A: Pattern Matching


class Pattern:
    def __init__(self, fragments):
        self.prefix = fragments[0]
        self.suffix = fragments[-1]
        self.middle = "".join(fragments[1:-1])


def match_patterns(patterns):
    prefix = max((p.prefix for p in patterns), key=len)
    suffix = max((p.suffix for p in patterns), key=len)

    prefix_check = all(prefix.startswith(p.prefix) for p in patterns)
    suffix_check = all(suffix.endswith(p.suffix) for p in patterns)

    if prefix_check and suffix_check:
        middle = "".join(p.middle for p in patterns)
        return prefix + middle + suffix
    return '*'


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    patterns = [Pattern(input().split('*')) for _ in range(N)]

    result = match_patterns(patterns)
    print('Case #{}: {}'.format(case, result))
