## Written by: Andrew Saengtawesin and Kimberly Chang
## Tested by: Andrew Saengtawesin and Kimberly Chang
## Debugged by: Andrew Saengtawesin and Kimberly Chang

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('claim_tasks', views.claim_tasks, name='claim_tasks'),
	path('view_tasks', views.view_tasks, name='view_tasks'),
	path('claim', views.claim, name='claim'),
	path('complete', views.complete, name='complete'),
]