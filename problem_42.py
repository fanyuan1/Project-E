import csv

with open('p042_words.txt', 'r') as f:
  input = list(csv.reader(f))

input = input[0]

convert = [sum((ord(i)-64 for i in j)) for j in input]

# generate triangle numbers
triangle_nums = [1]
n = 2
while triangle_nums[-1] < max(convert):
    triangle_nums.append(int(0.5*n*(n+1)))
    n += 1
    
print(len([x for x in convert if x in triangle_nums]))