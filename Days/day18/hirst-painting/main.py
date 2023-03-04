import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
hirst_colors = [(202, 10, 34), (247, 236, 36), (241, 231, 3), (34, 217, 77), (224, 159, 62), (39, 79, 185), (28, 38, 160), (212, 71, 14), (18, 151, 21), (241, 36, 152), (188, 15, 10), (219, 22, 129), (73, 8, 28), (219, 140, 198), (59, 13, 8), (225, 160, 5), (65, 202, 228), (18, 17, 41), (10, 97, 60), (83, 74, 216), (94, 206, 136), (238, 158, 219), (97, 235, 194), (4, 230, 242), (223, 79, 47), (5, 71, 45)]


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(hirst_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()