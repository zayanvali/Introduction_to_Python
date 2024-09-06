import random

subjects = ["maths", "english", "science", "geography", "history", "RE", "PE", "art", "music", "computer science"]
languages = ["english", "french", "spanish", "german", "italian", "russian", "arabic", "japanese", "chinese", "vietnamese"]
sports = ["football", "basketball", "tennis", "rugby", "hockey", "volleyball", "badminton", "swimming", "cricket", "golf"]
year = ["2024"]

a = random.choice(subjects)
b = random.choice(subjects)
c = random.choice(subjects)
d = random.choice(subjects)


number1 = random.choice(languages)
number2 = random.choice(languages)


e = random.choice(sports)
f = random.choice(sports)


print("A good school curriculum for you is : \n {} {} {} {} {} {} {} {}".format(year, a, number1, e, b, number2, f, c, d, ))