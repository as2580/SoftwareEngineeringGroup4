from django.urls import path

from . import views

app_name = 'analytics'
urlpatterns = [
    path('', views.index, name='index'),
	path('view_hours', views.view_hours, name='view_hours'),
	path('view_latest_hours', views.view_hours, name='view_latest_hours'),
	path('view_month_sales', views.view_month_sales, name='view_month_sales'),
	path('view_cat_sales', views.view_cat_sales, name='view_cat_sales'),
]