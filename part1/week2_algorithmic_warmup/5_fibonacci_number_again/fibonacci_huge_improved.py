# Uses python3
import sys

def get_pisano_period(m):
    a = 0
    b = 1
    c = a + b
    i = 0
    while i < m * m:
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1
        i = i+1

def get_fibonacci_huge(n, m):
    remainder = n % get_pisano_period(m)

    first = 0
    second = 1

    res = remainder

    i = 1
    while i < remainder:
        res = (first + second) % m
        first = second
        second = res
        i = i+1

    return res % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
