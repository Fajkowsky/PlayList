# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'nazwa użytkownika'}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'hasło'}))


class RegisterForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'login', 'type': 'text', 'class': 'form-control', 'placeholder': 'nazwa użytkownika'}),
            'first_name': forms.TextInput(attrs={'id': 'name', 'type': 'text', 'class': 'form-control', 'placeholder': 'imię'}),
            'password': forms.TextInput(attrs={'id': 'password', 'type': 'password', 'class': 'form-control', 'placeholder': 'hasło'}),
            'email': forms.TextInput(attrs={'id': 'email', 'type': 'email', 'class': 'form-control', 'placeholder': 'email'}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
