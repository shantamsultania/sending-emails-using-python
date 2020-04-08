import smtplib

# enable allow less know application in your google account then enter your email address here and the emails you
# want to sen email to in TO and the subject you want and other data

gmail_user = "enter your mail here"
gmail_pwd = "enter your password here"
TO = ['enter email 1', 'email 2 if any ','and so on']
SUBJECT = "Testing"
TEXT = "Testing...... sending mail using Gmail with the help of python..."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
for i in range(len(TO)):
    BODY = '\r\n'.join(['To: %s' % TO[i],
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    server.sendmail(gmail_user, [TO[i]], BODY)
    print('email sent to '+ str(TO[i]))

server.close()