from math import sqrt
#quadratic formula

def isPentagonal (n):
	m = (1+sqrt(1+12*n*2))/6
	return m.is_integer()

def isTriangle(n):
	m = (-1+sqrt(1+8*n))/2
	return m.is_integer()

hexagonal = [n*(2*n-1) for n in range(1,99999)]

print(list(filter(lambda x: isPentagonal(x)&isTriangle(x),hexagonal)))