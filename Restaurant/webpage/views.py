from django.shortcuts import render
from django.http import HttpResponse

def web(request):
    return render(request,'index.html')

def menu(request):
    return render(request,'menu.html')

def admins(request):
    return render(request,'admin.html')

def contact(request):
    return render(request,'contact.html')

def booktable(request):
    return render(request,'booktable.html')

