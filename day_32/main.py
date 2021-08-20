from email import message
import random
import datetime as dt
import smtplib



with open(r"day_32\quotes.txt", "r") as file:
    quotes = file.readlines()
    # Removing whitespace characters like \n at the end of each line
    quotes = [x.strip() for x in quotes] 
# print(quotes)

# quote_trigger_day = 

quote_message = random.choice(quotes)
print(quote_message)

now = dt.datetime.now()

today = now.weekday()

email = "progc515@gmail.com"
password = "pyThon1986$$"


if today == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email, to_addrs = "siddhesh.sule47@gmail.com", msg = f"Subject: Quote of the Day!\n\n{quote_message}")