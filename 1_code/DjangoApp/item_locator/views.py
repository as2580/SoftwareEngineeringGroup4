from django.shortcuts import render
from django.http import *
from util import db_helper
from . import forms

# Create your views here.


def home_index(request):
    return render(request, 'item_locator/customer_terminal_home.html')


def il_index(request):
    return render(request, 'item_locator/item_locator.html')


def search(request):
    search = str(request.GET['name'])
    list = db_helper.get_search_result(search)

    if list == []:
        context = {'location': 'Item Not Found', }
        return render(request, 'item_locator/item_locator.html', context)

    selection = []
    i = 0
    for item in list:
        selection.append((str(i), str(item[0])))
        i += 1

    form = forms.SelectionForm(selection)

    forms.list = list
    #name = str(list[0][0])
    #RFID = str(list[0][3])
    #location = db_helper.get_location(RFID)

    context = {'form': form,}
    return render(request, 'item_locator/item_locator.html', context)


def select(request):
    list = forms.list
    if list == []:
        context = {'location': 'No Item Selected', }
        return render(request, 'item_locator/item_locator.html', context)

    index = int(request.GET['selection'])

    if index >= 0 and index < list.__len__():
        name = str(list[index][0])
        RFID = str(list[index][3])
        location = db_helper.get_location(RFID)

        if location == "":
            forms.list = []
            location = "Item Not Found"

        context = {'name': name, 'location': location, }
        return render(request, 'item_locator/item_locator.html', context)
    else:
        name = "No Item Selected"
        forms.list = []
        context = {'name': name,}
        return render(request, 'item_locator/item_locator.html', context)


def pc_index(request):
    return render(request, 'item_locator/price_checker.html')


def search_rfid(request):
    RFID = str(request.GET['rfid'])
    if db_helper.get_item_info(RFID):
        item = db_helper.get_item_info(RFID)
        name = "Found Item: " + str(item[0][0])
        price = "Price: $" + str(item[0][1])
        context = {'name': name, 'price': price, }
    else:
        #name = "Error Finding Item"
        #price = "Please Scan Again"
        error = "ERROR FINDING ITEM\nPLEASE SCAN AGAIN"
        context = {'error': error,}

    return render(request, 'item_locator/price_checker.html', context)