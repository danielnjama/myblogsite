from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def sell(request):
    message="COMMING SOON"
    return render(request,'sell.html',{'message':message})

    