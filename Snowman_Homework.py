import turtle

screen = turtle.Screen()
x = input("What backround colour do you want : ")
y = input("What pen colour do you want : ")

screen.bgcolor(x)
turtle.color(y)

# Snowman
for zan in range(36):
  turtle.forward(18)
  turtle.right(10)

# Second circle of snowman
for zan in range(54):
  turtle.forward(12)
  turtle.left(10)

for zan in range(36):
  turtle.forward(8)
  turtle.right(10)

# Drawing left eye of Snowman

turtle.penup()
turtle.goto(-14, 205)
turtle.pendown()
turtle.circle(4)

# Draw right eye of snowman
turtle.penup()
turtle.goto(26, 205)
turtle.pendown()
turtle.circle(4)

# Draw smile of snowman
turtle.penup()
turtle.goto(-16,175)
turtle.pendown()
turtle.left(90)

for i in range(20):
  turtle.forward(4)
  turtle.left(10)


screen.mainloop()

## Homework : Complete the third circle of snowman as homework

## 13/04/2024 --- Replicate the remaining part of edublocks code from here and check if the program is running fine