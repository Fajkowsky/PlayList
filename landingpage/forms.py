# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from models import Song


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'nazwa użytkownika'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'hasło', 'type': 'password',}))


class RegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'login', 'type': 'text', 'class': 'form-control', 'placeholder': 'nazwa użytkownika'}),
            'password': forms.TextInput(attrs={'id': 'password', 'type': 'password', 'class': 'form-control', 'placeholder': 'hasło'}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class SongForm(ModelForm):

    class Meta:
        model = Song
        fields = ['artist', 'song_name', 'song_type', 'code']
        widgets = {
            'artist': forms.TextInput(attrs={'id': 'artist', 'type': 'text', 'class': 'form-control', 'placeholder': 'wykonawca'}),
            'song_name': forms.TextInput(attrs={'id': 'songname', 'type': 'text', 'class': 'form-control', 'placeholder': 'tytuł piosenki'}),
            'code': forms.TextInput(attrs={'id': 'code', 'type': 'url', 'class': 'form-control', 'placeholder': 'link do piosenki'}),
        }