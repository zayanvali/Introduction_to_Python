import random
x1 = int(input("Enter the starting range : "))
x2 = int(input("Enter the ending range : "))
x3 = random.randrange(x1, x2)
print("Program selected random number is : ", x3)
guess = int(input("Enter your guess : "))

while guess != x3:
    if guess < x3 :
        print("Your guess is lower than my number ")
        guess = int(input("Enter number again : "))
    elif guess > x3 : 
        print("Your guess is higher than my number ")
        guess = int(input("Enter number again : "))    
    else :
        break
print("You have guessed the right number")