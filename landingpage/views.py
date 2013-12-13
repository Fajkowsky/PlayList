# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.util import ErrorList
from django.db.models import F, Q
from django.http import HttpResponse
from django.core import serializers
import json

from forms import LoginForm, RegisterForm, SongForm
from models import Song, SongVoted

from songapi import get_song_link


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('frontpage')
            else:
                form._errors['valid'] = ErrorList(
                    [u"nie ma takiego użytkownika"])
    else:
        form = LoginForm()
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


def frontpage(request, data={'voted': True}):
    if request.user.is_authenticated():
        data['voted'] = 1
        if request.method == 'POST':
            form = request.POST.dict()
            data['voted'] = votesong(request.user.id,
                                     form['song_id'], form['vote'])
        data['songs'] = Song.objects.all().order_by('-score_plus')
        return render(request, "frontpage.html", data)
    else:
        return redirect('index')


def addsong(request):
    if request.user.is_authenticated():
        if request.is_ajax():
            form = request.POST.dict()
            response_data = {}
            if form['artist'] and form['song_name']:
                response_data = serializers.serialize("json", Song.objects.filter(
                    artist__contains=form['artist'], song_name__contains=form['song_name']))

            elif form['artist']:
                response_data = serializers.serialize(
                    "json", Song.objects.filter(artist__contains=form['artist']))

            elif form['song_name']:
                response_data = serializers.serialize(
                    "json", Song.objects.filter(song_name__contains=form['song_name']))

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        elif request.method == 'POST':
            if u'vote' in request.POST.dict():
                form = request.POST.dict()
                votesong(request.user.id, int(form['song_id']))
                return redirect('mysong')

            else:
                form = SongForm(request.POST)
                if form.is_valid():
                    song = form.save(commit=False)
                    song.user = request.user
                    song.code = get_song_link(song.artist, song.song_name)
                    song.save()
                    SongVoted(user=request.user, song=song).save()
                    return redirect('mysong')

        else:
            form = SongForm()
        return render(request, "addsong.html", {'form': form})


def mysong(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if u'notthissong' in request.POST.dict():
                form = request.POST.dict()
                Song.objects.filter(id=int(
                    form['song_id'])).update(problem=True)
        return render(request, "mysong.html", {'songs': Song.objects.filter(user=request.user)})


def votesong(user_id, song_id, vote='plus'):
    song = Song.objects.get(id=song_id)
    user = User.objects.get(id=user_id)
    if not SongVoted.objects.filter(user=user, song=song):
        if vote == 'plus':
            song.score_plus += 1
            song.save()
        elif vote == 'minus':
            song.score_minus += 1
            song.save()
        SongVoted(user=user, song=song).save()
        return True
    else:
        return False
