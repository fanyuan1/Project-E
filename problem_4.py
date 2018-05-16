def isPalindrome (number):
    
    trim = number
    palindrome = 0
    
    while (trim>0):
        last = trim%10
        trim = trim//10
        palindrome = last+palindrome*10
        
    if(number == palindrome):
        return True 
    else:
        return False

sol = 0
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        if (i*j>sol) & isPalindrome(i*j):
            sol = i*j    

print(sol)