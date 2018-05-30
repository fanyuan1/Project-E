from projecteuler import fact

def checker(n):
	ttl = 0
	for digits in str(n):
		ttl += fact(int(digits))
	if n == ttl:
		return True
	else:
		return False

from functools import reduce

print(reduce(lambda x,y: x+checker(y)*y, range(3,100000), 0))

#Much cooler solution
factorials = [1,1,2,6,24,120,720,5040,40320,362880]
out = 0
for n in range(3,100000):
	if n == sum(factorials[int(i)] for i in str(n)):
		out += n
print(out)
