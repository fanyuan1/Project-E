from projecteuler import isPalindrome 

sol = 0
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        if (i*j>sol) & isPalindrome(i*j):
            sol = i*j    

print(sol)