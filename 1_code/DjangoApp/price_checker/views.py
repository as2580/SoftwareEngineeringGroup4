from django.shortcuts import render
from django.http import *
from util import db_helper

# Create your views here.
def index(request):
    return render(request, 'price_checker/index.html')

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

    return render(request, 'price_checker/index.html', context)