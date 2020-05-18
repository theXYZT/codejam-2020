# Codejam 2020, Round 2: Security Update

from collections import namedtuple

Node = namedtuple("Node", ["i", "R", "T"])


def solve(num_nodes, num_edges, nodes, edges):
    R, T = [], []
    for i, x in enumerate(nodes, 1):
        if x < 0:
            R.append(Node(i, -x, None))
        else:
            T.append(Node(i, None, x))

    R.sort(key=lambda x: x.R)
    T.sort(key=lambda x: x.T)

    latency = [0] * num_nodes
    last = Node(0, 0, 0)
    N = 1
    while R or T:
        if R and R[0].R <= N:
            curr = R.pop(0)
            if curr.R == last.R:
                last = Node(curr.i, curr.R, last.T)
            else:
                last = Node(curr.i, curr.R, last.T + 1)
        else:
            curr = T.pop(0)
            if curr.T == last.T:
                last = Node(curr.i, last.R, curr.T)
            else:
                last = Node(curr.i, N, curr.T)

        latency[last.i] = last.T
        N += 1

    edge_latency = [1] * num_edges
    for i, (j, k) in enumerate(edges):
        dt = abs(latency[j] - latency[k])
        if dt > 0:
            edge_latency[i] = dt

    return edge_latency


# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    num_nodes, num_edges = map(int, input().split())
    nodes = list(map(int, input().split()))
    edges = [tuple(map(lambda x: int(x) - 1, input().split()))
             for _ in range(num_edges)]

    edge_latency = solve(num_nodes, num_edges, nodes, edges)
    print('Case #{}: {}'.format(case, " ".join(map(str, edge_latency))))
