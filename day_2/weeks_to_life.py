# 🚨 Don't change the code below 👇
age = input("What is your current age? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

rem_yrs = (90 - int(age))
rem_days = rem_yrs * 365
rem_wks = rem_yrs * 52
rem_months = rem_yrs * 12

print(f"you have {rem_days} days, {rem_wks} weeks or {rem_months} months left.")
