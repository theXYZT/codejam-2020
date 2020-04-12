# Codejam 2020, Round 1A: Square Dance

import itertools


class Dancer:
    north = south = east = west = None

    def __init__(self, skill):
        self.skill = skill
        self._eliminated = False

    @property
    def neighbors(self):
        all_compass = [self.north, self.south, self.east, self.west]
        return set(n for n in all_compass if n is not None)

    @property
    def eliminated(self):
        n = self.neighbors
        if n:
            self._eliminated = len(n) * self.skill < sum(i.skill for i in n)
        return self._eliminated

    def reassign_neighbors(self):
        if self.west is not None:
            self.west.east = self.east
        if self.east is not None:
            self.east.west = self.west
        if self.north is not None:
            self.north.south = self.south
        if self.south is not None:
            self.south.north = self.north


def resolve_round(dancers):
    eliminated = set(d for d in dancers if d.eliminated)
    for d in eliminated:
        d.reassign_neighbors()

    candidates = set().union(*[d.neighbors for d in eliminated])
    candidates = set(d for d in candidates if d not in eliminated)
    return eliminated, candidates


def get_interest_level(dancers):
    interest = sum(d.skill for d in dancers)
    result = interest
    eliminated, candidates = resolve_round(dancers)

    while eliminated:
        interest -= sum(d.skill for d in eliminated)
        result += interest
        eliminated, candidates = resolve_round(candidates)

    return result


def preprocess(R, C):
    stage = [[Dancer(int(s)) for j, s in enumerate(input().split())]
             for i in range(R)]

    for i in range(R):
        for j in range(C):
            if i > 0:
                stage[i][j].north = stage[i - 1][j]
            if i < R - 1:
                stage[i][j].south = stage[i + 1][j]
            if j > 0:
                stage[i][j].west = stage[i][j - 1]
            if j < C - 1:
                stage[i][j].east = stage[i][j + 1]

    return set(itertools.chain.from_iterable(stage))


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    dancers = preprocess(R, C)

    result = get_interest_level(dancers)
    print('Case #{}: {}'.format(case, result))
