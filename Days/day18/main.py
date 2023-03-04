from turtle import Turtle
import random

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# - Square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# - Dashed Line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

colors = ["CornflowerBlue", "SeaGreen", "SlateGray", "Indian Red", "wheat", "LightSeaGreen"]
# - Drawing different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for shape_side in range(3 , 11):
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(shape_side)


# screen = Screen()
# screen.exitonclick()