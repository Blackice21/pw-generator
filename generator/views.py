from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def aboutme(request):
    return render(request, 'generator/aboutme.html')

def password(request):

    thepassword = ''
    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend('ABCDEFGHIJKLMNOPQRSTUVWSYZ')
    
    if request.GET.get('numbers'):
        char.extend('123456789')

    if request.GET.get('speacial'):
        char.extend('!@#$%^&*()-=.')

    length = int(request.GET.get('length'))

    for i in range(length):
        thepassword += random.choice(char)
    return render(request, 'generator/password.html', {'password': thepassword})
