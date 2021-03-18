import csv, smtplib, ssl,getpass

port = 465 #for SSL
smtp_server = "smtp.gmail.com" #using gmail smtp server

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "hp4911497@gmail.com"
password = getpass.getpass(prompt='Password: ', stream=None)

"""
Note: csv file consists of dummy emails.
So kindly replace with the mails you prefer or want to send mails to

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login("hp4911497@gmail.com",password)
    with open("Projects/Mail/dummy.csv") as file:
        reader = csv.reader(file)
        next(reader) #skipping next row
        for name,email,grade in reader:
            print(f"Sending mail to {name}... ")
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )
