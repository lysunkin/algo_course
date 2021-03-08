# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1

    while left <= right: 
        middle = (right + left) // 2
        if a[middle] < x: 
            left = middle + 1
        elif a[middle] > x: 
            right = middle - 1
        else: 
            return middle 
  
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #for x in data[n + 2:]:
    #    print(linear_search(a, x), end = ' ')
    #print()
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
