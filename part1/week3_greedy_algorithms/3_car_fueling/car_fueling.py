# python3
import sys

def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current = 0
    limit = tank
    n = len(stops)

    while limit < distance:
        if current >= n or stops[current] > limit:
            return -1

        while current < n-1 and stops[current+1] <= limit:
            current += 1

        limit = stops[current] + tank 

        num_refills = num_refills + 1
        current += 1

    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
