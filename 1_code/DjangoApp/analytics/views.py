## Written by: Andrew Saengtawesin and Kimberly Chang
## Tested by: Andrew Saengtawesin and Kimberly Chang
## Debugged by: Andrew Saengtawesin and Kimberly Chang

from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import util.db_helper as tm_db

def index(request):
	return render(request, 'analytics/index.html')


def view_latest_hours(request):
	hours = get_latest_employee_hours()
	context = {'hours': hours}
	return render(request, 'analytics/view_latest_hours.html', context)
	

def view_hours(request):
	hours = tm_db.get_all_employee_hours()
	context = {'hours': hours}
	return render(request, 'analytics/view_hours.html', context)


def view_money_sales(request):
	sales = tm_db.get_all_money_sales()
	context = {'sales': sales}
	return render(request, 'analytics/view_money_sales.html', context)
	
	
def view_item_sales(request):
	sales = tm_db.get_all_item_sales()
	context = {'sales': sales}
	return render(request, 'analytics/view_item_sales.html', context)
