def sumofdivisor(n):
	counter = 1
	for i in range(2,n//2+1):
		if n%i == 0:
			counter += i
	return counter

out = 0

for i in range(10000):
	n = sumofdivisor(i)
	if (i != n) & (i == sumofdivisor(n)):
		out = out + i + n

print(out//2)