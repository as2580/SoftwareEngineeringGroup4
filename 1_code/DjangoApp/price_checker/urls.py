from django.urls import path

from . import views

app_name = 'price_checker'
urlpatterns = [
    path('', views.index, name='price_checker_url'),
    path('index', views.index, name='price_checker_url'),
    path('search_rfid', views.search_rfid, name='price_checker_url'),
]