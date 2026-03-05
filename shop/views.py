from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are about us page")

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def produch(request):
    return render(request, 'shop/productview.html')

