# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import User_profile, Party, Game
from django.forms import ModelChoiceField


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','username','last_name','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','maxlength': 55, 'placeholder': 'Nome'}),
            'username': forms.TextInput(attrs={'class': 'form-control','maxlength': 15, 'placeholder': 'Nome de usuário' }),
            'email': forms.TextInput(attrs={'class': 'form-control','maxlength': 30, 'placeholder': 'E-mail'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','maxlength': 10, 'placeholder': 'Data de nascimento'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','maxlength': 12, 'placeholder': 'Senha'}),
        }
        error_messages = {
            'first_name': {
                'required': 'Campo obrigatório'
            },
            'username': {
                'required': 'Campo obrigatório'
            },
            'email': {
                'required': 'Campo obrigatório'
            },
            'last_name': {
                'required': 'Campo obrigatório'
            },
            'password': {
                'required': 'Campo obrigatório'
            },
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('tags', 'description', 'profile_img')
        widgets =  {
            'tags': forms.TextInput(attrs={'class': 'form-control','maxlength': 55, 'placeholder': 'Nicknames usados em jogos'}),
            'description': forms.TextInput(attrs={'class': 'form-control','maxlength': 55, 'placeholder': 'Sua descrição como jogador'}),
            }



class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self,obj):
        return obj.name


class PartyForm(forms.ModelForm):
    related_game = MyModelChoiceField(queryset=Game.objects.all(), to_field_name='name')
    class Meta:
        model = Party
        fields = ('related_game','name', 'description', 'party_img')
        widgets =  {
            'name': forms.TextInput(attrs={'class': 'form-control','maxlength': 55, 'placeholder': 'Nome que será mostrado aos demais usuários'}),
            'description': forms.TextInput(attrs={'class': 'form-control','maxlength': 55, 'placeholder': 'Descrição da party'}),
            }
