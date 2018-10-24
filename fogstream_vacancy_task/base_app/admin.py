from __future__ import unicode_literals
from django.contrib import admin
from .models import MessageModel


class MessageAdmin(admin.ModelAdmin):
    fields = ['message_text', 'message_status']
    list_display = ('message_text', 'message_status')
admin.site.register(MessageModel,MessageAdmin)