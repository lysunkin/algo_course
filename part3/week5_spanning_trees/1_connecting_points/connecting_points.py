#Uses python3
import sys
import math
import queue

def minimum_distance(x, y):
    result = 0.0
    n = len(x)
    adj = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            distance = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            adj[i][j] = distance
            adj[j][i] = distance

    c = [sys.maxsize]*n
    visited = [False]*n
    parent = [None]*n

    h = queue.PriorityQueue()

    for v in range(n):
        h.put((c[v], v))
    
    while not h.empty():
        _, u = h.get()

        if visited[u]:
            continue

        visited[u] = True
    
        for v in range(n):
            if v == u:
                continue

            if not visited[v] and c[v] > adj[u][v]:
                c[v] = adj[u][v]
                parent[v] = u
                h.put((c[v], v))

    for i in range(n):
        if parent[i] != None: 
            result += adj[i][parent[i]]

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
