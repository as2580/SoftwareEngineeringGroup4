from django.urls import path

from . import views

app_name = 'item_locator'
urlpatterns = [
    path('', views.index, name='item_locator_url'),
    path('index', views.index, name='item_locator_url'),
    path('search', views.search, name='item_locator_url'),
    path('select', views.select, name='item_locator_url'),
]