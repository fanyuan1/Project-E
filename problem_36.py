from projecteuler import isPalindromeStr

ttl = 0

for i in range(1,1000000,2):
	if isPalindromeStr(str(i)) & isPalindromeStr(bin(i)[2:]):
		ttl += i

print(ttl)