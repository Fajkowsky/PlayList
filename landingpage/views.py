from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def frontpage(request):
    return render(request, "frontpage.html")

def register(request):
    return render(request, "register.html")

def addsong(request):
    return render(request, "addsong.html")

def mysong(request):
    return render(request, "mysong.html")
