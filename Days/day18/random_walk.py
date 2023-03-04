from turtle import Turtle
import turtle as t
import random

timmy_the_turtle = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# colors = ["CornflowerBlue", "SeaGreen", "SlateGray", "Indian Red", "wheat", "LightSeaGreen", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(200):
    # timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
