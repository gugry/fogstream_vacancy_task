from __future__ import unicode_literals
from django.db import models

class MessageModel(models.Model):
    verbose_name = 'сообщение'
    verbose_name_plural = 'сообщения'
    message_status = models.BooleanField()
    message_text = models.TextField()
    message_email = models.EmailField()
    def __str__(self):
        return self.message_text

