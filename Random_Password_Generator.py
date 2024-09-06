import random

letters_lower = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", 
                "v" "b", "n", "m"] 
letters_upper = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", 
                "V", "B", "N", "M"]

numbers1 = random.randint(1, 100)
numbers2 = random.randint(1, 100)
special_characters = ["!", "£", "$", "%", "^", "&", "*", "()"]

a = random.choice(letters_lower)
b = random.choice(letters_upper)
c = random.choice(special_characters)
d = random.choice(letters_lower)
e = random.choice(letters_upper)

print("A good password for you to consider is : {}{}{}{}{}{}{}".format(b, a, c, numbers1, d, numbers2, e))



# Homework Question:
# Write a program to build a school curriculum, consisting of subjects, languages, sports and year
# Hint : Use random library, and pick 10 items for languages, 10 items for sports and 10 items for subjects
