from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth import  login
from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'base_app/home.html', {'message_form': MessageForm})

def reg_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        if request.is_ajax():
            user = form.save()
            login(request, user)
            data = {
                'result': 'Успешно!',
            }
            return JsonResponse(data)
        else:
            return HttpResponse('not Ajax')
    if request.is_ajax():
        return JsonResponse(form.errors, status=400)
    return render(request, 'registration/registration.html', {'form': form})


def reg_passwords_validate(request):
    password_1 = request.GET.get('password1', None)
    password_2 = request.GET.get('password2', None)
    data = {
        'equal': password_1 == password_2,
        'not_equal': password_1 != password_2,
             }
    if data['not_equal']:
        data['error_message'] = 'Пароли не совпадают.'
    if data['equal']:
        data['error_message'] = ''
    return JsonResponse(data)


def reg_username_validate(request):
    username = request.GET.get('username', None)
    data = {'is_taken': User.objects.filter(username__iexact=username).exists(),
            'is_free': not User.objects.filter(username__iexact=username).exists()}

    if data['is_taken']:
        data['error_message'] = 'В системе уже есть пользователь с таким иминем.'
    if data['is_free']:
        data['error_message'] = ''
    return JsonResponse(data)


def username_login(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    users = User.objects.filter(username__iexact=username)
    if len(users) > 0:
        user = users[0]
        login(request, user)
        data = {'is_correct': User.check_password(user,password)}
    else:
        data = {'is_correct': False }

    return JsonResponse(data)


def message_for_admin(request, saved=None):
    superuser_email = User.objects.filter(is_superuser=True).values_list('email')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            mail = EmailMessage('Сообщение с сайта', new_message.message_text, '',
                settings.ADMINS, [''],
                reply_to=[superuser_email],
            )
            try:
                new_message.message_status = mail.send()
                context = {'result': 'Письмо отправлено'}
            except BaseException as err:
                print(err)
                new_message.message_status = 0
                context = {'result': "Проблемы при отправке"}

            new_message.save()
            return JsonResponse(context)
    else:
        form = MessageForm()
    return render(request, 'message/message.html', {'form': form})
