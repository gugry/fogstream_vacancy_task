from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import MessageModel

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['message_text']

class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model =  User
        fields = ("username", "password")

class Reg_form(UserCreationForm):
    class Meta:
        model =  User
        fields = ("username", "password1", "password2")



