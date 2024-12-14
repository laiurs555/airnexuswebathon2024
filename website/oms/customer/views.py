from django.http import HttpResponse
from django.shortcuts import render
from .models import customer 
# Create your views here.

def index(request):
    customer = customer.object.all()
    return render(request,'base.html',{'customer':customer})

def new (request):
    return HttpResponse("new customer")

