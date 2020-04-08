import os
import smtplib
from email.message import EmailMessage
import imghdr

# you just have to enter these Credentials nothing else
EMAIL_ADDRESS = 'you_email_address'
EMAIL_PASSWORD = 'your_email_password'

msg = EmailMessage()

msg['Subject'] = 'Your_own_subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'Your_mail_id'
msg.set_content('Your_Email_body')

files = ['Image_name_with.extension']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('mail sent')