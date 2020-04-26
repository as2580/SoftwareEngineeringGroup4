from django.shortcuts import render
from django.http import *

import util.db_helper as tm_db

def index(request):
	user = ""
	if 'user' in request.session:
		user = request.session['user']
	type = tm_db.get_account_type(user)
	slist = []
	list = []
	loggedIn = False
	if type == "Customer":
		loggedIn = True
		slist = tm_db.get_user_shopping_list(user)
		for line in slist:
			for RFID in line:
				item = tm_db.get_item_info(RFID)
				if item is not None:
					for part in item:
						list.append(part)
	context = {'list': list, 'loggedIn': loggedIn}
	return render(request, 'shopping_list/index.html', context)