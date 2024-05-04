pip install imaplib
user_email = 'your_email@gmail.com'
user_password = 'your_password'
python email_importer.py
git add email_importer.py
git commit -m "Update email_importer.py with new credentials"
git push origin main
git add email_importer.py
git commit -m "Update email_importer.py with Gmail import functionality"
python email_importer.py
import imaplib
import email
def import_emails_from_gmail(user_email, user_password):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(user_email, user_password)
        mail.select('inbox')
        status, data = mail.search(None, 'ALL')
        if status == 'OK':
            for num in data[0].split():
                status, email_data = mail.fetch(num, '(RFC822)')
                if status == 'OK':
                    raw_email = email_data[0][1]
                    email_message = email.message_from_bytes(raw_email)
                    
                    sender = email_message['From']
                    subject = email_message['Subject']
                    
                    if email_message.is_multipart():
                        for part in email_message.get_payload():
                            if part.get_content_type() == 'text/plain':
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = email_message.get_payload(decode=True).decode()
                    print(f"Sender: {sender}")
                    print(f"Subject: {subject}")
                    print(f"Body: {body}")
            mail.close()
            mail.logout()
            print('Emails imported successfully from Gmail.')
    except Exception as e:
        print(f'Error importing emails from Gmail: {e}')
def import_emails_from_hotmail(user_email, user_password):
    pass
def import_emails_from_yahoo(user_email, user_password):
    pass
def import_emails_from_outlook(user_email, access_token):
    pass
def import_emails_from_service(service_name, user_email, user_password, access_token=None):
    if service_name.lower() == 'gmail':
        import_emails_from_gmail(user_email, user_password)
    elif service_name.lower() == 'hotmail':
        import_emails_from_hotmail(user_email, user_password)
    elif service_name.lower() == 'yahoo':
        import_emails_from_yahoo(user_email, user_password)
    elif service_name.lower() == 'outlook':
        import_emails_from_outlook(user_email, access_token)
    else:
        print(f"Service '{service_name}' is not supported.")
chosen_service = 'Gmail'
user_email = 'your_email@gmail.com'
user_password = 'your_password'
access_token = 'your_oauth_access_token'
import_emails_from_service(chosen_service, user_email, user_password, access_token)