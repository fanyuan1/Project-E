from projecteuler import isPrime
from math import sqrt

i = 1

def checker(n):
	for i in range(1,int(sqrt(n/2))+1):
		if isPrime(n-2*i*i):
			return True
	return False


def run():
	i = 1
	while 1:
		n = 2*i+1
		if isPrime(n) or checker (n):
			i += 1
			continue
		return n

print(run())