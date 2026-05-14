
import random
import smtplib
from datetime import datetime
import pandas

today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")


birthday_data = {(row.month,row.day):row for (index,row) in data.iterrows()}
# { new_key:new_value for (index, row) in dict.iterrows()}


# print(birthday_data[today_tuple]["name"])
# print(birthday_data[today_tuple]["year"])


file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

if today_tuple in birthday_data:
    print(birthday_data[today_tuple]["name"])
    print(birthday_data[today_tuple]["email"])
    # birthday_person = birthday_data[today_tuple]
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_data[today_tuple]["name"])
    my_email = "maiccuzzunottoppe@gmail.com"
    password = "bdqrlnpsacdfwjim"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_data[today_tuple]["email"],
                            msg=f"Subject:Happy Birthday {birthday_data[today_tuple]["name"]} \n\n "
                                f"{content}")







