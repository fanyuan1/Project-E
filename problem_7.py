from projecteuler import isPrime

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