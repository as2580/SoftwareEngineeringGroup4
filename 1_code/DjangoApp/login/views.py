## Written by: Abhinandan Vellanki, Andrew Saengtawesin, and Kimberly Chang
## Tested by: Andrew Saengtawesin and Kimberly Chang
## Debugged by: Andrew Saengtawesin and Kimberly Chang

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
	request.session['user'] = ""
	return render(request, 'login/cust.html')
	
	
def custReg(request):
	return render(request, 'login/custReg.html')
	
@csrf_exempt	
def custHome(request):
	if(len(request.session['user'])>0):
		username = request.session['user']
		loggedIn = True
		context = {'user': username, 'loggedIn': loggedIn}
		return render(request, 'home/cust.html', context)
	username = request.POST['username']
	password = request.POST['password']
	
	loggedIn = False
	
	if(password == db_h.get_password(username) and db_h.get_account_type(username) == 'Customer'):
		loggedIn = True
		request.session['user'] = username
		context = {'user': username, 'loggedIn': loggedIn}
		return render(request, 'home/cust.html', context)
	else:
		context = {'alert': "Incorrect Username or Password."}
		return render(request, 'login/cust.html', context)

def empLogin(request):
	request.session['user'] = ""
	return render(request, 'login/emp.html')
	
@csrf_exempt	
def empHome(request):
	if(len(request.session['user'])>0):
		username = request.session['user']
		loggedIn = True
		context = {'user': username, 'loggedIn': loggedIn}
		if(db_h.get_account_type(username) == 'Employee'):
			return render(request, 'home/emp.html', context)
		elif(db_h.get_account_type(username) == 'Manager'):
			return render(request, 'home/man.html', context)
			
	username = request.POST['username']
	password = request.POST['password']
	
	loggedIn = False
	
	if(password == db_h.get_password(username) and db_h.get_account_type(username) != 'Customer'):
		loggedIn = True
		request.session['user'] = username
		context = {'user': username, 'loggedIn': loggedIn}
		if(db_h.get_account_type(username) == 'Employee'):
			return render(request, 'home/emp.html', context)
		elif(db_h.get_account_type(username) == 'Manager'):
			return render(request, 'home/man.html', context)
	else:
		context = {'alert': "Incorrect Username or Password."}
		return render(request, 'login/emp.html', context)


def logout(request):
	request.session['user'] = ""
	return render(request, 'homepage.html')


def hours(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = db_h.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	ID = db_h.get_id(user)
	hours = db_h.get_id_employee_hours(ID)
	checkOutDay = db_h.get_id_null_hours(ID)
	checkedIn = False
	if any(checkOutDay):
		checkedIn = True
	context = {'hours': hours, 'loggedIn': loggedIn, 'checkedIn': checkedIn}
	return render(request, 'login/hours.html', context)
	
	
def checkedIn(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = db_h.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	ID = db_h.get_id(user)
	db_h.add_hours(ID)
	hours = db_h.get_id_employee_hours(ID)
	checkOutDay = db_h.get_id_null_hours(ID)
	checkedIn = False
	if any(checkOutDay):
		checkedIn = True
	context = {'hours': hours, 'loggedIn': loggedIn, 'checkedIn': checkedIn}
	return render(request, 'login/hours.html', context)
	

def checkedOut(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = db_h.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	ID = db_h.get_id(user)
	db_h.add_checkout(ID)
	hours = db_h.get_id_employee_hours(ID)
	checkOutDay = db_h.get_id_null_hours(ID)
	checkedIn = False
	if any(checkOutDay):
		checkedIn = True
	context = {'hours': hours, 'loggedIn': loggedIn, 'checkedIn': checkedIn}
	return render(request, 'login/hours.html', context)


