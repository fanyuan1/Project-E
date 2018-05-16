#borrowing from problem_4 isPrime function
from math import sqrt
from functools import reduce

def isPrime(number):
    for i in range(2,int(sqrt(number)+1)):
        if (number%i == 0):
            return 0
    return number

print(reduce((lambda x, y: x + isPrime(y) ),range(3,2000000,2),2))