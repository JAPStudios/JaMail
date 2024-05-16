import os
import imaplib
import base64
import email
import mysql.connector
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/drive.readonly']
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)
with open('token.json', 'w') as token:
    token.write(creds.to_json())
def import_user_data(user_id):
    try:
        connection = mysql.connector.connect(
            host="Google",
            user="Google",
            password="Google",
            database="Google"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT user_id, username, email, created_at FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            user_data = cursor.fetchone()
            if user_data:
                print("User Data:")
                print(f"User ID: {user_data[0]}")
                print(f"Username: {user_data[1]}")
                print(f"Email: {user_data[2]}")
                print(f"Created At: {user_data[3]}")
            else:
                print(f"No user found with ID: {user_id}")
    except mysql.connector.Error as error:
        print(f"Error connecting to the database: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
user_id_to_import = 123
import_user_data(user_id_to_import)