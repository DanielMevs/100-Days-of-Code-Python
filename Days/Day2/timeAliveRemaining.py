#tells you how long you have to live assuming you 
#live until 90 years old


age = input("What is your current age?\n")
age = int(age)

yearsRemaining = 90 - age
weeksRemaing = yearsRemaining * 52
monthsRemaining = yearsRemaining * 12

print(f"You have {yearsRemaining} years remaing")
print(f"You have {weeksRemaing} weeks remaining")
print(f"You have {monthsRemaining} months remaining")

