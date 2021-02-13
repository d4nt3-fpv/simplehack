import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = "klasse09c@web.de"
EMAIL_PASSWORD = "!Bw2005?"

contacts = ['klasse09c@web.de', 'klasse09c@web.de']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'klasse09c@web.de'

msg.set_content('This is a plain text email')

with open("img.jpg", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
    
msg.add_attachment(file_data,  maintype='image', subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL('smtp.web.de', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)