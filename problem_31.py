coins = [200,100,50,20,10,5,2,1]

counter = 0

def perm(n,i):
	ways = 0
	current_coin = coins[i]
	if n == 0:
		return 1
	elif current_coin == 1:
		return 1
	else:
		for j in range(n//current_coin+1):
			ways += perm(n-current_coin*j,i+1)
		return ways

print (perm(200,0))