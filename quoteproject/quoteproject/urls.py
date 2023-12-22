# quoteproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Import the include function

urlpatterns = [
    path("admin/", admin.site.urls),
    path('quoteapp/', include('quoteapp.urls')),  # Include the quoteapp URLs
    # Add other URL patterns as needed
]
