import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='Pdf Mail Demo'
msg['From']='Priyanshi Tiwari'
msg['To']='riyatiwari727@gmail.com'

with open('Emailtemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('priyanshivyas2@gmail.com','Priyanshi727$')
    server.send_message(msg)

print("Message sent!")


