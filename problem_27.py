#producting as many as primes with n^2 + a*n + b
#abs(a)<1000 & abs(b)<=1000
#some constraints: n = 0 ===> b has to be prime
#n = 1 ===> 1+a+b has to be prime?
from math import sqrt

def isPrime(number):
	if number < 2:
		return False
	else:
	    for i in range(2,int(sqrt(number)+1)):
	        if (number%i == 0):
	            return False
	    return True

#b can only take on these values
primes = list(filter(isPrime, range(2,1000)))

def consecutiveprimes(a,b):
	n = 0
	while 1:
		if isPrime(n**2+a*n+b):
			n += 1
		else:
			return n

score = 0
out = 0

for a in range(-999,1000):
	for b in primes:
		temp = consecutiveprimes(a,b)
		if temp>score:
			score = temp
			print("score: ",score)
			print(a,b)
			out = a*b
print(out)
#-61, 971 pair generates primes up to n=71