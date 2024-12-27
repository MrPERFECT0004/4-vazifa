from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Car,Brand

# Create your views here.
def brand(request:WSGIRequest):
    brands = Brand.objects.all()
    {"brands":brands}
    return render(request,"brand.html",{"brands":brands})

def car(request:WSGIRequest):
    cars = Car.objects.all()
    return render(request,"car.html",{"cars":cars})