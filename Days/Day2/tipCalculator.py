print("Welcome to the tip calculator\n")
billTotal = float(input("What was the total bill? "))
tipPercentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
numOfPeople = int(input("How many people to split the bill? "))

tipPercentage *= .01
tipTotal = billTotal * tipPercentage
eachPersonPay = tipTotal / numOfPeople

print(f"\nEach person should pay: ${eachPersonPay:.2f} \n")
'''
#alternatively
finalAmount = "{:.2f}".format(eachPersonPay)
print(f"Each person should pay: ${eachPersonPay} \n")

'''