#this took a long time to run, very nonoptimal
from math import sqrt

def isPrime(number):
	if number < 2:
		return False
	else:
	    for i in range(2,int(sqrt(number)+1)):
	        if (number%i == 0):
	            return False
	    return True

primes = [x for x in range(2,1000000) if isPrime(x)]
non_circular_p = primes[:]

for i in primes:

	l_i = list(str(i))

	if len([x for x in l_i if int(x)%2==0 or int(x) == 5])>0:
		continue
	else: 
		no_good = 0
		for j in range(len(l_i)-1):
			#rotate to next number
			l_i.append(l_i.pop(0))

			temp = int(''.join(l_i))

			if temp not in primes:
				no_good = 1
				break

		if no_good == 0:
			non_circular_p.pop(non_circular_p.index(i))

non_circular_p.pop(non_circular_p.index(2))

#print([x for x in primes if x not in non_circular_p])
print(len(primes)-len(non_circular_p))
