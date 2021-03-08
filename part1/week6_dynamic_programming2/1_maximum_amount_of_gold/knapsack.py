# Uses python3
import sys

def optimal_weight(W, w):

    n = len(w)

    value_matrix = [[0 for col in range(W + 1)] for row in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            value_matrix[i][j] = value_matrix[i-1][j]
            if w[i-1] <= j:
                local = value_matrix[i-1][j - w[i-1]] + w[i - 1]
                if local > value_matrix[i][j]:
                    value_matrix[i][j] = local

    # last cell in table
    return value_matrix[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
