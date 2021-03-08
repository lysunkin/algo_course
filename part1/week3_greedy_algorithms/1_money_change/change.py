# Uses python3
import sys

def get_change(m):
    tens = m // 10
    rem = m%10

    fives = rem // 5
    rem = m%5
   
    ones = rem

    return tens+fives+ones

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
