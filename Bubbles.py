import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.pensize(3)
turtle.speed(100)

for i in range(15):
    turtle.pencolor("lightgreen")
    turtle.fillcolor("lightgreen")
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.begin_fill()
    i = random.randint(50, 100)
    turtle.circle(i)
    turtle.end_fill()

screen.mainloop()