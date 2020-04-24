from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.register, name='register'),
    path('', views.success, name='success'),
    path('', views.login, name='login'),
]
