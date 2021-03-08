# Uses python3
def calc_fib(n):
	if (n <= 1):
		return n

	i = 1
	a, b = fib_basic()
	while i < n-1:
		a, b = fib_basic(a, b)
		i = i+1
	return b

def fib_basic(a=0, b=1):
	a, b = b, a+b
	return a, b

n = int(input())
print(calc_fib(n))
