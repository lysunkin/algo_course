# Uses python3
import sys

# Sum of nth Fibonacci series = F((n+2) % 60) - 1

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range((n + 1) % 60):
        previous, current = current, (previous + current)%10

    if current == 0:
        return 9

    return current - 1 

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
