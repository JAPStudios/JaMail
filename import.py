// The code that rescues ALL data from the user specified Google/Microsoft account upon them clicking the icon of either company that they wish to target when importing within the Jmail application not leaving a single thing from a single product/service/website from either company behind for permanent deletion.
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import microsoft.graph
from datetime import datetime
import httplib2
import requests
import self as self
import simplejson as json
import google.oauth2.credentials
from googleapiclient import errors
from oauth2client import client
from oauth2client.tools import run_flow
from oauth2client.file import Storage
from googleapiclient.discovery import build
from googleapiclient.http import BatchHttpRequest
GOOGLE_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
                 'https://www.googleapis.com/auth/drive.metadata.readonly',
                 'https://www.googleapis.com/auth/contacts.readonly',
                 'https://www.googleapis.com/auth/webhistory',
                 'https://www.googleapis.com/auth/calendar.readonly']
def authenticate_google():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'google_client_secret.json', GOOGLE_SCOPES)
    flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
    auth_url, _ = flow.authorization_url(prompt='consent')
    print('Please go to this URL and authorize access:', auth_url)
    auth_code = input('Enter the authorization code: ')
    flow.fetch_token(code=auth_code)
    credentials = flow.credentials
    return credentials
def retrieve_google_data(credentials):
    gmail_service = googleapiclient.discovery.build('gmail', 'v1', credentials=credentials)
    emails = gmail_service.users().messages().list(userId='me').execute()
    
    drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)
    files = drive_service.files().list().execute()
    
    contacts = googleapiclient.discovery.build('people', 'v1', credentials=credentials).people().connections().list(resourceName='people/me', personFields='names,emailAddresses').execute()
    
    search_history = googleapiclient.discovery.build('customsearch', 'v1', credentials=credentials).cse().list().execute()
    
    calendar_service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    events = calendar_service.events().list(calendarId='primary').execute()
    
    return emails, files, contacts, search_history, events
MS_SCOPES = ['user.read', 'mail.read', 'files.read.all', 'contacts.read', 'calendars.read', 'user.readbasic.all']
def authenticate_microsoft():
    app = msal.ConfidentialClientApplication('your_client_id', authority='https://login.microsoftonline.com/your_tenant_id', client_credential='your_client_secret')
    result = app.acquire_token_for_client(scopes=MS_SCOPES)
    if 'access_token' in result:
        return result['access_token']
    else:
        print(result.get('error'))
        print(result.get('error_description'))
        return None
def retrieve_microsoft_data(access_token):
    graph_client = microsoft.graph.GraphServiceClient('https://graph.microsoft.com/v1.0', token=access_token)
    emails = graph_client.me.messages.get()
    files = graph_client.me.drive.root.children.request().get()
    contacts = graph_client.me.contacts.get()
    events = graph_client.me.events.get()
    
    return emails, files, contacts, events
def rescue_data():
    google_credentials = authenticate_google()
    google_emails, google_files, google_contacts, google_search_history, google_events = retrieve_google_data(google_credentials)
    microsoft_access_token = authenticate_microsoft()
    microsoft_emails, microsoft_files, microsoft_contacts, microsoft_events = retrieve_microsoft_data(microsoft_access_token)
rescue_data()