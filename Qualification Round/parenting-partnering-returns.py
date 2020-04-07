# Codejam 2020, Qualification Round: Parenting Partnering Returns

from collections import namedtuple

Activity = namedtuple("Activity", ["id", "start", "end"])

# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())

    activities = []
    for i in range(N):
        a, b = map(int, input().split())
        activities.append(Activity(i, a, b))
    activities.sort(key=lambda x: x.start)

    C, J = 0, 0
    assignments = ['*'] * N
    for a in activities:
        if C <= a.start:
            assignments[a.id] = 'C'
            C = a.end
        elif J <= a.start:
            assignments[a.id] = 'J'
            J = a.end
        else:
            break

    result = "".join(assignments)

    if '*' in result:
        print('Case #{}: IMPOSSIBLE'.format(case))
    else:
        print('Case #{}: {}'.format(case, result))
