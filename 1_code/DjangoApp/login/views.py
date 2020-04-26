from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
import util.db_helper as db_h


# Create your views here.
def indexView(request):
	return render(request, 'homepage.html')


def custLogin(request):
	return render(request, 'login/cust.html')
	
@csrf_exempt	
def custHome(request):
	username = request.POST['username']
	password = request.POST['password']
	
	if(password == db_h.get_password(username) and db_h.get_account_type(username) == 'Customer'):
		context = {'user': username}
		return render(request, 'home/cust.html', context)
	else:
		context = {'alert': "Incorrect Username or Password."}
		return render(request, 'login/cust.html', context)

def empLogin(request):
	return render(request, 'login/emp.html')
	
@csrf_exempt	
def empHome(request):
	username = request.POST['username']
	password = request.POST['password']
	
	if(password == db_h.get_password(username) and db_h.get_account_type(username) != 'Customer'):
		context = {'user': username}
		if(db_h.get_account_type(username) == 'Employee'):
			return render(request, 'home/emp.html', context)
		elif(db_h.get_account_type(username) == 'Manager'):
			return render(request, 'home/man.html', context)
	else:
		context = {'alert': "Incorrect Username or Password."}
		return render(request, 'login/emp.html', context)

def redirect(request):
	return render(request, 'homepage.html')

