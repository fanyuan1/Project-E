#code super  slowwww

from math import sqrt

def unique_divisors(number):
	if number == 1:
		return 0
	for i in range(2,int(sqrt(number)+1)):
		if number%i == 0:
			while number%i == 0:
				number = number//i
			return 1 + unique_divisors(number)
	return 1


cont_count = 0

for i in range(1000000):
	print(i)
	if unique_divisors(i) == 4:
		cont_count += 1
	elif cont_count == 4:
		print(i-4)
		break
	else:
		cont_count = 0

