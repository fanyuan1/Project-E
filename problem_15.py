from functools import reduce

def ncr (n,r):
	if r > n//2:
		r = n-r
	bot = reduce (lambda x,y: x*y, range(1,r+1),1)
	top = reduce (lambda x,y: x*y, range(n,n-r,-1),1)
	return top//bot

print(ncr (40,20))