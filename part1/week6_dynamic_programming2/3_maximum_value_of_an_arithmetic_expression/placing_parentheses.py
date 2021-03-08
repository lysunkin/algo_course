# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    n = (len(dataset) + 1) // 2

    m = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        m[i][i] = int(dataset[2*i])

    M = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        M[i][i] = int(dataset[2*i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = get_min_and_max(i, j, M, m, dataset)

    return M[0][-1]

def get_min_and_max(i, j, M, m, dataset):
    ret_min = math.inf
    ret_max = -math.inf

    for k in range(i, j):
        maxmax = evalt(M[i][k], M[k+1][j], dataset[2*k+1])
        maxmin = evalt(M[i][k], m[k+1][j], dataset[2*k+1])
        minmax = evalt(m[i][k], M[k+1][j], dataset[2*k+1])
        minmin = evalt(m[i][k], m[k+1][j], dataset[2*k+1])
        ret_min = min(ret_min, maxmax, maxmin, minmax, minmin)
        ret_max = max(ret_max, maxmax, maxmin, minmax, minmin)

    return ret_min, ret_max

if __name__ == "__main__":
    print(get_maximum_value(input()))
