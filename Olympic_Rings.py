import turtle

screen = turtle.Screen()

screen.bgcolor("white")

turtle.speed(10)

turtle.pensize(5)

def olympic(color,x,y,radius):
  turtle.pencolor(color)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.circle(radius) 

olympic('blue',-150,80,60)
olympic('black',0,80,60)
olympic('red',150,80,60)
olympic('yellow',-70,20,60)
olympic('green',80,20,60)

screen.mainloop()