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


timmy_the_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        # print(timmy_the_turtle.heading())
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + 10)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
