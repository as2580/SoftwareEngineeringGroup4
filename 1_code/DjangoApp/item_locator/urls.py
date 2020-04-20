from django.urls import path

from . import views

app_name = 'item_locator'
urlpatterns = [
    path('', views.index, name='index'),
]