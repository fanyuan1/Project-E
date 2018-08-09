from math import sqrt

pentagonal = [n*(3*n-1)//2 for n in range(1,9999)]

def isPentagonal (n):
	m = (1+sqrt(1+12*n*2))/6
	return m.is_integer()


def run():
	for i in range(len(pentagonal)):
		for j in range(i):
			if (isPentagonal(pentagonal[i] + pentagonal [j]) & isPentagonal(pentagonal[i] - pentagonal[j])):
				print (pentagonal[i] - pentagonal[j])
				return 0
run()


