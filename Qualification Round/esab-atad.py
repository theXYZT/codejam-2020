# Codejam 2020, Qualification Round: ESAb ATAd

import sys


class Case:
    def __init__(self, nbits):
        self.nbits = nbits
        self.data = ['*'] * self.nbits
        self.complement_id = None
        self.reverse_id = None

    def query(self, i):
        print(str(i + 1), flush=True)
        response = input()
        if response == 'N':
            sys.exit()
        return response

    def query_pairs(self, i):
        # Reads i-th position from the beginning and from the end
        j = self.nbits - i - 1
        self.data[i] = self.query(i)
        self.data[j] = self.query(j)

        # Finds reference positions in data for configuration check
        if self.complement_id is None and self.data[i] == self.data[j]:
            self.complement_id = i
        if self.reverse_id is None and self.data[i] != self.data[j]:
            self.reverse_id = i

    def reverse(self):
        self.data = self.data[::-1]

    def complement(self):
        flip = {'0': '1', '1': '0'}
        self.data = [flip[c] if c in flip else c for c in self.data]

    def check_if_reversed(self):
        if self.reverse_id is None:
            _ = self.query(0)  # Waste a query
        else:
            if self.data[self.reverse_id] != self.query(self.reverse_id):
                self.reverse()

    def check_if_complemented(self):
        if self.complement_id is None:
            _ = self.query(0)  # Waste a query
        else:
            if self.data[self.complement_id] != self.query(self.complement_id):
                self.complement()

    def solve(self):
        read_position = 0

        # Read first 5 and last 5 positions
        for i in range(5):
            self.query_pairs(i)
            read_position += 1

        while '*' in self.data and read_position < self.nbits // 2:
            # Use two queries to check data configuration
            # Between every four paired queries
            if read_position % 4 == 1:
                self.check_if_complemented()
                self.check_if_reversed()

            self.query_pairs(read_position)
            read_position += 1

        print("".join(self.data), flush=True)
        if input() == 'N':
            sys.exit()


# I/O Code
num_cases, num_bits = map(int, input().split())

for _ in range(1, num_cases + 1):
    case = Case(num_bits)
    case.solve()

sys.exit()
