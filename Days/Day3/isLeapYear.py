"""To determine if there's a leap year, the year
has to be evenly dvisible by 4
EXCEPT if the year is evenly divisible by 100 unless
it's also divisible by 400
"""
year = int(input("Which year do you want to check? \n"))

def isLeapYear(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				return True
			else:
				return False
	return False

print(isLeapYear(year))