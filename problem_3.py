from math import sqrt

n = 600851475143

def factors(n):
	for i in range(2,int(sqrt(n)+1)):
		if (n%i == 0):
			return factors(n//i)
	print(n)

factors(n)