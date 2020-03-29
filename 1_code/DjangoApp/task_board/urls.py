from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('claim_tasks', views.edit, name='claim_tasks'),
	path('view_tasks', views.modify, name='view_tasks'),
]