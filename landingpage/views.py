# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.util import ErrorList

from forms import LoginForm, RegisterForm, SongForm
from models import Song


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            print user
            if user is not None:
                login(request, user)
                return redirect('frontpage')
            else:
                form._errors['valid'] = ErrorList(
                    [u"nie ma takiego użytkownika"])
    else:
        form = LoginForm()
    print request.user
    return render(request, "index.html", {'form': form, 'user': request.user})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def logouting(request):
    logout(request)
    return redirect('index')


def frontpage(request):
    if request.user.is_authenticated():
        return render(request, "frontpage.html", {'songs': Song.objects.all()})
    else:
        return redirect('index')

def addsong(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = SongForm(request.POST)
            if form.is_valid():
                song = form.save(commit=False)
                song.user = request.user
                song.save()
                return redirect('frontpage')
        else:
            form = SongForm()
        return render(request, "addsong.html", {'form': form})


def mysong(request):
    if request.user.is_authenticated():
        return render(request, "mysong.html", {'songs': Song.objects.filter(user=request.user)})
