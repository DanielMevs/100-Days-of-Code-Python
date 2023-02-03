''' these enemies are different'''
# enemies = 1

# def increase_enemies():
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


''' these enemies are the same'''
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")