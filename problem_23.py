#find Non-abundant sums
def isAbundant(n):
	counter = 1
	for i in range(2,n//2+1):
		if n%i == 0:
			counter += i
	return counter>n

abundantlist = []

for i in range(12,28112):
	if isAbundant(i):
		abundantlist.append(i)

l = [[x+y for x in abundantlist if x+y < 28124] for y in abundantlist]

new_l = []
for sublist in l:
    for i in sublist:
        new_l.append(i)

print (sum(range(28124))-sum(set(new_l)))