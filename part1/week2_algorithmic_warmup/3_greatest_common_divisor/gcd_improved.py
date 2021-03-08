# Uses python3
import sys

def gcd(a, b):
	if b == 0:
		return a

	rem = a%b
	return gcd(b, rem)

if __name__ == "__main__":
	input = sys.stdin.read()
	a, b = map(int, input.split())
	print(gcd(a, b))
