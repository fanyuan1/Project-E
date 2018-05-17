from math import sqrt
from functools import reduce

def factorize(n):
    for i in range(2,int(sqrt(n)+1)):
        if (n%i == 0):
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
            return factorize(n//i)
    if n in factors:
        factors[n] += 1
    else:
        factors[n] = 1
        
i = 0
j = 0
while 1:
    j += 1
    i += j
    factors = {}
    factorize(i)
    if(reduce(lambda x, y: x * (y+1), list(factors.values()),1)>500):
        print(i)
        break