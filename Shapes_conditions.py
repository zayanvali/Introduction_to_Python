import turtle
x = turtle.Screen()
x1 = int(input("What shape do you want to draw: \nEnter 1 for Square \nEnter 2 for Circle \nEnter 3 for Rectangle \nEnter your selection : "))

if x1 == 1:
    for i in range (4):
        turtle.forward(100)
        turtle.right(90)

if x1 == 2:
    turtle.circle(100)

if x1 == 3:
    for i in range (2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

x.mainloop()