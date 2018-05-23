from math import log10

index = 3
n = 2
n_1 = 1

while int(log10(n))+1 < 1000:
	index += 1
	n, n_1 = n+n_1, n

print (index)