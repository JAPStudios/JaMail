import imaplib
import email
def extract_email_data(email_data):
    mail = email.message_from_bytes(email_data[0][1])
    subject = mail['Subject']
    sender = mail['From']
    body = ""
    if mail.is_multipart():
        for part in mail.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_payload(decode=True).decode()
    else:
        body = mail.get_payload(decode=True).decode()
    return {
        'subject': subject,
        'sender': sender,
        'body': body
    }
mail = imaplib.IMAP4_SSL('imap.example.com')
mail.login('username', 'password')
mail.select('inbox')
typ, data = mail.search(None, 'ALL')
for num in data[0].split():
    typ, email_data = mail.fetch(num, '(RFC822)')
    if email_data:
        extracted_data = extract_email_data(email_data)
        print(extracted_data)
mail.close()
mail.logout()