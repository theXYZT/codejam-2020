# Codejam 2020, Round 2: Wormhole in One

from math import gcd
from itertools import permutations
from collections import defaultdict, namedtuple

Position = namedtuple("Position", ["x", "y"])


def solve(N, holes):
    if N <= 4:
        return N

    directions = set()
    for a, b in permutations(holes, 2):
        dx, dy = a.x - b.x, a.y - b.y
        g = gcd(abs(dx), abs(dy))
        dx, dy = dx // g, dy // g

        # Force directions to point in the 1st and 4th quadrants
        if (dx, dy) < (-dx, -dy):
            dx, dy = -dx, -dy

        directions.add((dx, dy))

    result = 4
    for dx, dy in directions:
        holes_per_line = defaultdict(int)
        for hole in holes:
            holes_per_line[hole.x * dy - hole.y * dx] += 1

        single, odd, even = 0, 0, 0
        for num_holes in holes_per_line.values():
            if num_holes == 1:
                single += 1
            elif num_holes % 2:
                odd += num_holes
            else:
                even += num_holes

        single = min(1, single) if odd % 2 else min(2, single)
        result = max(result, odd + even + single)

    return result


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    holes = [Position(*map(int, input().split())) for _ in range(N)]

    print('Case #{}: {}'.format(case, solve(N, holes)))
