#there are 10! permutations in total
def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

n = 1000000-1

digits = '0123456789'
digits = list(digits)
out = []

#if we focus on the last 9 digits there are 9! permutations

while len(digits) > 0:
	perms = fact(len(digits)-1)
	out.append(digits.pop(n//perms))
	n = n%perms

print(out)