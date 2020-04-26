from django.urls import path

from . import views

app_name = 'shopping_list'
urlpatterns = [
    path('', views.index, name='index'),
	path('search', views.search, name='search'),
]