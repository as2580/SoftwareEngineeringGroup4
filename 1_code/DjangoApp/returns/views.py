from django.shortcuts import render
from django.http import *

# Create your views here.
def index(request):
    return render(request, 'returns/index.html')