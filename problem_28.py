prev = 1
increment = 2
ttl = 1

for i in range(500):
	ttl += (prev+increment*1+prev+increment*4)*2
	#set up next loop
	prev = prev+increment*4
	increment +=2

print(ttl)