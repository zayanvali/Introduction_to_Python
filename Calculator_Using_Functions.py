# Calculator actions - Addition, Subtraction, Multiplication, Division, Quotient, Remainder

def Add(x, y):
    return x+y

def Subtract(x, y):
    return x-y

def Multiplication(x, y):
    return x*y

def Division(x, y):
    return x/y

def Quotient(x, y):
    return x//y

def Remainder(x, y):
    return x%y


print("Welcome to the Calculator program by Zayn!!")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
ans = "y"

while ans == "y" or ans == "Y":
    
    print("Please select an operation to proceed further : \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quotient \n6. Remainder")
    choice = int(input("Enter your selection: "))
    if choice == 1:
        print(x, " + ", y, " = ", Add(x, y))

    elif choice == 2:
        print(x, " - ", y, " = ", Subtract(x, y))

    elif choice == 3:
        print(x, " x ", y, " = ", Multiplication(x, y))

    elif choice == 4:
        print(x, " / ", y, " = ", Division(x, y))

    elif choice == 5:
        print(x, " // ", y, " = ", Quotient(x, y))

    elif choice == 6:
        print(x, " % ", y, " = ", Remainder(x, y))

    print("Do you want to play again? (Y/N)")
    ans = input()
 
 
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break