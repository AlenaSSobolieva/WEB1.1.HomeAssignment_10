# quoteapp/models.py

from mongoengine import Document, StringField, ReferenceField
from django.db import models

class Author(Document):
    name = StringField(max_length=100)
    bio = StringField()

class Quote(Document):
    text = StringField()
    author = ReferenceField(Author)


