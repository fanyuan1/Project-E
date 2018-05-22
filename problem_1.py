#thanks to Gauss
n = 999

#sum of multiple of 3
multi3 = (3+n//3*3)*(n//3)//2

#sum of multiple of 5
multi5 = (5+n//5*5)*(n//5)//2

#sum of multiple of 15
multi15 = (15+n//15*15)*(n//15)//2

print(multi3+multi5-multi15)