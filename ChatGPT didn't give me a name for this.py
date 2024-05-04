pip install google-cloud-sql
pip install google-cloud-firestore
import imaplib
import email
import your_database_module
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
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
    your_database_module.save_email(sender, subject, body)
mail.close()
mail.logout()
print('Emails imported successfully.')