import os
import imaplib
import base64
import email
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
import msal

# Google API configurations
GOOGLE_SCOPES = {
    'gmail': ['https://www.googleapis.com/auth/gmail.readonly'],
    'drive': ['https://www.googleapis.com/auth/drive.readonly'],
    'docs': ['https://www.googleapis.com/auth/documents.readonly'],
    'youtube': ['https://www.googleapis.com/auth/youtube.readonly']
}
GOOGLE_SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'

# Microsoft API configurations
MS_CLIENT_ID = 'your_client_id'
MS_CLIENT_SECRET = 'your_client_secret'
MS_AUTHORITY = 'https://login.microsoftonline.com/common'
MS_SCOPES = ['https://graph.microsoft.com/.default']


# Function to authenticate with Google API
def authenticate_google(service_name):
    scopes = GOOGLE_SCOPES[service_name]
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_SERVICE_ACCOUNT_FILE, scopes=scopes)
    return credentials


# Function to authenticate with Microsoft API
def authenticate_microsoft():
    app = msal.ConfidentialClientApplication(
        MS_CLIENT_ID, authority=MS_AUTHORITY, client_credential=MS_CLIENT_SECRET)
    result = app.acquire_token_for_client(scopes=MS_SCOPES)
    if 'access_token' in result:
        return result['access_token']
    else:
        print(f"Error: {result.get('error_description')}")
        return None


# Function to fetch emails from Gmail
def fetch_gmail_emails():
    credentials = authenticate_google('gmail')
    service = build('gmail', 'v1', credentials=credentials)
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        print(f"Message snippet: {msg['snippet']}")


# Function to fetch emails from Microsoft
def fetch_microsoft_emails():
    token = authenticate_microsoft()
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('https://graph.microsoft.com/v1.0/me/messages', headers=headers)
        emails = response.json().get('value', [])
        for email in emails:
            print(f"Email subject: {email['subject']}")


# Function to fetch files from Google Drive
def fetch_google_drive_files():
    credentials = authenticate_google('drive')
    service = build('drive', 'v3', credentials=credentials)
    results = service.files().list(pageSize=10).execute()
    items = results.get('files', [])
    for item in items:
        print(f"File name: {item['name']}, ID: {item['id']}")


# Function to fetch Google Docs document
def fetch_google_docs_document(document_id):
    credentials = authenticate_google('docs')
    service = build('docs', 'v1', credentials=credentials)
    document = service.documents().get(documentId=document_id).execute()
    print(f"Document title: {document.get('title')}")


# Function to fetch YouTube playlists
def fetch_youtube_playlists():
    credentials = authenticate_google('youtube')
    service = build('youtube', 'v3', credentials=credentials)
    results = service.playlists().list(part='snippet', mine=True).execute()
    playlists = results.get('items', [])
    for playlist in playlists:
        print(f"Playlist title: {playlist['snippet']['title']}")


# Function to fetch files from Microsoft OneDrive
def fetch_microsoft_drive_files():
    token = authenticate_microsoft()
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers)
        files = response.json().get('value', [])
        for file in files:
            print(f"File name: {file['name']}, ID: {file['id']}")


# Function to fetch Microsoft OneNote notebooks
def fetch_microsoft_onenote_notebooks():
    token = authenticate_microsoft()
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get('https://graph.microsoft.com/v1.0/me/onenote/notebooks', headers=headers)
        notebooks = response.json().get('value', [])
        for notebook in notebooks:
            print(f"Notebook name: {notebook['displayName']}")


if __name__ == "__main__":
    # Call the functions to fetch data
    fetch_gmail_emails()
    fetch_microsoft_emails()
    fetch_google_drive_files()
    fetch_google_docs_document('your_document_id')
    fetch_youtube_playlists()
    fetch_microsoft_drive_files()
    fetch_microsoft_onenote_notebooks()