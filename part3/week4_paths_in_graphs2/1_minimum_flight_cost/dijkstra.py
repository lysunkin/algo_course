#Uses python3

import sys
import queue

def distance(adj, cost, s, t):
    n = len(adj)
    d = [sys.maxsize]*n
    d[s] = 0
    visited = [False]*n
    q = queue.PriorityQueue()
    for v in range(n):
        q.put((d[v], v))

    while not q.empty():
        u = q.get()[1] # get shortest leg
        if visited[u]:
            continue

        visited[u] = True
        for i in range(len(adj[u])):
            v = adj[u][i]
            if d[v] > d[u] + cost[u][i]:
                d[v] = d[u] + cost[u][i]
                q.put((d[v], v))

    if d[t] != sys.maxsize:
        return d[t]
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
