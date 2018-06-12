from math import sqrt

squares = [i*i for i in range(1,1000)]

all_pairs = {}

for items in squares:
	diff = [x - items for x in squares]
	matches = list(filter(lambda x: x in squares, diff))

	for i in matches:
		p = sqrt(items)+sqrt(i)+sqrt(items+i)
		if p < 1000:
			if p in all_pairs:
				all_pairs[p] += 1
			else:
				all_pairs[p] = 1

most_occ = max(all_pairs.values())

for key, val in all_pairs.items():
	if val == most_occ:
		print(key)