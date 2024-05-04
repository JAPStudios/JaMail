import imaplib
import email
from google.cloud import sql
def import_emails_from_service(service_name, user_email, user_password):
    if service_name.lower() == 'gmail':
        IMAP_SERVER = 'imap.gmail.com'
        IMAP_PORT = 993
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(user_email, user_password)
        mail.select('inbox')
    try:
        status, data = mail.search(None, 'ALL')
        for num in data[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            sender = email_message['From']
            subject = email_message['Subject']
            body = ""
            if email_message.is_multipart():
                for part in email_message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = email_message.get_payload(decode=True).decode()
            with sql.connect() as connection:
                query = "INSERT INTO emails (sender, subject, body) VALUES (%s, %s, %s)"
                values = (sender, subject, body)
                connection.execute(query, values)
        print('Emails imported successfully.')
    except Exception as e:
        print(f'Error importing emails: {e}')
    finally:
        mail.close()
        mail.logout()
user_email = 'your_email@gmail.com'
user_password = 'your_password'
selected_service = 'Gmail'
import_emails_from_service(selected_service, user_email, user_password)