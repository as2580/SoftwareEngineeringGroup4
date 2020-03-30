from django.urls import path

from . import views

app_name = 'check_out'
urlpatterns = [
    path('', views.index, name='index'),
]