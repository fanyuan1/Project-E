from projecteuler import isPrime
from itertools import permutations

primes = []

for i in range(1009,9974):
	if isPrime(i):
		primes.append(i)


for i in primes:
	perms = list(permutations(str(i)))
	perm_primes = []
	for j in perms:
		k = int(j[0])*1000+int(j[1])*100+int(j[2])*10+int(j[3])
		if k in primes:
			perm_primes.append(k)

	if len(perm_primes) >= 3:
		for l in perm_primes:
			if (l+3330 in perm_primes) & (l+6660 in perm_primes):
				print(l,l+3330,l+6660)