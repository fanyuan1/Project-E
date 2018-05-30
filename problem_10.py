from functools import reduce
from projecteuler import isPrime

print(reduce((lambda x, y: x + isPrime(y) ),range(3,2000000,2),2))