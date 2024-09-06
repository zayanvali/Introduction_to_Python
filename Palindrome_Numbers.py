num = int(input("Please enter a number: "))
num2 = num

#print(num2, num)
pal = 0
while (num > 0):
    digit = num%10
    #print(digit)
    pal = pal*10 + digit
    #print(pal)
    num = num // 10
    #print(digit)

if (num2 == pal):
    print("The number you have entered is a palindrome number.")
else:
    print("The number you have entered is not a palindrome number.")