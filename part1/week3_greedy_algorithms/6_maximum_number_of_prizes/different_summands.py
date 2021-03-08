# Uses python3
import sys

def optimal_summands(n):
    summands = []

    i = 0
    s = 0
    ps = 0
    while s < n:
        ps = s
        s += i+1
        if s > n:
            summands[i-1] += (n-ps)
            break
        summands.append(i+1)
        i += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
