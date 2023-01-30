#code to paste into reeborg's world to solve the problem of espaping a maze
#the strategy/algorithm we can use is go all the way to the right until there's an obstacle,
#then redirect and keep searching right until we find the exit

def turn_right():
	turn_left()
	turn_left()
	turn_left()

while front_is_clear():
	move()
turn_left()

while not at_goal():
	if right_is_clear():
		turn_right()
		move()
	elif front_is_clear():
		move()
	else:
		turn_left()