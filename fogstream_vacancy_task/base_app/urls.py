from django.urls import path, include
from django.conf.urls import  url
from . import views
from django.views.generic.base import TemplateView

app_name = 'base_app'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='username_login'),
    path('login/username_login/', views.username_login, name='username_login'),
    path('message_for_admin/', views.message_for_admin, name='message_for_admin'),
    path('registration/', views.reg_user, name='user_registration'),
    path('registration/reg_username_validate/', views.reg_username_validate,
         name='reg_username_validate    '),
    path('registration/reg_passwords_validate/', views.reg_passwords_validate,
         name='reg_passwords_validate'),
]



