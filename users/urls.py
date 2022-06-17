from django.urls import path,include
from . import views

app_name = 'users'
urlpatterns = [
    #URL авторизация
    path('', include('django.contrib.auth.urls')),
    # страница регистрации
    path('register/', views.register, name='register'),
]