from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'chandigarh.craigslist.org/search/?query={}'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get('https://final_url')
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    stuff_for_frontend = {
        'search': search,
        }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
    