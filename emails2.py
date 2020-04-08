import os
import smtplib
from email.message import EmailMessage
import imghdr

# you just have to enter these Credentials nothing else t
EMAIL_ADDRESS = 'you_email_address'
EMAIL_PASSWORD = 'your_email_password'

msg = EmailMessage()

msg['Subject'] = 'Your_own_subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'Your_mail_id'
msg.set_content('Your_Email_body')

files = ['New Microsoft Office Word Document.docx']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('mail sent')