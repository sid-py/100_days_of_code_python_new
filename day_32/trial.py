# from email import message
# import smtplib

# my_email = "progc515@gmail.com"
# password = "pyThon1986$$"
# message = "Subject: Business Proposition \n\nHello There! I have a business proposal for you!"


# #### ----------------Method with "close()" requirement--------------####
# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.starttls()
# # connection.login(user = my_email, password = password)
# # connection.sendmail(from_addr=my_email, to_addrs="siddhesh.sule47@gmail.com", msg = message)
# # connection.close()


# #### ----------------Method WITHOUT any need to close the connection--------------####

# # count = 5

# # while count > 0:
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = my_email, password = password)
#     connection.sendmail(from_addr=my_email, to_addrs="siddhesh.sule47@gmail.com", msg = message)
#     # count -= 1
    
    
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
# dst = now.dst
week_day = now.weekday()
hour = now.hour
time = now.time()
dob = dt.datetime(year=1986, month=4, day=30)
print(time)

# print(now, year, month, day, dst, hour)
