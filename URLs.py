from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
]
from django.urls import path
from .views import google_auth, google_callback, microsoft_auth, microsoft_callback
urlpatterns = [
    path('auth/google/', google_auth, name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),
    path('auth/microsoft/', microsoft_auth, name='microsoft_auth'),
    path('microsoft/callback/', microsoft_callback, name='microsoft_callback'),
]