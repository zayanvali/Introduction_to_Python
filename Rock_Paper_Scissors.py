import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
 
while True:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")

    choice = int(input("User turn : "))
    while choice > 3 or choice < 1 : 
        choice = int(input("Enter Valid Input: "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......") 


    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print("computer choice is: " + comp_choice_name)
    print(choice_name + " v/s " + comp_choice_name)

    # condition for winning
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "Paper"

    
    elif((choice == 1 and comp_choice == 3) or
      (choice == 3 and comp_choice ==1 )):
        print("rock wins => ", end = "")
        result = "Rock"

    else:
        print("scissor wins => ", end = "")
        result = "Scissor"

    # Printing either user or computer wins
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
         
    print("Do you want to play again? (Y/N)")
    ans = input()
 
 
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
     
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")