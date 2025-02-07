import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_sender = 'myemail@gmai.com'
email_password = os.environ.get('EMAIL_PASSWORD')
email_receiver = 'myemail@gmai.com'

subject = 'Check out my video'
body = '''
Go to YouTube: ''
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Attach file
with open('photo.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())