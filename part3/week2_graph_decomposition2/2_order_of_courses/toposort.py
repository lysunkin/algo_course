#Uses python3

import sys

def toposort(adj):
    order = []
    used = [False]*len(adj)
  
    def dfs_visit(adj, u):
        used[u] = True
        for v in adj[u]:
            if not used[v]:
                    dfs_visit(adj, v)
        order.append(u)

    for v in range(len(adj)):
        if not used[v]:
            dfs_visit(adj, v)

    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

