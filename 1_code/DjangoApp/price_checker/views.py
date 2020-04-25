from django.shortcuts import render
from django.http import *
from util import db_helper

# Create your views here.
def index(request):
    RFID = "308932602"  # example rfid

    request.session['rfid'] = RFID
    item = db_helper.get_item_info(itemID)

    request.session['price'] = float(item.price)
    price = request.session['price']

    request.session['name'] = item.name
    name = request.session['name']

    context = {'name': name, 'price': price, }
    return render(request, 'price_checker/index.html', context)