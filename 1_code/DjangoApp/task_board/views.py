from django.shortcuts import render
from django.http import *

import task_board.task_manager_db_helper as tm_db

def index(request):
    tasks = tm_db.get_all_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_board/index.html', context)


def claim_tasks(request):
    tasks = tm_db.get_incomplete_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_board/claim_tasks.html', context)


def view_tasks(request):
    tasks = tm_db.get_employee_tasks(41)
    context = {'tasks': tasks}
    return render(request, 'task_board/view_tasks.html', context)
