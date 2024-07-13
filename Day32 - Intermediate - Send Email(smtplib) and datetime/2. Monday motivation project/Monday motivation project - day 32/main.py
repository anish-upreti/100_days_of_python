#Monday Motivation Quote Project
import smtplib
import datetime as dt
import random

my_email = "_your_email_"  # use your own email
my_password = "_password_" # use your own password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:         # weekday 0 for monday, 1 for tuesday, 2 for wednesday and so on.
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        quote = random.choice(quote_list)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="for.test1111@yahoo.com",
            msg=f"Subject:Monday Motivation Quote \n\n{quote}"
        )


# # Sending Email with Python
# import smtplib
#
# my_email = "for.test.code.0725@gmail.com"
# password = "mgmyuososeazukgu"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="for.test1111@yahoo.com",
#                     msg="Subject:Test\n\nThis is the test mail.")
# connection.close()


# # Working with date and time in Python
# import datetime as dt
#
# date_time = dt.datetime.now()
# year = date_time.year
# month = date_time.month
# day_of_week = date_time.weekday()
# print(date_time)
# print(year)
# print(month)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2000, month=1, day=1)
# print(date_of_birth)

