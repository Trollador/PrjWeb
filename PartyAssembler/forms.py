# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Registro_usuario


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registro_usuario
        fields = ['nome','apelido','dta_nasc','email','senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control','maxlength': 255, 'placeholder': 'Nome'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'email': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'dta_nasc': forms.TextInput(attrs={'class': 'form-control','maxlength': 10}),
            'senha': forms.PasswordInput(attrs={'class':'form-control','maxlength': 255}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Registro_usuario
        fields = ['apelido','senha']
        widgets = {
            'apelido': forms.TextInput(attrs={'class': 'form-control','maxlength': 255}),
            'senha': forms.PasswordInput(attrs={'class':'form-control','maxlength': 255}),
        }
