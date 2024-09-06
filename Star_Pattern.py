import turtle

# Fullscreen the canvas
screen = turtle.Screen()
turtle.speed(50)
turtle.pensize(4)
#screen.setup(1.0, 1.0)


x = input("What backround colour do you want : ")
y = input("What pen colour do you want : ")

screen.bgcolor(x)
turtle.color(y)


count = 0
while count < 20 :
  turtle.forward(200)
  turtle.right(90)
  turtle.right(100)
  count = count + 1
  
turtle.hideturtle()





#turtle.circle(20)
# print("My name is Zayn")
# x = input("What is your name : ")
# print("My name is " + x)

# y = input("What is your favourite food : ")
# print(y)

screen.mainloop()


## Homework
#1. Practice the star pattern program in edublocks
#2. Create a new copy of Snowman, and use the concept of turtle color and background color in it.