from django.shortcuts import render,HttpResponse
import random

# Create your views here.


def home(request):
    return render(request,"generator/home.html")


def about(request):
    return render(request,"generator/about.html")


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('#$%^&!'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length',12))
    passwords = ''

    for i in range(length):
        passwords += random.choice(characters)

    return render(request,"generator/password.html",{'password':passwords})