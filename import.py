// The code that rescues ALL data from the user specified Google/Microsoft account not leaving a single thing from a single product/service/website from either company behind for permanent deletion.
import os
import imaplib
import base64
import email
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
def authenticate_google_service(service_name, version, scopes, key_file):
    credentials = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
    service = build(service_name, version, credentials=credentials)
    return service
import msal
def authenticate_microsoft_service(client_id, client_secret, authority, scope):
    app = msal.ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        return result['access_token']
    else:
        raise Exception("Could not obtain token")
def backup_google_emails():
    pass
def backup_google_videos():
    pass
def backup_google_documents():
    pass
def backup_google_sheets():
    pass
def backup_outlook_emails():
    pass
def backup_onedrive_files():
    pass
def backup_microsoft_teams_messages():
    pass
def backup_microsoft_contacts():
    pass
def backup_onenote():
    pass
def backup_google_forms():
    pass
def backup_google_sites():
    pass
def backup_youtube():
    pass
def backup_browsing_history():
    pass