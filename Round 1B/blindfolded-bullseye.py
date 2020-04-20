# Codejam 2020, Round 1B: Blindfolded Bullseye

import sys
from random import randint


class Case:
    def __init__(self):
        self.queries_left = 300

    def query(self, X, Y):
        self.queries_left -= 1
        print("{} {}".format(X, Y), flush=True)
        response = input()
        if response == 'WRONG':
            sys.exit()
        return response

    def binary_search_left(self, right, func):
        left = -10**9
        while left < right:
            m = (left + right) // 2
            f = func(m)
            if f == 'HIT':
                right = m
            elif f == 'MISS':
                left = m + 1
            else:
                return None
        return left

    def binary_search_right(self, left, func):
        right = 10**9
        while left < right:
            m = (left + right) // 2
            f = func(m)
            if f == 'HIT':
                left = m + 1
            elif f == 'MISS':
                right = m
            else:
                return None
        return right - 1

    def solve(self):
        x, y = 0, 0
        r = self.query(x, y)
        while r == 'MISS':
            x, y = randint(-10**9, 10**9), randint(-10**9, 10**9)
            r = self.query(x, y)

        if r == 'CENTER':
            return

        x_low = self.binary_search_left(x, lambda x: self.query(x, y))
        if x_low is None:
            return

        x_high = self.binary_search_right(x, lambda x: self.query(x, y))
        if x_high is None:
            return

        y_low = self.binary_search_left(y, lambda y: self.query(x, y))
        if y_low is None:
            return

        y_high = self.binary_search_right(y, lambda y: self.query(x, y))
        if y_high is None:
            return

        r = self.query((x_low + x_high) // 2, (y_low + y_high) // 2)
        if r != 'CENTER':
            sys.exit()


# I/O Code
num_cases, A, B = map(int, input().split())

for _ in range(1, num_cases + 1):
    case = Case()
    case.solve()

sys.exit()
