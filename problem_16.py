from functools import reduce
print(reduce(lambda x, y : x+int(y), list(str(int(2**1000))),0))

sum = 0
for i in str(2**1000):
	sum += int(i)
print(sum)