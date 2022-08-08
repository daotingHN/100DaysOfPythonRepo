# ------------------- Sending Emails ------------------- #

# import smtplib
#
# my_email = "darrenadrianting@yahoo.com"
# password = "glnwvgkhrnsfxldx"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, passowrd=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="darrenadrianting@gmail.com",
#         msg="Subject:Hello\n\n This is the body."
#     )


# ------------------- Using Datetime ------------------- #
# import datetime as dt
#
# # Current Date & Time (object)
# now = dt.datetime.now()
#
# # Current Year/Month/Day/Hour (int)
# year = now.year
# month = now.month
# day = now.day
# weekday = now.weekday()  # starts from 0 (which is Monday)
# hour = now.hour
# print(weekday)
#
# date_of_birth = dt.datetime(year=2000, month=7, day=24, hour=16)
# print(date_of_birth)


# ------------------- Challenge 1 ------------------- #
import smtplib
import datetime as dt
import random

MY_EMAIL = "darrenadrianting@yahoo.com"
PASSWORD = "glnwvgkhrnsfxldx"

# ---- Datetime ---- #
# now = dt.datetime.now()
now = dt.datetime(year=2021, month=10, day=11)
weekday = now.weekday()

# ---- Access Quotes ---- #
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # print(quote)

# ---- Send Email ---- #
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, passowrd=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Quote of the Week\n\n{quote}"
        )
