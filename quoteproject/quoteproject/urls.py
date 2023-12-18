# quoteproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Add include import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quoteapp.urls')),  # Include your app's URLs
]
