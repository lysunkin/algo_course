#Uses python3

import sys
import functools 

def largest_number(a):
    res = ""

    a.sort(key = functools.cmp_to_key(lambda x, y: -1 if str(y) + str(x) < str(x) + str(y) else 1))

    for x in a:
        res += x

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
