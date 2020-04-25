from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView



# Create your views here.
def indexView(request):
	return render(request, 'homepage.html')

@login_required
def dashboardView(request):
	type=request.session['type']
	if type == 'employee':
		return render(request, 'dashboards/dashboard_employee.html')
	if type == 'manager':
		return render(request, 'dashboards/dashboard_manager.html')
	if type == 'customer':
		return render(request, 'dashboards/dashboard_customer.html')


def cust_login_view(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			#if(get_password(username)==password):#authentication against database
			request.session['type']='customer'
			form.save()
			return redirect('dashboard')#redirect to login page when account creation is successful
			#else:
			#	return redirect('login_url')
	else:
		form=LoginView	
	return render(request, 'registration/login.html', {'form':form})

def emp_login_view(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			#if(get_password(username)==password):#authentication against database
			request.session['type']='employee'
			form.save()
			return redirect('dashboard')#redirect to login page when account creation is successful
			#else:
			#	return redirect('login_url')
	else:
		form=LoginView	
	return render(request, 'registration/login.html', {'form':form})

def manager_login_view(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			#if(get_password(username)==password):#authentication against database
			request.session['type']='manager'
			form.save()
			return redirect('dashboard')#redirect to login page when account creation is successful
			#else:
			#	return redirect('login_url')
	else:
		form=LoginView	
	return render(request, 'registration/login.html', {'form':form})


def registerView(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password2']
			#create_user(username,password,accountType, ID="NULL", first=None, last=None)#add user to database
			#form.save()
			return redirect('login_url')#redirect to login page when account creation is successful
	else:
		form=UserCreationForm()	
	return render(request, 'registration/register.html', {'form':form})

