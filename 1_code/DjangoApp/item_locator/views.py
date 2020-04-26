from django.shortcuts import render
from django.http import *
from util import db_helper
from . import forms

# Create your views here.

def index(request):
    return render(request, 'item_locator/index.html')

def search(request):
    search = str(request.GET['name'])
    list = db_helper.get_search_result(search)

    if list == []:
        context = {'location': 'Item Not Found', }
        return render(request, 'item_locator/index.html', context)

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
    return render(request, 'item_locator/index.html', context)

def select(request):
    list = forms.list
    if list == []:
        context = {'location': 'No Item Selected', }
        return render(request, 'item_locator/index.html', context)

    index = int(request.GET['selection'])

    if index >= 0 and index < list.__len__():
        name = str(list[index][0])
        RFID = str(list[index][3])
        location = db_helper.get_location(RFID)

        if location == "":
            forms.list = []
            location = "Item Not Found"

        context = {'name': name, 'location': location, }
        return render(request, 'item_locator/index.html', context)
    else:
        name = "No Item Selected"
        forms.list = []
        context = {'name': name,}
        return render(request, 'item_locator/index.html', context)