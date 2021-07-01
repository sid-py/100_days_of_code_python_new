import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = random.choice(names) # Defining the variable name whihc picks random name from the list.
print(f"{name} is going to buy the meal today!") # Printing the name with message.

