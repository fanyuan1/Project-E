#bruteforce...
def run():
	for a in range(1,999):
		for b in range(1,999):
			c = 1000-b-a
			if a**2 + b**2 == c**2:
				return a*b*c

print(run())

#alternate solution
#a^2+b^2=(1000-a-b)^2 => a = 1000*(b-500)/(b-1000)
#both a, b are less than 500 for the natural number restrictions to hold

def run2():
	for a in range(1,500):
		b = 1000*(a-500)/(a-1000)
		if b%1 == 0:
			return int(a*b*(1000-a-b))

print(run2())
