# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

# Counting TRUE score
t = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
te = name1_lower.count("e") + name2_lower.count("e")

# Counting LOVE score
l = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")
le = name1_lower.count("e") + name2_lower.count("e")

score_TRUE = t + r + u + te
score_LOVE = l + o + v + le

score = int(str(score_TRUE) + str(score_LOVE)) # String concatenation and int conversion

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")