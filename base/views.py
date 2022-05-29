import email
from django.shortcuts import render
from django.http import HttpResponse
from base.models import Contact


# Create your views here.

def index(request):
    return render(request, "index.html")


def contact(request):
    if request.method=="POST":
        name = request.POST['fname']
        last = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['number']
        contact = Contact.objects.create(name=name, last=last, email=email, phone=phone)
        contact.save()

    return render(request,"contact.html")

def services(request):
    return render(request, "services.html")

def Home(request):
    return render(request, "Basic.html")

def Html(request):
    return render(request, "Html.html")

def datascience(request):
    return render(request, "datascience.html")