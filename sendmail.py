# Sending email using SSL Connection
import smtplib, ssl
import getpass

port = 465  # for SSL

smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"  # your email
reciever_email = "reciever@gmail.com"  # recievers email

# for sending to multiple emails create a list like below
# reciever_email = ["reciever1@gmail.com","reciever2@gmail.com"] 

message = """\
Subject: Hi there

This message is sent from Python."""

password = getpass.getpass(prompt='Password: ', stream=None)
# getpass() used to hide typing password in prompt

# creating a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login("sender@gmail.com", password)
    server.sendmail(sender_email, reciever_email, message)

# Server is automatically closed after getting out from with block
