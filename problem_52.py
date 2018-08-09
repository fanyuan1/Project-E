import collections

def same_p(a, b):
	a=str(a)
	b=str(b)
	d = collections.defaultdict(int)
	for x in a:
		d[x] += 1
	for x in b:
		d[x] -= 1
	return not any(d.values())



def run():
	j = 2
	while 1:
		print (j)
		for i in range(10**j, 10**(j+1)//6+1):
			if same_p(i,i*2)&same_p(i,i*3)&same_p(i,i*4)&same_p(i,i*5)&same_p(i,i*6):
				return i
		j+=1

print(run())