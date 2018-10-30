from django.urls import path, include
from . import views
from .views import RegUser

app_name = 'base_app'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='username_login'),
    path('message_for_admin/', views.message_for_admin, name='message_for_admin'),
    path('registration/', RegUser.as_view(), name='user_registration'),
]



