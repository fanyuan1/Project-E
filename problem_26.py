#trying to emulate long division
#ofc if a number can be written as a fraction p/q, it must be rational
#find how many loops it takes before the remainder repeats itself
def sequencelen(n):
	remainders = {}
	digits = len(str(n))
	numerator = 10**digits
	while 1:
		remainder = numerator%n
		if remainder in remainders:
			return remainders[remainder]
		else:
			for items in remainders.keys():
				remainders[items] += 1
			remainders[remainder] = 1
		numerator = remainder*10

temp = list(map(sequencelen, range(1,1000)))
print(temp.index(max(temp))+1)