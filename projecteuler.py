def isPrime(number):
	from math import sqrt
	if number < 2:
		return False
	else:
	    for i in range(2,int(sqrt(number)+1)):
	        if (number%i == 0):
	            return False
	    return True

def isPalindromeStr(n):
	if (n == n[::-1]):
		return True
	else:
		return False

#palindrome checker number
def isPalindrome(number):
    
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

#factorial
def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

#nCr
def ncr (n,r):
	from functools import reduce
	if r > n//2:
		r = n-r
	bot = reduce (lambda x,y: x*y, range(1,r+1),1)
	top = reduce (lambda x,y: x*y, range(n,n-r,-1),1)
	return top//bot
