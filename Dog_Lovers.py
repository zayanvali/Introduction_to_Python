# A kennel shop in your neighbourhood has a self help kiosk to help with the details of different dog breeds.Write a python program to 
# mimic this kiosk.
# A sample run of it can be of the form:-(When run initially)
#Hello Dog Lovers!!
#Select the dog breed to know more about it.
#1. German Shepherd
#2. Bulldog
#3. Poodle
#4. Golden Retriever
#5. Beagle
#Enter the dog of your choice : 1
#(After entering the choice)
#German Shepherd
#They’re intelligent and capable working dogs. Their devotion #and courage are unmatched. And they’re amazingly versatile.
#Hint :Print the menu .
#Ask user for choice
#Depending on choice display details of dog

print("Hello Dog Lovers! Welcome to our Dog Awareness Campaign!")
print("\nSelect the dog breed to know more about it : ")
print("\n1. German Shepherd \n2. Bulldog \n3. Poodle \n4. Golden Retriever \n5. Beagle")

choice = int(input("Enter the dog of your choice : "))
if choice == 1 :
    print("\nYou have selected German Shepherd. \naglingThey’re intelligent and capable working dogs. Their devotion and courage are unmatched. And they’re amazingly versatile.")

elif choice == 2 :
    print("\nYou have selected Bulldog. \nThe Bulldog is a British breed of dog of mastiff type. It may also be known as the English Bulldog or British Bulldog. It is a medium-sized, muscular dog of around 40–55 lb.")

elif choice == 3 :
    print("\nYou have selected Poodle. \nThe Poodle, called the Pudel in German and the Caniche in French, is a breed of water dog. The breed is divided into four varieties based on size, the Standard Poodle, Medium Poodle, Miniature Poodle and Toy Poodle.")

elif choice == 4 :
    print("\nYou have selected Golden Retriever. \nThe Golden Retriever is a Scottish breed of retriever dog of medium size. It is characterised by a gentle and affectionate nature and a striking golden coat.")

elif choice == 5 :
    print("\nYou have selected Beagle. \nThe beagle is a breed of small scent hound, similar in appearance to the much larger foxhound. The beagle was developed primarily for hunting hare, known as beagling.")

else :
    print("Invalid choice.")