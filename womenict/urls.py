# project_name/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coreapp.urls')),  # Include app's URLs
    # Define other URL patterns as needed
]
