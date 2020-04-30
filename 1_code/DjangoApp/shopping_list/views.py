from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

import util.db_helper as tm_db

def index(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	list = []
	loggedIn = False
	if type == "Customer":
		loggedIn = True
		list = tm_db.get_user_shopping_list(user)
	context = {'list': list, 'loggedIn': loggedIn}
	return render(request, 'shopping_list/index.html', context)
	
	
@csrf_exempt
def search(request):
	search = ""
	if request.method == 'POST':
		search = request.POST["search"]
	results = tm_db.get_search_result(search)
	context = {'list': results, 'query': search}
	return render(request, 'shopping_list/search.html', context)
	
@csrf_exempt
def add(request):
	item = ""
	if request.method == 'GET':
		item = request.GET["RFID"]
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	tm_db.add_slist_item(user, item)
	type = tm_db.get_account_type(user)
	list = []
	loggedIn = False
	if type == "Customer":
		loggedIn = True
		list = tm_db.get_user_shopping_list(user)
	context = {'list': list, 'loggedIn': loggedIn}
	return render(request, 'shopping_list/index.html', context)


@csrf_exempt
def delete(request):
	item = ""
	if request.method == 'GET':
		item = request.GET["RFID"]
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	tm_db.remove_slist_item(user, item)
	type = tm_db.get_account_type(user)
	list = []
	loggedIn = False
	if type == "Customer":
		loggedIn = True
		list = tm_db.get_user_shopping_list(user)
	context = {'list': list, 'loggedIn': loggedIn}
	return render(request, 'shopping_list/index.html', context)		
		
		
		