import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
list_length = len(names)
random_int = random.randint(0, list_length-1)
print (names[random_int] + " is going to buy the meal today!")