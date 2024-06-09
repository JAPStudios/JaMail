import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings
def google_auth(request): redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri=http://localhost:8000/core/google/callback&scope=openid email profile&response_type=code")
def google_callback(request):
    code = request.GET.get('code')
    data = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': 'http://localhost:8000/core/google/callback',
        'grant_type': 'authorization_code'
    }
    response = requests.post('https://oauth2.googleapis.com/token', data=data)
    tokens = response.json()
    user_info_response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', params={'access_token': tokens['access_token']})
    user_info = user_info_response.json()
    return JsonResponse(user_info)
def microsoft_auth(request):
    return redirect(f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={settings.MICROSOFT_CLIENT_ID}&response_type=code&redirect_uri=http://localhost:8000/core/microsoft/callback&response_mode=query&scope=User.Read")
def microsoft_callback(request):
    code = request.GET.get('code')
    data = {
        'code': code,
        'client_id': settings.MICROSOFT_CLIENT_ID,
        'client_secret': settings.MICROSOFT_CLIENT_SECRET,
        'redirect_uri': 'http://localhost:8000/core/microsoft/callback',
        'grant_type': 'authorization_code'
    }
    response = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data)
    tokens = response.json()
    user_info_response = requests.get('https://graph.microsoft.com/v1.0/me', headers={'Authorization': f"Bearer {tokens['access_token']}"})
    user_info = user_info_response.json()
    return JsonResponse(user_info)