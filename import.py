import os
import imaplib
import base64
import email
from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('gmail', 'v1', credentials=credentials)
results = service.users().messages().list(userId='me').execute()
messages = results.get('messages', [])
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    print(f"Message snippet: {msg['snippet']}")
import msal
import requests
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
AUTHORITY = 'https://login.microsoftonline.com/common'
SCOPES = ['https://graph.microsoft.com/.default']
app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
result = app.acquire_token_for_client(scopes=SCOPES)
if 'access_token' in result:
    graph_url = 'https://graph.microsoft.com/v1.0/me/messages'
    headers = {'Authorization': 'Bearer ' + result['access_token']}
    response = requests.get(graph_url, headers=headers)
    emails = response.json().get('value', [])
    
    for email in emails:
        print(f"Email subject: {email['subject']}")
else:
    print(f"Error: {result.get('error_description')}")
from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10).execute()
items = results.get('files', [])
for item in items:
    print(f"File name: {item['name']}, ID: {item['id']}")
from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('docs', 'v1', credentials=credentials)
document_id = 'your_document_id'
document = service.documents().get(documentId=document_id).execute()
print(f"Document title: {document.get('title')}")
from google.oauth2 import service_account
from googleapiclient.discovery import build
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
SERVICE_ACCOUNT_FILE = 'path/to/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('youtube', 'v3', credentials=credentials)
results = service.playlists().list(part='snippet', mine=True).execute()
playlists = results.get('items', [])
for playlist in playlists:
    print(f"Playlist title: {playlist['snippet']['title']}")
import msal
import requests
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
AUTHORITY = 'https://login.microsoftonline.com/common'
SCOPES = ['https://graph.microsoft.com/.default']
app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
result = app.acquire_token_for_client(scopes=SCOPES)
if 'access_token' in result:
    graph_url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    headers = {'Authorization': 'Bearer ' + result['access_token']}
    response = requests.get(graph_url, headers=headers)
    files = response.json().get('value', [])
    
    for file in files:
        print(f"File name: {file['name']}, ID: {file['id']}")
else:
    print(f"Error: {result.get('error_description')}")
if 'access_token' in result:
    graph_url = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks'
    headers = {'Authorization': 'Bearer ' + result['access_token']}
    response = requests.get(graph_url, headers=headers)
    notebooks = response.json().get('value', [])
    
    for notebook in notebooks:
        print(f"Notebook name: {notebook['displayName']}")
else:
    print(f"Error: {result.get('error_description')}")