import requests
def fetch_google_data(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://www.googleapis.com/drive/v2/files', headers=headers)
    return response.json()
def fetch_microsoft_data(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers)
    return response.json()