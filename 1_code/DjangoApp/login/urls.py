from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns=[
	path('',views.indexView, name="home"),
	path('dashboard/', views.dashboardView, name="dashboard"),
	path('customerlogin/',LoginView.as_view(), name="customer_login_url"),
	path('managerlogin/',LoginView.as_view(), name="manager_login_url"),
	path('employeelogin/',LoginView.as_view(), name="employee_login_url"),
	path('register/',views.registerView, name="register_url"),
	path('logout/',LogoutView.as_view(next_page='home'),name="logout"),#redirect to home after logout
]