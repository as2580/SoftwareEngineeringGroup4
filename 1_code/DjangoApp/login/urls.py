from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
	path('',views.indexView, name="home"),
	path('cust_login', views.custLogin, name="cust_login"),
	path('cust_home', views.custHome, name="cust_home"),
	path('cust_reg', views.custReg, name="cust_reg"),
	path('emp_reg', views.empReg, name="emp_reg"),
	path('emp_login', views.empLogin, name="emp_login"),
	path('emp_home', views.empHome, name="emp_home"),
	path('loggedout', views.logout, name="loggedout"),
	path('hours', views.hours, name="hours"),
	path('checkedIn', views.checkedIn, name="checkedIn"),
	path('checkedOut', views.checkedOut, name="checkedOut"),
	path('register', views.register, name="register"),
	path('registerE', views.registerE, name="registerE"),
]