import math;
def Perimeter_Rectangle(x, y): 
    return 2 * (x + y)

def Area_Rectangle(x, y):
    return x*y

def Perimeter_Square(x):
    return 4*x 

def Area_Square(x):
    return x*x

def Perimeter_Triangle(x, y, z):
    return x + y + z

def Area_Triangle(x, y):
    return (x*y)/2

def Circumference_Circle(x):
    return x*math.pi

def Area_Circle(x):
    return math.pi*x*x

print("Welcome to Shape Wise Calculation program!")
print("Please select an operation to proceed further : \n1. Perimeter of Rectangle \n2. Area of Rectangle \n3. Perimeter of Square \n4. Area of Square \n5. Perimeter of triangle \n6. Area of triangle \n7. Circumference of Circle \n8. Area of Circle")
choice = int(input("Enter your selection: "))
if choice == 1:
    x = int(input("Enter the length of rectangle: "))
    y = int(input("Enter the height of rectangle: "))
    print("The perimeter of rectangle is : ", Perimeter_Rectangle(x, y))

if choice == 2:
    x = int(input("Enter the length of rectangle: "))
    y = int(input("Enter the height of rectangle: "))
    print("The area of rectangle is : ", Area_Rectangle(x, y))

if choice == 3:
    x = int(input("Enter the length of square: "))
    print("The perimeter of square is : ", Perimeter_Square(x))

if choice == 4:
    x = int(input("Enter the length of square: "))
    print("The area of square is : ", Area_Square(x))

if choice == 5:
    x = int(input("Enter the length of side 1: "))
    y = int(input("Enter the length of side 2: "))
    z = int(input("Enter the length of side 3: "))
    print("The perimeter of triangle is : ", Perimeter_Triangle(x, y, z))

if choice == 6:
    x = int(input("Enter the length of side : "))
    y = int(input("Enter the height of side : "))
    print("The area of triangle is : ", Area_Triangle(x, y))

if choice == 7:
    x = int(input("Enter the length of diameter : "))
    print("The circumference of circle is : ", Circumference_Circle(x))

if choice == 8:
    x = int(input("Enter the length of radius : "))
    print("The area of circle is : ", Area_Circle(x))