#Password Generator Project
#author: Daniel Mevs
#notes: generally, the random module is not recommended for security purposes
import random

def passWordGenerator():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	print("Welcome to the PyPassword Generator!")
	nr_letters= int(input("How many letters would you like in your password?\n")) 
	nr_symbols = int(input(f"How many symbols would you like?\n"))
	nr_numbers = int(input(f"How many numbers would you like?\n"))

	totalLength = nr_numbers + nr_letters + nr_symbols

	randomLetters = []
	for i in range(0, nr_letters):
		randomLetters.append(letters[random.randint(0, len(letters) - 1)])
	del letters

	randomNumbers = []
	for i in range(0, nr_numbers):
		randomNumbers.append(numbers[random.randint(0, len(numbers) - 1)])
	del numbers

	randomSymbols = []
	for i in range(0, nr_symbols):
		randomSymbols.append(symbols[random.randint(0, len(symbols) - 1 )])
	del symbols


	category = ["letters", "numbers", "symbols"]
	genDict = {"letters": randomLetters, "numbers": randomNumbers, "symbols": randomSymbols}
	#print(genDict)

	del randomLetters
	del randomNumbers
	del randomSymbols

	newPassWordList = []
	currentCategory = category[random.randint(0, len(category) - 1)]

	while len(newPassWordList) <= totalLength or category:
		if not genDict[currentCategory]:
			del genDict[currentCategory]
			category.remove(currentCategory)
			#print(category)
			if not category:
				break
			currentCategory = category[random.randint(0, len(category) -1)]
			continue
		lastRandomCharIdx = len(genDict[currentCategory]) - 1
		newPassWordList.append(genDict[currentCategory][lastRandomCharIdx])
		genDict[currentCategory].pop()
		currentCategory = category[random.randint(0, len(category) - 1)]
		#print(newPassWordList)

	#del category

	newPassWord = "".join(newPassWordList)

	print(f"Your new password is {newPassWord}")

	#random.choice and random.shuffle are also useful methods
