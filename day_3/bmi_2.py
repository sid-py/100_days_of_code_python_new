# 🚨 Don't change the code below 👇

message = input("Do you know your height in meters?:\n")

if message.upper() == "Y" or message.upper() == "YES":
    height = float(input("Enter your height in meters: \n"))
else:
    height_ft = float(input("Enter your height in ft.inches: \n"))
    height = height_ft * 0.3048
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


