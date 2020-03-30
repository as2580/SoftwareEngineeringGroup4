from django.shortcuts import get_object_or_404, render
from django.http import *
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from util import db_helper

from check_out import check_out_helper
from .forms import NewItemsForm
# Create your views here.


def index(request):
    base_items = ["308932602", "164885937", "57088767", "750583724", "261603766", "346028340"]
    request.session['items'] = base_items
    items = request.session['items']
    shopping_cart = check_out_helper.LinkedList()
    for i in items:
        info = db_helper.get_item_info(i)
        new_info = [[d['name'] for d in info], [d['price'] for d in info]]
        flat_info = [val for sublist in new_info for val in sublist]
        shopping_cart.insert(flat_info[0], flat_info[1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    request.session['totals'] = totals
    return render(request, 'check_out/index.html', context)


def finish(request):
    totals = request.session['totals']
    context = {'totals': totals, }
    return render(request, 'check_out/Finish.html', context)


def remove_item(request):
    items = request.session['items']
    context = {'items': items}
    return render(request, 'check_out/removeItem.html', context)


def add_items(request):
    new_items = ["553192494", "553192494"]
    items = request.session['items']
    shopping_cart = check_out_helper.LinkedList()
    for i in new_items:
        items.append(i)
    for i in items:
        info = db_helper.get_item_info(i)
        new_info = [[d['name'] for d in info], [d['price'] for d in info]]
        flat_info = [val for sublist in new_info for val in sublist]
        shopping_cart.insert(flat_info[0], flat_info[1])
    info_list = shopping_cart.to_lists()
    totals = shopping_cart.total()
    context = {'info_list': info_list, 'totals': totals, }
    request.session['totals'] = totals
    return render(request, 'check_out/addItems.html', context)


def get_item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewItemsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewItemsForm()

    return render(request, 'newitem.html', {'form': form})

