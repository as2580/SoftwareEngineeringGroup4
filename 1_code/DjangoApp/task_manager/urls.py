from django.urls import path

from . import views

app_name = 'task_manager'
urlpatterns = [
    path('', views.index, name='index'),
	path('edit', views.edit, name='edit'),
	path('modify', views.modify, name='modify'),
	path('create', views.create, name='create'),
	path('created', views.created, name='created'),
	path('delete', views.delete, name='delete'),
]