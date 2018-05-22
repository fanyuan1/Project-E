from math import sqrt

def isPrime(number):
    for i in range(2,int(sqrt(number)+1)):
        if (number%i == 0):
            return False
    return True

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