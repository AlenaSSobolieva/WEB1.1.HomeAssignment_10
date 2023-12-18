# quoteapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('quote_list/', views.quote_list, name='quote_list'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]
