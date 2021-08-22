##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "progc515@gmail.com"
MY_PASS = "pyThon1986$$"


birthdays = pd.read_csv(r"day_32\birthday\birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")

birthday_today = dt.datetime.now()


for entry in birthday_dict:
    birthday_message = (f"Happy Birthday!{entry['name']}")
    print(entry["month"])
    if birthday_today.month == entry["month"]:
        print(f"Yes! Happy Birthday {entry['name']}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASS)
            connection.sendmail(from_addr = MY_EMAIL, to_addrs = entry["email"], msg = f"Subject: Birthday Message!\n\n{birthday_message}")


