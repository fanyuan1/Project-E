#since 9^5 = 59,049, assume we test a 6 digit number, the maximum the sum can be is
#59,049*6 = 354,294

def sumoffifthpower(n):
	if n//10 == 0:
		return n**5
	else:
		return (n%10)**5+sumoffifthpower(n//10)

ttl = 0

for i in range(2,354294):
	if i == sumoffifthpower(i):
		ttl += i

print(ttl)