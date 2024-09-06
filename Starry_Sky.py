import turtle
import random

screen = turtle.Screen()
screen.bgcolor("indigo")
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

    count = 0
    turtle.begin_fill()
    while count<6:
        turtle.forward(100)
        turtle.left(144)
        count = count+1
    turtle.end_fill()
    turtle.right(45)

screen.mainloop()