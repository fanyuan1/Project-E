#brute force
#find how many numbers we have to concat... 9 1 digit numbers, 90 2 digit numbers,... so on

i = 1
count = 1000000

while count > i*9*10**(i-1):
	count -= i*9*10**(i-1)
	i += 1

top_num = count//i + sum([10**(i-1)-1]) + 1

string = ""

for i in range(top_num+1):
	string += str(i)

print(int(string[1])*int(string[10])*int(string[100])*int(string[1000])*int(string[10000])*int(string[100000])*int(string[1000000]))