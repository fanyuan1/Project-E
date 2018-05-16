from math import sqrt
def isPrime(number):
    for i in range(2,int(sqrt(number)+1)):
        if (number%i == 0):
            return False
    return True

counter = 1
n = 3
current = 2

while(counter < 10001):
    if isPrime(n):
        counter += 1
        current = n
        n += 2
    else:
        n += 2

print(current)