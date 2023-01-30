print("Welcome to the rollercoaster!")
height = int(input("What is your heigt in cm? "))
bill = 0

if height >= 120:
	print("You can ride the rollercoaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print(f"child tickets are ${bill}.")
	elif age <= 18:
		bill = 7
		print(f"youth tickets are ${bill}")
	elif age >= 45 and age <= 55:
		bill = 0
		#for someone who is going through a mid-life crisis
		print("Everything is going to be ok. Have a free ride on us!")
	else:
		bill = 12
		print(f"Adult tickets are ${bill}.")

	wantsPhoto = input("Do you want a photo taken? Y or N ")

	if wantsPhoto.upper() == "Y":
		bill += 3
	print(f"Your final bill is ${bill}")

else:
	print("Sorry, you have to grow taller before you can ride.")