# Uses python3
import sys

def merge_sort_num_of_inv(a):
    n = len(a)
    num_of_inversions = 0
    if n == 1:
        return a, num_of_inversions
    mid = n // 2
    b, n1 = merge_sort_num_of_inv(a[:mid])
    num_of_inversions += n1
    c, n2 = merge_sort_num_of_inv(a[mid:])
    num_of_inversions += n2
    a_new, n3 = merge_num_of_inv(b, c)
    num_of_inversions += n3
    return a_new, num_of_inversions

def merge_num_of_inv(b, c):
    d = list()
    num_of_inversions = 0
    while (len(b) != 0) and (len(c) != 0):
        if b[0] <= c[0]:
            d.append(b[0])
            b = b[1:]
        else:
            d.append(c[0])
            c = c[1:]
            num_of_inversions += len(b)
    d.extend(b)
    d.extend(c)
    return d, num_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
