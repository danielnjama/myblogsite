from django.shortcuts import render
from . models import items
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    products = items.objects.all()
    return render(request,'index.html',{'products':products})


def send_email(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    
    if name and email and subject and message:
        message = ('{} said {}'.format(name,message))
        try:
            send_mail(subject, message, email, ['danielnjama2015@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Thank you for contacting us. we\'ll get back to you shortly')
    else:
        
        return HttpResponse('Make sure all fields are entered and valid.')

def search(request):
    search_results=request.POST.get('choice')
    products = items.objects.filter(types=search_results)
    return render(request,'index.html',{'products':products})