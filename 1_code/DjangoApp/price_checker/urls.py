from django.urls import path

from . import views

app_name = 'price_checker'
urlpatterns = [
    path('', views.index, name='index'),
]