from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'assets/assets.html')

def assest(request):
    return render(request, 'assets/asset.html')

def index(request):
    return render(request, 'listings/search.html')