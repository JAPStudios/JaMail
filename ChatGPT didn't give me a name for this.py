import smtpd
import asyncore
class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"Received message from: {mailfrom}")
        print(f"To: {rcpttos}")
        print(f"Message data:\n{data}")
server = CustomSMTPServer(('127.0.0.1', 25), None)
asyncore.loop()
# Assuming you are in the root directory of your project
# Create the Python file
touch email_server.py
# Open the file in a text editor and paste the code
# Save and close the file
# Add the file to the Git repository
git add email_server.py
# Commit the changes
git commit -m "Add email server code"
# Push the commit to your GitHub repository
git push origin main
import smtplib
from email.mime.text import MIMEText
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