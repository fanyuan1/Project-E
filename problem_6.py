#
term1 = ((1+100)*100//2)**2

term2 = 0
for i in range(100):
	term2 += (i+1)**2

print(term1-term2)