#cancel digits from each a,b. given a != b, the two digits cannot be from the same decimal place
# a<b given by problem restrictions

out_a = 1
out_b = 1
for a in [x for x in range(10,100) if x%10 != 0]:
	for b in [x for x in range(a+1,100) if x%10 != 0]:
		if a/b == (a//10) / (b-(10*(a%10))):
			out_a *= a
			out_b *= b

from fractions import Fraction
print(Fraction(out_a,out_b))

