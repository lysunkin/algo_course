# Uses python3
import sys

# Sum of nth Fibonacci series = F((n+2) % 60) - 1

def fibonacci_sum(n):
    previous = 0
    current  = 1

    for _ in range((n + 1) % 60):
        previous, current = current, (previous + current)%10

    if current == 0:
        return 9

    return current - 1 

def fibonacci_partial_sum(from_, to):
    return (10+fibonacci_sum(to)-fibonacci_sum(from_-1))%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
