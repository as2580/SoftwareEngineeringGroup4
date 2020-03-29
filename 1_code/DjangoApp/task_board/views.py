from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

from .forms import EmployeeIDForm

import task_board.task_manager_db_helper as tm_db

def index(request):
    tasks = tm_db.get_all_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_board/index.html', context)


def claim_tasks(request):
    tasks = tm_db.get_incomplete_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_board/claim_tasks.html', context)

@csrf_exempt
def view_tasks(request):
	if request.method == 'POST':
		ID = request.POST["employeeID"]
		tasks = tm_db.get_employee_tasks(ID)
		context = {'tasks': tasks}
		return render(request, 'task_board/view_tasks.html', context)
	else:
		form = EmployeeIDForm()
	return render(request, 'index.html', {'form': form})
