# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'email': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'username': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'password': forms.PasswordInput(attrs={'class':'form-control','maxlength': 255}),
        }

        error_messages = {
            'first_name': {
                'required': 'Campo obrigatório'
            },
            'last_name': {
                'required': 'Campo obrigatório'
            },
            'email': {
                'required': 'Campo obrigatório'
            },
            'username': {
                'required': 'Campo obrigatório'
            },
            'password': {
                'required': 'Campo obrigatório'
            },
        }
