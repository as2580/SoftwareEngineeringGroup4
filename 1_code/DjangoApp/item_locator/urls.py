from django.urls import path

from . import views

app_name = 'item_locator'
urlpatterns = [
    path('', views.home_index, name='customer_terminal_url'),
    path('home_index', views.home_index, name='customer_terminal_url'),
    path('il_index', views.il_index, name='item_locator_url'),
    path('search', views.search, name='item_locator_url'),
    path('select', views.select, name='item_locator_url'),
    path('pc_index', views.pc_index, name='price_checker_url'),
    path('search_rfid', views.search_rfid, name='price_checker_url'),
]