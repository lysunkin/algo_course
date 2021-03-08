# python3

def max_pairwise_product(numbers):
    n = len(numbers)
    maxItem = 0
    secondToMaxItem = 0
    for i in range(n):
        if numbers[i] > maxItem:
            secondToMaxItem = maxItem
            maxItem = numbers[i]
        elif numbers[i] > secondToMaxItem:
            secondToMaxItem = numbers[i]

    return maxItem * secondToMaxItem


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
