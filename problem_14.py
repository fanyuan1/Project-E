def chain(n):
    if n in dictionary:
        return dictionary[n]
    else:
        if n%2 == 0:
            return 1+chain(n//2)
        else:
            return 2+chain((3*n+1)//2)

longest = 2
num = 2
length = 0
dictionary = {1:1,2:2}

for i in range(1,1000001):
    length = chain (i)
    if length > longest:
        num = i
        longest = length
        
print(num)