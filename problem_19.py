import datetime
#class datetime.date(year, month, day)

counter = 0

for year in range(1901,2001):
	for month in range(1,13):
			if datetime.date(year, month, day=1).weekday() == 6:
				counter += 1

print(counter)