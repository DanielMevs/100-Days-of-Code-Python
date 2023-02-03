enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()
# print(player_health)
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

# this won't work this time because it's inside the scope of another function
# drink_potion()

print(player_health)

if 3 > 2:
    a_variable = 3