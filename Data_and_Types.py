## There are different types of data in python namely Integers, Floats, Strings, Lists, Tuples, Sets, Dictionary, Boolean

# integers
x1 = 137

# floats
x2 = 17.39

# strings
x3 = "Hello there"

# lists -- they are always represented using square brackets
x4 = [137, 17.39, "Hello there", ("temp values", 10.34, 27, True), False, ["Demo list", 147, 98.34, True]]

# Tuples -- they are represented using round brackets
x5 = (137, 17.39, "Hello there", ("temp values", 10.34, 27, True), False, ["Demo list", 147, 98.34, True])

# Boolean -- True or False
x6 = 17 > 21 


print(x6)

# Operators 
# >, <, >=, <=, =, ==, != (not equal)
# = is used as an assignment operetor for assigning values to a variable e.g x = 23, y = "Demo"
# == is used in order to compare two variables, 
# for eg: 
# if x==y :
#     print("Equal") 
# else: 
#     print("Not Equal")


## Type of Data --- Type is the keyword which helps to understand the kind of data we are dealing with

print(type(x1), type(x2), type(x3), type(x4), type(x5), type(x6))

## Write a program to check if you are eligible to vote
# for someone between 0-13, you are a kid, between 13-17 you are a teenager, 18 and above you are eligible to vote

x = int(input("How old are you : "))

if x < 13:
    print("You are not eligible to vote as you are a kid ")

elif 13 <= x < 18:
    print("You are not eligible to vote as you are a teenager ")

else :
    print("You are eligible to vote ")
    
