from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from util import db_helper

from check_out import check_out_helper
from .forms import NewItemsForm
# Create your views here.

@csrf_exempt
def index(request):
    base_items = ["308932602", "164885937", "57088767", "750583724", "261603766", "346028340"]  # example list
    request.session['items'] = base_items  # global variable declaration
    items = request.session['items']
    shopping_cart = check_out_helper.LinkedList()  # initializing linked list for storage
    for i in items:  # populating linked list with name and price
        info = db_helper.get_item_info(i)
        shopping_cart.insert(info[0][0], info[0][1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    request.session['totals'] = totals
    return render(request, 'check_out/index.html', context)


def finish(request):
    totals = request.session['totals']
    context = {'totals': totals, }
    return render(request, 'check_out/Finish.html', context)

@csrf_exempt
def remove_item(request):
    items = request.session['items']  # not functioning currently
    delitem = int(request.POST['id'])
    shopping_cart = check_out_helper.LinkedList()  # initializing linked list for storage
    deleted = items.pop(delitem)
    taskName = 'Return Items to Shelves(Checkout Terminal 1)'
    taskDescription = 'Return item(s) from bin at Checkout Terminal 1'
    db_helper.add_task(taskName, taskDescription)
    for i in items:
        info = db_helper.get_item_info(i)
        shopping_cart.insert(info[0][0], info[0][1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    request.session['totals'] = totals
    return render(request, 'check_out/removeitem.html', context)

@csrf_exempt
def add_items(request):  # same idea as index
    new_items = ["553192494", "553192494"]
    items = request.session['items']
    shopping_cart = check_out_helper.LinkedList()
    for i in new_items:  # appending new items into global list
        items.append(i)
    for i in items:
        info = db_helper.get_item_info(i)
        #no longer needed for some reason, no clue why
        #new_info = [[d['name'] for d in info], [d['price'] for d in info]]
        # Removing excess delimiters in list and inserting into shopping_cart linked list
        #flat_info = [val for sublist in new_info for val in sublist]
        #shopping_cart.insert(flat_info[0], flat_info[1])
        shopping_cart.insert(info[0][0], info[0][1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    request.session['totals'] = totals
    return render(request, 'check_out/addItems.html', context)

def cash(request):
    totals = request.session['totals']
    change = round(round(totals[1], 0) + 10 - totals[1], 2)
    context = {'totals': totals, 'change': change, }
    return render(request, 'check_out/cash.html', context)

def credit(request):
    totals = request.session['totals']
    context = {'totals': totals, }
    return render(request, 'check_out/credit.html', context)

