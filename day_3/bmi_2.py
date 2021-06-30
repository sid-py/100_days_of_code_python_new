# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/height**2

print(bmi)

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weigth.")
elif 25 <= bmi < 30:
    print("You are slightly overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")


