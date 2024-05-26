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
def print_menu():
    print("""
        ******************************
        * Google Cloud Data Recovery *
        ******************************
        1. Input Google Access Token (Profile Data)
        2. Input Google Access Token (Email Data)
        3. Create Google Access Token (No App Data)
        4. Create Google Access Token (Supplied by App)
        5. Quit
            """)
def main():
    user_response = None
    print_menu()
    choice = input("Type number option you require: ")
    if choice == "1":
        access_token = input("(PROFILE) Enter your Google Access Token: ")
        user_response = query_profile_api(access_token)
    elif choice == "2":
        access_token = input("(EMAIL) Enter your Google Access Token: ")
        query_email_api(access_token)
    elif choice == "3":
        user_request_access_token()
    elif choice == "4":
        generate_access_token()
    elif choice == "5":
        exit()
    else:
        print("\nInvalid choice, try again")
    if user_response is not None:
        write_files(user_response)
    main()
def user_request_access_token():
    """
    Generates an OAuth access token by having the user give access to their account (WARNING: USER PERMISSION REQUIRED)
    """
    client_id = '280174354411-s5ss17k6bb39ql04nf472fjlteh9nqmv.apps.googleusercontent.com'
    client_secret = 'h0gtTSge5BmtHxHOzf83cRdC'
    flow = client.OAuth2WebServerFlow(
        client_id=client_id,
        client_secret=client_secret,
        scope='https://www.googleapis.com/auth/userinfo.profile '
              'https://www.googleapis.com/auth/gmail.readonly',
        redirect_uri='http://localhost:8080')
    storage = Storage('token.data')
    credentials = run_flow(flow, storage)
    print("Access Token: %s" % credentials.access_token)
    print("Refresh Token: %s" % credentials.refresh_token)
    return
def generate_access_token():
    """
    Generates an OAuth access token given a client_id, client_secret and refresh_token stored within an app.
    """
    client_id = input('Input Client ID from App: ')  # Client ID found in the app, linked to Google
    client_secret = input('Input Client Secret from App: ')  # Client Secret found in the app, linked to Google
    refresh_token = input('Input Refresh Token from App: ')
    cred = client.GoogleCredentials(
        access_token=None,
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
        token_expiry=None,
        token_uri='https://accounts.google.com/o/oauth2/token',
        user_agent='Python client library',
        revoke_uri='https://accounts.google.com/o/oauth2/revoke')
    http = cred.authorize(httplib2.Http())
    cred.refresh(http)
    self.gmail_service = build('gmail', 'v1', credentials=cred)
    print("Access Token: %s" % cred.access_token)
    return
def query_email_api(access_token):
    """
    this queries the Gmail Batch API for Gmail messages.
    param access_token: an oauth access token
    return:
    """
    f = open("emaildata.json", "w+")
    f.close()
    def callback(response):
        """
        generic callback function used to deal with the responses from the Batch API.
        """
        with open('emaildata.json', 'a') as outfile:
            json.dump(response, outfile, indent=4, sort_keys=True)
        return
    credentials = google.oauth2.credentials.Credentials(access_token)
    GMAIL = build('gmail', 'v1', credentials=credentials)
    message_ids = GMAIL.users().messages().list(userId='me', ).execute()
    try:
        messages = []
        count = 0
        if 'messages' in message_ids:
            messages.extend(message_ids['messages'])
        while 'nextPageToken' in message_ids:
            page_token = message_ids['nextPageToken']
            message_ids = GMAIL.users().messages().list(userId='me', pageToken=page_token).execute()
            messages.extend(message_ids['messages'])
            count += 1
        message_estimate = count * 100
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
    choice = input("%d Pages of Messages have been found on this account. It is estimated that"
                   "would be %d Messages.\nWould you like to continue? Type Y to Proceed, otherwise type any key: " % (
                       count, message_estimate))
    if choice == "Y":
        message_ids_sorted = ([message_id['id'] for message_id in messages])
        batch = BatchHttpRequest()
        for msg_id in message_ids_sorted:
            batch.add(GMAIL.users().messages().get(userId='me', id=msg_id, format='minimal'), callback=callback)
            batch.execute()
        return
    else:
        return
def query_profile_api(access_token):
    """
    This function queries the Google Profile API for OAuth and returns name and details.
    param access_token: OAuth access token.
    return data: Returns the response from the Profile API and passes it through to the Json file.
    """
    scope = "https://www.googleapis.com/userinfo/v2/me"
    headers = {
        'cache-control': "no-cache",
        'Authorization': 'Bearer ' + access_token
    }
    response = requests.request("GET", scope, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data
def write_files(user_response):
    """
    Writes generic json blobs to disk
    param user_response: Generic json blob
    return:
    """
    with open('data.json', 'w') as outfile:
        json.dump(user_response, outfile, indent=4, sort_keys=True)
    return
if __name__ == '__main__':
    main()