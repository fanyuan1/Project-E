from projecteuler import isPrime
from functools import reduce

prime_sum = [2]

for i in range(3,1000000):
	if isPrime(i):
		prime_sum.append(prime_sum[-1]+i)

most_consec = 21

for i in range(most_consec,len(prime_sum)):
	for j in range(i-(most_consec+1),0,-1):
		if (prime_sum[i]-prime_sum[j] > 1000000):
			break
		if isPrime(prime_sum[i]-prime_sum[j]):
			most_consec = i-j
			result = prime_sum[i]-prime_sum[j]

print(result)