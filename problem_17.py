counts = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,0:0,
          10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,
         20:6,30:6,40:6,50:5,60:5,70:7,80:6,90:6}

def lettercount(n):
    if n == 0:
        return -3
    counter = 0
    if n//100 > 0:
        #triple digit number, adding 7 for "hundred" and 3 for "and"
        counter = counter + 10 + counts[n//100]
        return counter + lettercount(n%100)
    else:
        #one or two digits number
        if n in counts:
            return counts[n]
        else:
            #two digits above 20
            return counts[n%10] + counts[n//10*10]

from functools import reduce
reduce (lambda x,y : x+lettercount(y), list(range(1,1000)),0) + 11