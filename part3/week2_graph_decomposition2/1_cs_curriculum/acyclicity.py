#Uses python3

import sys

def acyclic(adj):
    visited = [False for x in range(len(adj))]
    parents = [None for x in range(len(adj))]
    stacked = [False for x in range(len(adj))]
    cycle = []

    def dfs(adj, start, cycle):
        visited[start] = True
        stacked[start] = True
        for current in adj[start]:
            if not visited[current]:
                parents[current] = start
                dfs(adj, current, cycle)
            elif stacked[current]:
                x = start
                while x != current:
                    cycle.append(x)
                    x = parents[x]
                cycle = [current] + cycle
        stacked[start] = False

    for item in range(len(adj)):
        if not visited[item]:
            dfs(adj, item, cycle)

    if len(cycle) > 0:
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
