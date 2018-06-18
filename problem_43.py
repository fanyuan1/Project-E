from itertools import permutations

perm = permutations([0,1,2,3,4,5,6,7,8,9])

divisors = [2,3,5,7,11,13,17]

def checker (l):
	if l[0] == 0:
		return False
	for i in range(1,8):
		if ((l[i]*100+l[i+1]*10+l[i+2]) % divisors[i-1]) != 0:
			return False
	return True

ttl = 0

for l in perm:
	if checker(l):
		temp = list(map(str,l))
		temp = ''.join(x for x in temp)
		ttl += int(temp)

print(ttl)