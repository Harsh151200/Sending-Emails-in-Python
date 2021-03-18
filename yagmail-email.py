import yagmail

receiver = "reciever@gmail.com"
body = "Hello there from Yagmail"
filename = "Projects/Mail/dummy.csv"

yag = yagmail.SMTP("sender@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    attachments=filename,
)