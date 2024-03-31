import smtpd
import asyncore
import smtplib
from email.mime.text import MIMEText
class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Received message from: {mailfrom}")
        print(f"To: {rcpttos}")
        print(f"Message data:\n{data}")
server = CustomSMTPServer(('127.0.0.1', 25), None)
asyncore.loop()
# Set up SMTP server details
smtp_server = 'your_smtp_server'
smtp_port = 587  # Example port, adjust as needed
smtp_username = 'your_username'
smtp_password = 'your_password'
# Set up email content
sender = 'your_email@example.com'
recipient = 'recipient_email@example.com'
subject = 'Test Email'
body = 'This is a test email.'
# Create MIMEText object
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient
# Connect to SMTP server and send email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
    print('Email sent successfully.')
except Exception as e:
    print(f'An error occurred: {e}')