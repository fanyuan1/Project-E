from projecteuler import isPrime

out = 1

#find all primes smaller than 20 and and calculate the highest power that does not exceed 20
for i in range(2,21):
	if isPrime(i):
		j = i
		while j < 20:
			j *= i
		j = j//i
		out *= j	

print(out)