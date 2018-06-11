from projecteuler import isPrime
from math import log

def tructprime(n):

	if isPrime(n):

		m = n % 10 ** int(log(n,10))
		n = n//10
		while n != 0:
			if isPrime(n):
				n = n//10
			else:
				return False

		while m > 10:		
			if isPrime(m):
				m = m % 10 ** int(log(m,10))
			else:
				return False

		return(isPrime(m))
		
	else:
		return False

ttl = 0
counter = 0
i = 11

while counter < 11:
	if tructprime(i):
		ttl += i
		counter += 1
	i+=2

print(ttl)