from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import MessageForm


def index(request):
    return render(request, 'base_app/home.html', {'message_form': MessageForm})

class RegUser(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST or None)
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return render(request, 'registration/registration.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST or None)
        response = HttpResponse('not Ajax')
        if form.is_valid():
            if request.is_ajax():
                user = form.save()
                login(request, user)
                data = {
                    'result': 'Успешно!',
                }
                response = JsonResponse(data)
        else:
            err_list = []
            for key in form.errors.as_data().keys():
                err_list.append( str(form.errors.as_data()[key][0])[2:-2])
            response = JsonResponse({'result':err_list})
        return response

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

@login_required
def message_for_admin(request, saved=None):
    superuser_email = User.objects.filter(is_superuser=True).values_list('email')
    superusers = User.objects.all()
    print(superusers )
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
