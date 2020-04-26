from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
	path('',views.indexView, name="home"),
	path('cust_login', views.custLogin, name="cust_login"),
	path('cust_home', views.custHome, name="cust_home"),
	path('emp_login', views.empLogin, name="emp_login"),
	path('emp_home', views.empHome, name="emp_home"),
	path('task_board/', views.redirect, name="task_board"),
]