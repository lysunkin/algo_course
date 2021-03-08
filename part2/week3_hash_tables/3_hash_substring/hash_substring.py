# python3

import random

_prime = 1000000007

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash_func(s, p, x):

    h = 0

    for c in reversed(s):
        h = ((h * x + ord(c)) % p + p) % p

    return h

def precompute(pattern, text, p, x):

    remaining_len = len(text) - len(pattern)
    result = [None] * (remaining_len + 1)
    substring = text[remaining_len:len(text)]
    result[remaining_len] = hash_func(substring, p, x)

    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in range(remaining_len - 1, -1, -1):
        result[i] = (x * result[i+1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % p

    return result

def get_occurrences(pattern, text):

    x = random.randint(0, _prime)

    result = []
    pattern_hash = hash_func(pattern, _prime, x)
    hashes = precompute(pattern, text, _prime, x)
    remaining_len = len(text) - len(pattern)

    for i in range(0, remaining_len + 1):
        if pattern_hash != hashes[i]:
            continue
        if text[i:i+ len(pattern)] == pattern:
            result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
