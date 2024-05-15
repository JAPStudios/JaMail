import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import config
class EmailService:
    def __init__(self):
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.smtp_username = config.SMTP_USERNAME
        self.smtp_password = config.SMTP_PASSWORD
        self.encryption_method = config.ENCRYPTION_METHOD
    def send_email(self, recipient, subject, body):
        try:
            smtp = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp.starttls()
            smtp.login(self.smtp_username, self.smtp_password)
            message = MIMEMultipart()
            message['From'] = self.smtp_username
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))
            smtp.sendmail(self.smtp_username, recipient, message.as_string())
            smtp.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
if __name__ == '__main__':
    email_service = EmailService()
    recipient_email = 'recipient@example.com'
    email_subject = 'Test Email'
    email_body = 'This is a test email sent from the EmailService class.'
    result = email_service.send_email(recipient_email, email_subject, email_body)
    if result:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")