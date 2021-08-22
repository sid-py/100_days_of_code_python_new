##################### Extra Hard Starting Project ######################

import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "progc515@gmail.com"
MY_PASS = "pyThon1986$$"

# 1. Update the birthdays.csv
birthdays = pd.read_csv(r"day_32\birthday\birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")

birthday_today = dt.datetime.now()
num = random.randint(1,3)

for entry in birthday_dict:
    # 2. Check if today matches a birthday in the birthdays.csv
    if birthday_today.month == entry["month"] and birthday_today.day == entry["day"]:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(fr"day_32\birthday\letter_templates\letter_{num}.txt") as letter:
            content = letter.read()
            content = content.replace("[NAME]", entry["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASS)
            connection.sendmail(from_addr = MY_EMAIL, to_addrs = entry["email"], msg = content)
            print(f"Birthday wish successfuly sent to {entry['name']}!")


