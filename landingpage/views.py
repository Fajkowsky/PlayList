from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms.util import ErrorList

from forms import LoginForm, RegisterForm

def index(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, "index.html", {'form': form})

def frontpage(request):
    return render(request, "frontpage.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})

def addsong(request):
    return render(request, "addsong.html")

def mysong(request):
    return render(request, "mysong.html")
