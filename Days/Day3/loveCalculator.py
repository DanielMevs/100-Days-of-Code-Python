name1 = input("Enter first person's name: ")
name2 = input("Enter second person's name: ")

full_name = (name1 + name2).lower()

t=full_name.count('t')
r=full_name.count('r')
u = full_name.count('u')
e = full_name.count('e')

true = t+r+u+e

l= full_name.count('l')
o=full_name.count('o')
v=full_name.count('v')
e=full_name.count('e')

love = l+o+v+e
love_score = str(true) + str(love)
love_score = int(love_score)

print(love_score)

if love_score < 10 or love_score > 90:
	print(f"your love score is {love_score}, you go together like coke and mentos")

elif love_score >= 40 and love_score <= 50:
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"your score is {love_score}\n")