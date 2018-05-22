#brute force loop
out = 0
i = 1
j = 2

while i <= 4000000:
	if i % 2 == 0:
		out += i
	i = i+j
	i,j = j,i

print(out)