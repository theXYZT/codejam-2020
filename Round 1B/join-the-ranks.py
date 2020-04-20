# Codejam 2020, Round 1B: Join the Ranks


def solve(R, S):
    deck = list(range(1, R+1)) * S
    num_shuffles = (R * S - R + 1) // 2

    shuffles = []
    for _ in range((R * S - R) // 2):
        a, first = 0, deck[0]
        while deck[a] == first:
            a += 1

        second = deck[a]
        while deck[a] == second:
            a += 1

        b = a + 1
        while deck[b] != second:
            b += 1

        shuffles.append((a, b - a))
        deck = deck[a:b] + deck[:a] + deck[b:]

    if (R * S - R) % 2:
        a, first = 0, deck[0]
        while deck[a] == first:
            a += 1

        shuffles.append((a, R * S - a))
        deck = deck[a:] + deck[:a]

    return num_shuffles, shuffles


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    R, S = map(int, input().split())

    num_shuffles, shuffles = solve(R, S)
    print('Case #{}: {}'.format(case, num_shuffles))
    for a, b in shuffles:
        print('{} {}'.format(a, b))
