# Uses python3
from sys import stdin

def get_pisano_period(m):
    a, b = 0, 1
    i = 0
    while i < m * m:
        a, b = b, (a + b) % m
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

def fibonacci_sum_squares(n):
    return get_fibonacci_huge(n, 10)*get_fibonacci_huge(n+1, 10)%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
