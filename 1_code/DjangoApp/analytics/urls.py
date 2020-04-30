from django.urls import path

from . import views

app_name = 'analytics'
urlpatterns = [
    path('', views.index, name='index'),
	path('view_hours', views.view_hours, name='view_hours'),
	path('view_latest_hours', views.view_latest_hours, name='view_latest_hours'),
	path('view_money_sales', views.view_money_sales, name='view_money_sales'),
	path('view_item_sales', views.view_item_sales, name='view_item_sales'),
]