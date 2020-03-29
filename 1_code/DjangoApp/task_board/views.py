from django.shortcuts import render
from django.http import *

def index(request):
    tasks = tm_db.get_all_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_manager/index.html', context)
