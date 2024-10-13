import ssl
from email.message import EmailMessage
import smtplib
from credentials import password

sender = "awrash.sn@gmail.com"
receiver = "yasnaghavami18@gmail.com"
subject = 'Testing Email Module'

body = """
I'm testing gmail automation with email module in python!
"""

email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject

email.set_content(body)

# Add file attachment
with open('HTTP.pdf', 'rb') as file:
    email.add_attachment(file.read(), maintype='pdf', subtype='pdf', filename=file.name)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    print("Sending email to", receiver)
    smtp.login(sender, password)
    smtp.send_message(email)
    print("Sent!")
