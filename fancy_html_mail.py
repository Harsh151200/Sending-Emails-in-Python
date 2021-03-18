import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

port = 465 #for SSL

smtp_server = "smtp.gmail.com" 
sender_email =  "sender@gmail.com" #your email
reciever_email = "reciever@gmail.com" #recievers email

password = getpass.getpass(prompt='Password: ', stream=None)
#getpass() used to hide typing password in prompt

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["To"] = sender_email
message["From"] = reciever_email

#Creating a plain text and html verison of context
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.google.com">Google</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

#Turing this plain and html messages into MIMEText objects
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

# Adding the HTML/plain-text parts -> MIMEMultipart message
# The email client will first try to render the last part
message.attach(part1)
message.attach(part2)

#creating a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.login("sender@gmail.com",password)
    server.sendmail(sender_email,reciever_email,message.as_string())

# Server is automatically closed after getting out from with block