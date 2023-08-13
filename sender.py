# created by devil0crew
import sys
import smtplib
from termcolor import colored, cprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
smtp_host = 'host.com'
smtp_port = 25
smtp_username = 'Username'
smtp_password = 'Password'

# Email content
subject = 'Email sender by devil'
body = 'Your message'

# Email list
email_list = ['email1@google.com', 'email2@google.com']

# Create a message object
message = MIMEMultipart()
message['From'] = smtp_username
message['Subject'] = subject

# Attach the message body
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
smtp_server = smtplib.SMTP(smtp_host, smtp_port)
smtp_server.starttls()
smtp_server.login(smtp_username, smtp_password)

# Send emails to the list of recipients
for email in email_list:
    message['To'] = email
    smtp_server.sendmail(smtp_username, email, message.as_string())

# Close the SMTP server connection
smtp_server.quit()
text = colored('Done! by devil', 'green')
print(text)
