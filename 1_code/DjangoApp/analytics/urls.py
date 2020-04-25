from django.urls import path

from . import views

app_name = 'analytics'
urlpatterns = [
    path('', views.index, name='index'),
	path('view_hours', views.view_hours, name='view_hours'),
	path('view_sales', views.view_sales, name='view_sales'),
]