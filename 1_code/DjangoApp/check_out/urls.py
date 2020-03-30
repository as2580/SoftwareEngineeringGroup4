from django.urls import path

from . import views

app_name = 'check_out'
urlpatterns = [
    path('', views.index, name='index'),
    path('Finish', views.finish, name='finish'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('add_items', views.add_items, name='add_items')
]