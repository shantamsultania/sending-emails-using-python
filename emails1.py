import os
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = 'shantam12300@gmail.com'
EMAIL_PASSWORD = 'Shantam@12'

msg = EmailMessage()

msg['Subject'] = 'subject'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'shantam12300@gmail.com'
msg.set_content('how abdkadakdhakdadajkdakdakadkhdhak h kjhakjkd')

files = ['c1.jpg']

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