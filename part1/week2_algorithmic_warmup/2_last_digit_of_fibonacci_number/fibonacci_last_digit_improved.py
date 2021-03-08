# Uses python3
def calc_last_fib_digit(n):
	if (n <= 1):
		return n

	i = 1
	a, b = fib_last_digit_basic()
	while i < n-1:
		a, b = fib_last_digit_basic(a, b)
		i = i+1
	return b

def fib_last_digit_basic(a=0, b=1):
	a, b = b, (a+b)%10
	return a, b

n = int(input())
print(calc_last_fib_digit(n))
