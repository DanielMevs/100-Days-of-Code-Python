size = input("What size pizza do you want? Small (S), medium (M), or large (L) \n")
price = 0
if size.upper() == 'S':
	price += 15
elif size.upper() == 'M':
	price += 20
else:
	price += 25

pepperoni = input("Do you want pepperoni? Y N\n")
if pepperoni.upper() == 'Y':
	if size == 'M' or size == 'S':
		price += 2
	else:
		price += 3

extraCheese = input("Do you want extra cheese? Y N\n")
if extraCheese.upper() == 'Y':
	price += 1

print(f"Your total price is ${price}")
