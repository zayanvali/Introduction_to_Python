import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.pensize(3)
turtle.speed(100)

for i in range (15):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    i = 36

    while i>0:
        i = i-1
        a = random.randint(40, 80)
        turtle.forward(a)
        turtle.backward(a)
        turtle.left(10)

screen.mainloop()