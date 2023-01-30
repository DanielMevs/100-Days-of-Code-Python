import random
#in London, which is a finacial hotspot, bankers at restarents will 
#put their credit cards in a bowl and randomly pick a card
#The person who has their card chosen pays for everyone's bill
names_string = input("Give me everybod's names, seperated by a coma. ")
names = names_string.split(", ")

random_choice = random.randint(0, len(names) - 1)
person_who_will_pay = names[random_choice]

#alternatively
#person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to pay for the meal today!")
