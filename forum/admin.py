from django.contrib import admin
from .models import Publication, Comment, Like, Message

admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Message)