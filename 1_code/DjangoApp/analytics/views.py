## Written by: Andrew Saengtawesin and Kimberly Chang
## Tested by: Andrew Saengtawesin and Kimberly Chang
## Debugged by: Andrew Saengtawesin and Kimberly Chang

from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import util.db_helper as tm_db

def index(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Manager":
		loggedIn = True
	context = {'loggedIn': loggedIn}
	return render(request, 'analytics/index.html', context)


def view_latest_hours(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Manager":
		loggedIn = True
	hours = tm_db.get_latest_employee_hours()
	context = {'hours': hours, 'loggedIn': loggedIn}
	return render(request, 'analytics/view_latest_hours.html', context)
	

def view_hours(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Manager":
		loggedIn = True
	hours = tm_db.get_all_employee_hours()
	context = {'hours': hours, 'loggedIn': loggedIn}
	return render(request, 'analytics/view_hours.html', context)


def view_money_sales(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Manager":
		loggedIn = True
	sales = tm_db.get_all_money_sales()
	context = {'sales': sales, 'loggedIn': loggedIn}
	return render(request, 'analytics/view_money_sales.html', context)
	
	
def view_item_sales(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Manager":
		loggedIn = True
	sales = tm_db.get_all_item_sales()
	context = {'sales': sales, 'loggedIn': loggedIn}
	return render(request, 'analytics/view_item_sales.html', context)
