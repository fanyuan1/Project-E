#brute force

def checker (m,n):
	concat = str(m)+str(n)+str(m*n)
	if '0' in concat or len(concat)!=9 or m*n in qualifiers:
		return False
	else:
		digits = []
		for items in concat:
			if items in digits:
				return False
			else:
				digits.append(items)
		print(m,n,m*n)
		qualifiers.append(m*n)

qualifiers = []

for i in range(9999):
	for j in range(999):
		checker(i,j)

print(sum(qualifiers))