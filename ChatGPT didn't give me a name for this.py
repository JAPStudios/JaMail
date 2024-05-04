from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
def import_emails_from_gmail(user_credentials, labels_to_import):
    service = build('gmail', 'v1', credentials=user_credentials)
    messages = []
    for label in labels_to_import:
        response = service.users().messages().list(userId='me', labelIds=[label]).execute()
        if 'messages' in response:
            messages.extend(response['messages'])
    extracted_emails = []
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        sender = next(h['value'] for h in msg['payload']['headers'] if h['name'] == 'From')
        subject = msg['payload']['headers'][22]['value']
        body = msg['snippet']
        extracted_emails.append({'sender': sender, 'subject': subject, 'body': body})
    return extracted_emails
user_credentials = Credentials(token='user_access_token', refresh_token='user_refresh_token', token_uri='https://accounts.google.com/o/oauth2/token', client_id='your_client_id', client_secret='your_client_secret', scopes=['https://www.googleapis.com/auth/gmail.readonly'])
labels_to_import = ['INBOX', 'SENT']
emails_to_import = import_emails_from_gmail(user_credentials, labels_to_import)
for email_data in emails_to_import:
    your_database_module.save_email(email_data['sender'], email_data['subject'], email_data['body'])
print('Emails imported successfully.')
import imaplib
import email
from google.cloud import sql
project_id = 'your_project_id'
instance_id = 'your_instance_id'
database_name = 'your_database_name'
client = sql.Client(project=project_id)
instance = client.instance(instance_id)
database = instance.database(database_name)
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
    with database.connect() as connection:
        query = "INSERT INTO emails (sender, subject, body) VALUES (%s, %s, %s)"
        values = (sender, subject, body)
        connection.execute(query, values)
mail.close()
mail.logout()
print('Emails imported successfully.')