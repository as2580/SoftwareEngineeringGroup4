from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

import task_manager.task_manager_db_helper as tm_db

def index(request):
    tasks = tm_db.get_all_tasks()
    context = {'tasks': tasks}
    return render(request, 'task_manager/index.html', context)
