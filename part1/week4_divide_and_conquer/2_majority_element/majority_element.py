# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    a.sort()

    majority_count = len(a)//2+1
    max_count = 0
    current_elem = ''
    for item in a:
        if current_elem != item:
            if max_count >= majority_count:
                return current_elem
            max_count = 1
            current_elem = item
        else:
            max_count += 1

    if max_count >= majority_count:
        return current_elem

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
