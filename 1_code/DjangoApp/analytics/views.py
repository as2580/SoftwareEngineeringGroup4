## Written by: Andrew Saengtawesin and Kimberly Chang
## Tested by: Andrew Saengtawesin and Kimberly Chang
## Debugged by: Andrew Saengtawesin and Kimberly Chang

from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import util.db_helper as tm_db

def index(request):
	return render(request, 'analytics/index.html')
	

def view_hours(request):
	return render(request, 'analytics/view_hours.html')

	
def view_hours(request):
	return render(request, 'analytics/view_latest_hours.html')


def view_month_sales(request):
	return render(request, 'analytics/view_month_sales.html')
	
	
def view_cat_sales(request):
	return render(request, 'analytics/view_cat_sales.html')
