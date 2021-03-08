# Uses python3
import sys

from collections import namedtuple

Item = namedtuple('Item', ['w', 'v'])

def get_optimal_value(capacity, weights, values):
    value = 0.

    if len(weights) != len(values):
        return value

    if len(weights) == 0:
        return value

    items = [Item(weights[i], values[i]) for i in range(0, len(values))]
    items.sort(key=lambda x: x.v/x.w, reverse=True)

    for item in items:
        if capacity == 0:
            break

        weight = item.w
        val = item.v
        if weight > capacity:
            fraction = val/weight*capacity
            value += fraction
            capacity = 0
        else:
            value += val
            capacity = capacity-weight

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
