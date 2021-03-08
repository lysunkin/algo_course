# Uses python3
import sys

def get_change(m):
    fourth = m // 4
    rem = m % 4
    third = rem // 3
    ones = rem % 3
    # fix greedy approach by noticing that if we have two coins of one we can optimize
    if ones == 2 and fourth >= 1:
        fourth -= 1
        third += 2
        ones -= 2
    n = ones+third+fourth

    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
