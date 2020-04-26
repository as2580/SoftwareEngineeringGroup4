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
	if type == "Employee" or type == "Manager":
		loggedIn = True
	context = {'loggedIn': loggedIn}
	return render(request, 'task_board/index.html', context)


def claim_tasks(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	tasks = tm_db.get_incomplete_tasks()
	context = {'tasks': tasks, 'loggedIn': loggedIn}
	return render(request, 'task_board/claim_tasks.html', context)


@csrf_exempt
def view_tasks(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	ID = str(tm_db.get_id(user))
	tasks = []
	if ID.isnumeric and ID:
		tasks = tm_db.get_employee_tasks(ID)
	context = {'tasks': tasks, 'loggedIn': loggedIn}
	return render(request, 'task_board/view_tasks.html', context)
	

@csrf_exempt
def claim(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	if request.method == 'POST':
		ID = tm_db.get_id(user)
		taskID = request.POST["id"]
		tm_db.update_task_state(taskID, "In Progress", ID)
		tasks = tm_db.get_task(taskID)
		context = {'tasks': tasks, 'loggedIn': loggedIn}
		return render(request, 'task_board/claim.html', context)
	else:
		context = {'loggedIn': loggedIn}
		return render(request, 'task_board/index.html', context)


def complete(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	loggedIn = False
	if type == "Employee" or type == "Manager":
		loggedIn = True
	if request.method == 'GET':
		ID = request.GET["employeeID"]
		taskID = request.GET["id"]
		tm_db.update_task_state(taskID, "Complete", ID)
		tasks = tm_db.get_task(taskID)
		context = {'tasks': tasks, 'loggedIn': loggedIn}
		return render(request, 'task_board/complete.html', context)
	else:
		context = {'loggedIn': loggedIn}
		return render(request, 'task_board/index.html', context)
