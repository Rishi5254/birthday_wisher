
import datetime as dt
import random
import smtplib
import pandas

file = pandas.read_csv("birthdays.csv")
data = file.to_dict("records")


birth_day_mem = None

present = dt.datetime.now()
present_month = present.month
present_day = present.day

for n in range(0, len(data)):
    if present_day == data[n]["day"] and present_month == data[n]["month"]:
        birth_day_mem = data[n]

    letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

    with open(random.choice(letters)) as letter:
        letter_matter = letter.read()
        new_letter = letter_matter.replace("[NAME]", birth_day_mem['name'])
    print(new_letter)

    mail = "hii482621@gmail.com"
    password = "Rishi@81818"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(mail, password)
        connection.sendmail(from_addr=mail, to_addrs=birth_day_mem["email"], msg=f"Subject:Happy Birthday\n\n{new_letter}")