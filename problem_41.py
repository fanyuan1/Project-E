from projecteuler import isPrime
#from itertools import permutations

def isPandigital (num):
	for i in range(1,len(str(num))+1):
		if str(i) not in str(num):
			return False
	return True

for num in range(7654321,3,-2):
	if isPandigital(num) & isPrime(num):
		print(num)
		break

#print(list(filter(lambda x: isPandigital(x), range(987654321,3,-2))))
#print(list(filter(lambda x: isPrime(x), range(987654321,3,-2))))

